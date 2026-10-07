---
name: "performance-profiler"
description: >-
  S—y—s—t—e—m—a—t—i—c— —p—e—r—f—o—r—m—a—n—c—e— —p—r—o—f—i—l—i—n—g— —f—o—r— —N—o—d—e—.—j—s—,— —P—y—t—h—o—n—,— —a—n—d— —G—o— —a—p—p—l—i—c—a—t—i—o—n—s—.— —I—d—e—n—t—i—f—i—e—s— —C—P—U—,— —m—e—m—o—r—y—,— —a—n—d— —I—/—O— —b—o—t—t—l—e—n—e—c—k—s—,— —g—e—n—e—r—a—t—e—s— —f—l—a—m—e—g—r—a—p—h—s—,— —a—n—a—l—y—z—e—s— —b—u—n—d—l—e— —s—i—z—e—s—,— —o—p—t—i—m—i—z—e—s— —d—a—t—a—b—a—s—e— —q—u—e—r—i—e—s—,— —r—u—n—s— —l—o—a—d— —t—e—s—t—s— —w—i—t—h— —k—6— —a—n—d— —A—r—t—i—l—l—e—r—y—.— —A—l—w—a—y—s— —m—e—a—s—u—r—e—s— —b—e—f—o—r—e— —a—n—d— —a—f—t—e—r—.— —U—s—e— —w—h—e—n— —i—n—v—e—s—t—i—g—a—t—i—n—g— —a— —s—l—o—w— —e—n—d—p—o—i—n—t—,— —p—l—a—n—n—i—n—g— —a— —p—e—r—f—o—r—m—a—n—c—e— —b—u—d—g—e—t—,— —o—r— —h—u—n—t—i—n—g— —a— —m—e—m—o—r—y— —l—e—a—k— —i—n— —p—r—o—d—u—c—t—i—o—n.
---

# Performance Profiler

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Performance Engineering  

---

## Overview

Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks; generates flamegraphs; analyzes bundle sizes; optimizes database queries; detects memory leaks; and runs load tests with k6 and Artillery. Always measures before and after.

## Core Capabilities

- **CPU profiling** — flamegraphs for Node.js, py-spy for Python, pprof for Go
- **Memory profiling** — heap snapshots, leak detection, GC pressure
- **Bundle analysis** — webpack-bundle-analyzer, Next.js bundle analyzer
- **Database optimization** — EXPLAIN ANALYZE, slow query log, N+1 detection
- **Load testing** — k6 scripts, Artillery scenarios, ramp-up patterns
- **Before/after measurement** — establish baseline, profile, optimize, verify

---

## When to Use

- App is slow and you don't know where the bottleneck is
- P99 latency exceeds SLA before a release
- Memory usage grows over time (suspected leak)
- Bundle size increased after adding dependencies
- Preparing for a traffic spike (load test before launch)
- Database queries taking >100ms

---

## Quick Start

```bash
# Analyze a project for performance risk indicators
python3 scripts/performance_profiler.py /path/to/project

# JSON output for CI integration
python3 scripts/performance_profiler.py /path/to/project --json

# Custom large-file threshold
python3 scripts/performance_profiler.py /path/to/project --large-file-threshold-kb 256
```

---

## Golden Rule: Measure First

```bash
# Establish baseline BEFORE any optimization
# Record: P50, P95, P99 latency | RPS | error rate | memory usage

# Wrong: "I think the N+1 query is slow, let me fix it"
# Right: Profile → confirm bottleneck → fix → measure again → verify improvement
```

---

## Node.js Profiling
→ See references/profiling-recipes.md for details

## References

- [references/profiling-recipes.md](references/profiling-recipes.md) — Node.js/Python/Go profiling commands, flamegraph generation, heap snapshots
- [references/optimization-playbook.md](references/optimization-playbook.md) — before/after measurement template, quick-win optimization checklist (DB/Node/bundle/API), common pitfalls, best practices

