/**
 * Gemini Ultracode Dynamic Workflow Runtime for Antigravity CLI / IDE (agy)
 *
 * Emulates the "Code-as-Orchestrator" architecture of Anthropic Claude's Ultracode
 * using Google's Gemini 3.8 Flash (`gemini-3.8-flash`) via the Google Gen AI SDK.
 *
 * Architecture Highlights:
 * 1. State Isolation: Loops, branching, and intermediate results live in Node.js runtime memory,
 *    never bloating the model's conversational context window.
 * 2. Tunable Reasoning: Configures Gemini 3.8 Flash's native `thinking_level` ("low", "medium", "high").
 * 3. Bounded Concurrency & Prefix Cache Warming: Fanning out with `pipeline()` staggers start times
 *    to leverage Gemini Context Caching across parallel workers.
 * 4. Adversarial Verification: Independent subagent quality gates before merging findings.
 */

import { GoogleGenAI } from "@google/genai";

// ============================================================================
// Types & Interfaces
// ============================================================================

export type ThinkingLevel = "low" | "medium" | "high";

export interface AgentOptions {
  model?: string;
  thinkingLevel?: ThinkingLevel;
  systemInstruction?: string;
  responseSchema?: Record<string, unknown>;
  tools?: Array<Record<string, unknown>>;
  label?: string;
  maxRetries?: number;
}

export interface AgentResult<T = unknown> {
  id: string;
  label?: string;
  output: T;
  rawText: string;
  tokensUsed?: {
    promptTokens: number;
    candidatesTokens: number;
    totalTokens: number;
  };
  durationMs: number;
}

export interface WorkflowMeta {
  name: string;
  description: string;
  author?: string;
  version?: string;
}

export interface ConcurrencyOptions {
  maxConcurrency?: number;
  cacheStaggerMs?: number; // ms to pause before releasing sibling fan-out calls to prime prefix cache
}

// ============================================================================
// Execution Harness Class
// ============================================================================

export class GeminiUltracodeRuntime {
  private client: GoogleGenAI;
  private defaultModel = "gemini-3.8-flash";
  private defaultThinkingLevel: ThinkingLevel = "medium";
  private activePhase = "Default";
  private agentCounter = 0;
  private maxConcurrency = 16;
  private cacheStaggerMs = 500;

  constructor(apiKey?: string, options?: ConcurrencyOptions) {
    this.client = new GoogleGenAI({
      apiKey: apiKey || process.env.GEMINI_API_KEY || "",
    });
    if (options?.maxConcurrency) this.maxConcurrency = options.maxConcurrency;
    if (options?.cacheStaggerMs !== undefined) this.cacheStaggerMs = options.cacheStaggerMs;
  }

  /**
   * Defines a stage header in the terminal/UI execution trace.
   */
  public phase(title: string): void {
    this.activePhase = title;
    console.log(`\n\x1b[35m=== [Phase: ${title}] ===\x1b[0m`);
  }

  /**
   * Logs runtime telemetry or script annotations.
   */
  public log(message: string): void {
    console.log(`\x1b[36m[Ultracode Runtime]\x1b[0m ${message}`);
  }

  /**
   * Spawns an isolated subagent worker powered by Gemini 3.8 Flash.
   */
  public async agent<T = string>(prompt: string, options: AgentOptions = {}): Promise<AgentResult<T>> {
    const agentId = `worker-${++this.agentCounter}`;
    const model = options.model || this.defaultModel;
    const thinkingLevel = options.thinkingLevel || this.defaultThinkingLevel;
    const label = options.label || agentId;
    const maxRetries = options.maxRetries ?? 3;

    let attempt = 0;
    const startTime = Date.now();

    while (attempt <= maxRetries) {
      attempt++;
      try {
        // Uses the official Gemini 3.8 Interactions API structure
        const generationConfig: Record<string, unknown> = {
          thinking_level: thinkingLevel, // "low" | "medium" | "high" per Sept 2026 specs
        };

        if (options.responseSchema) {
          generationConfig.response_mime_type = "application/json";
          generationConfig.response_schema = options.responseSchema;
        }

        const payload: Record<string, unknown> = {
          model,
          input: prompt,
          generation_config: generationConfig,
        };

        if (options.systemInstruction) {
          payload.system_instruction = options.systemInstruction;
        }

        if (options.tools && options.tools.length > 0) {
          payload.tools = options.tools;
        }

        const interaction = await this.client.interactions.create(payload as any);
        const rawText = (interaction as any).output_text || "";

        let parsedOutput: T;
        if (options.responseSchema) {
          parsedOutput = JSON.parse(rawText) as T;
        } else {
          parsedOutput = rawText as unknown as T;
        }

        const durationMs = Date.now() - startTime;
        console.log(`  \x1b[32m✔\x1b[0m [${this.activePhase}] ${label} completed in ${durationMs}ms`);

        return {
          id: agentId,
          label,
          output: parsedOutput,
          rawText,
          durationMs,
        };
      } catch (err: any) {
        if (attempt <= maxRetries) {
          console.warn(`  \x1b[33m⚠\x1b[0m [${this.activePhase}] ${label} attempt ${attempt} failed: ${err.message}. Retrying...`);
          await new Promise((res) => setTimeout(res, 1000 * attempt));
        } else {
          console.error(`  \x1b[31m✖\x1b[0m [${this.activePhase}] ${label} permanently failed after ${maxRetries} retries.`);
          throw err;
        }
      }
    }

    throw new Error(`Agent ${agentId} exhausted execution retries.`);
  }

  /**
   * Executes tasks concurrently across a bounded worker pool.
   */
  public async parallel<T>(tasks: Array<() => Promise<T>>): Promise<T[]> {
    const results: T[] = [];
    const queue = [...tasks.entries()];
    const poolSize = Math.min(this.maxConcurrency, tasks.length);

    const worker = async () => {
      while (queue.length > 0) {
        const item = queue.shift();
        if (!item) break;
        const [index, taskFn] = item;
        results[index] = await taskFn();
      }
    };

    const pool = Array.from({ length: poolSize }, () => worker());
    await Promise.all(pool);
    return results;
  }

  /**
   * Bounded fan-out across an array of items with cache-warming prefix staggering.
   */
  public async pipeline<I, O>(
    items: I[],
    taskGenerator: (item: I, index: number) => Promise<O>
  ): Promise<O[]> {
    const tasks: Array<() => Promise<O>> = items.map((item, index) => {
      return async () => {
        // Stagger first few calls to prime the prompt/system-instruction cache
        if (index > 0 && index < this.maxConcurrency && this.cacheStaggerMs > 0) {
          await new Promise((resolve) => setTimeout(resolve, this.cacheStaggerMs));
        }
        return await taskGenerator(item, index);
      };
    });

    return await this.parallel(tasks);
  }
}

// ============================================================================
// Blueprint: Antigravity Dynamic Workflow Example
// ============================================================================

export const meta: WorkflowMeta = {
  name: "gemini-ultracode-repo-audit",
  description: "Audits repository route handlers for security flaws using parallel workers and adversarial verification.",
  version: "1.0.0",
};

/**
 * Example workflow function that can be executed directly by Antigravity CLI:
 * `agy workflow run ./gemini_ultracode_runtime.ts`
 */
export async function runWorkflow(args: { targetDirectory?: string } = {}) {
  const runtime = new GeminiUltracodeRuntime(process.env.GEMINI_API_KEY, {
    maxConcurrency: 12,
    cacheStaggerMs: 300,
  });

  const targetDir = args.targetDirectory || "src/api/routes";
  runtime.log(`Targeting directory: ${targetDir}`);

  // --------------------------------------------------------------------------
  // Phase 1: Code Discovery & AST Mapping
  // --------------------------------------------------------------------------
  runtime.phase("Discovery");
  const discoveryResult = await runtime.agent<{ files: string[] }>(
    `Scan the codebase and return a list of API route handlers inside ${targetDir}. Output strictly as JSON.`,
    {
      label: "Codebase Discovery Agent",
      thinkingLevel: "medium",
      responseSchema: {
        type: "OBJECT",
        properties: {
          files: {
            type: "ARRAY",
            items: { type: "STRING" },
          },
        },
        required: ["files"],
      },
    }
  );

  const routeFiles = discoveryResult.output.files || [
    "src/api/routes/auth.ts",
    "src/api/routes/billing.ts",
    "src/api/routes/users.ts",
  ];
  runtime.log(`Discovered ${routeFiles.length} route files to inspect.`);

  // --------------------------------------------------------------------------
  // Phase 2: Parallel Code Audit (Worker Fan-Out)
  // --------------------------------------------------------------------------
  runtime.phase("Audit Fan-Out");
  const auditFindings = await runtime.pipeline(routeFiles, async (file) => {
    return await runtime.agent<{ file: string; issues: Array<{ title: string; severity: string; description: string }> }>(
      `Audit the endpoint implementation in '${file}' for missing authorization guards, IDOR, or unvalidated params.`,
      {
        label: `Audit: ${file}`,
        thinkingLevel: "medium",
        systemInstruction: "You are an expert AppSec auditor specializing in high-throughput static vulnerability detection.",
        responseSchema: {
          type: "OBJECT",
          properties: {
            file: { type: "STRING" },
            issues: {
              type: "ARRAY",
              items: {
                type: "OBJECT",
                properties: {
                  title: { type: "STRING" },
                  severity: { type: "STRING", enum: ["LOW", "MEDIUM", "HIGH", "CRITICAL"] },
                  description: { type: "STRING" },
                },
                required: ["title", "severity", "description"],
              },
            },
          },
          required: ["file", "issues"],
        },
      }
    );
  });

  // Flatten collected issues
  const rawIssues = auditFindings.flatMap((finding) =>
    finding.output.issues.map((issue) => ({ file: finding.output.file, ...issue }))
  );
  runtime.log(`Extracted ${rawIssues.length} candidate security issues across all files.`);

  // --------------------------------------------------------------------------
  // Phase 3: Adversarial Verification (Quality Gate)
  // --------------------------------------------------------------------------
  runtime.phase("Adversarial Verification");
  const verifiedIssues = await runtime.pipeline(rawIssues, async (candidate, idx) => {
    return await runtime.agent<{ isTruePositive: boolean; confidenceScore: number; rationale: string }>(
      `Critique this reported vulnerability and determine if it is a true positive or hallucination/false positive:\n` +
      `File: ${candidate.file}\nIssue: ${candidate.title}\nSeverity: ${candidate.severity}\nDetails: ${candidate.description}`,
      {
        label: `Verifier #${idx + 1}: ${candidate.title}`,
        thinkingLevel: "high", // Escalate reasoning for adversarial audit
        systemInstruction: "You are a skeptical Principal Security Engineer. Attempt to disprove the vulnerability candidate.",
        responseSchema: {
          type: "OBJECT",
          properties: {
            isTruePositive: { type: "BOOLEAN" },
            confidenceScore: { type: "NUMBER" },
            rationale: { type: "STRING" },
          },
          required: ["isTruePositive", "confidenceScore", "rationale"],
        },
      }
    );
  });

  const verifiedReport = rawIssues.filter((_, idx) => verifiedIssues[idx].output.isTruePositive);
  runtime.log(`Verification completed: ${verifiedReport.length} of ${rawIssues.length} issues confirmed.`);

  // --------------------------------------------------------------------------
  // Phase 4: Final Synthesis & Actionable Remediation Plan
  // --------------------------------------------------------------------------
  runtime.phase("Synthesis");
  const finalSummary = await runtime.agent<string>(
    `Generate a concise, prioritized Markdown security remediation report for the development team based on these verified issues:\n` +
    JSON.stringify(verifiedReport, null, 2),
    {
      label: "Report Synthesizer",
      thinkingLevel: "high",
    }
  );

  return {
    verifiedCount: verifiedReport.length,
    report: finalSummary.output,
  };
}

// Allow CLI invocation
if (require.main === module) {
  runWorkflow()
    .then((result) => {
      console.log("\n\x1b[32m=== FINAL REMEDIATION DELIVERABLE ===\x1b[0m\n");
      console.log(result.report);
    })
    .catch((err) => {
      console.error("Workflow failed:", err);
      process.exit(1);
    });
}
