---
name: bulk-youtube-download
description: >-
  Use when the user wants to download many videos or audio tracks at once from YouTube or any other yt-dlp-supported site — a list of links, whole playlists, or a channel's /videos or /shorts tab — with subtitles, thumbnail, metadata and chapters embedded and output organized into per-playlist folders. Trigger phrases: 'bulk download these videos', 'download this playlist', 'download every video from this channel', 'archive these YouTube links', 'rip the audio from these videos'. Wraps EDM115/bulk-youtube-download (yt-dlp + FFmpeg). Do NOT use for transcripts, search, or channel metadata without downloading files (use youtube-full).
license: "MIT"
---

# bulk-youtube-download — Batch Video Downloads via yt-dlp

Downloads every URL in a list (single videos, playlists, channel tabs, mixed) with one yt-dlp
pass per URL, using archive-quality defaults.

> **Source:** Ported from [EDM115/bulk-youtube-download](https://github.com/EDM115/bulk-youtube-download)
> (MIT, © 2023 EDM115) at commit `79e6145`. `scripts/` holds the upstream scripts unmodified;
> `LICENSE` is the upstream license.

Only download content the user owns, has permission to download, or that is licensed for it.
YouTube's Terms of Service restrict downloading outside its own offline feature.

## Bundled files

| Path | Use |
|---|---|
| `scripts/bulk-youtube-download.sh` | Bash (Linux/macOS/Git Bash). Non-interactive — safe for the agent to run. |
| `scripts/bulk-youtube-download.bat` | Command Prompt. Ends with `pause`, so it blocks a non-interactive run. Hand it to the user; do not run it as the agent. |

Both read `links.txt` from the **current working directory** and write to `./downloads/`. The
script directory is the base directory shown when this skill loads — referred to below as
`SKILL_DIR`.

## Prerequisites

| Tool | Why | Checked by script? |
|---|---|---|
| `yt-dlp` (current release) | Downloader. YouTube breaks old versions within weeks. | Yes |
| `ffmpeg` + `ffprobe` | Merging video+audio, embedding subs/thumbnail/chapters. | Yes |
| JS runtime: Deno (default) or Node | YouTube's player challenge. Without one yt-dlp warns and formats go missing. | **No** — verify it yourself |

If `yt-dlp` came from `pip`, upgrade with the `[default]` extra so the EJS challenge solver is
included. If Deno is absent but Node is installed, append `--js-runtimes node` to the run.

## Workflow (agent-driven)

1. **Pick a working directory** for the output (ASSUMPTION if unstated: a new folder under the
   current project or the user's Downloads, never the skill directory).
2. **Write `links.txt`** there. Either format parses:
   - JSON array of URL strings (upstream's documented format), or
   - one URL per line.

   The `.sh` parser strips all whitespace, double quotes and one trailing comma per line, and
   drops lines that are exactly `[` or `]`. Anything else on a line becomes a URL — no comments.
3. **Preflight** (Bash/Zsh):

   ```bash
   yt-dlp --version && ffmpeg -version | head -1 && (deno --version || node --version)
   ```

   Success: a yt-dlp date version, an ffmpeg version line, and a Deno or Node version.
4. **Dry run first** when the list contains playlists or channels — they can expand to
   hundreds of files. From the working directory (Bash/Zsh):

   ```bash
   bash "SKILL_DIR/scripts/bulk-youtube-download.sh" -s --flat-playlist --print "%(title)s [%(id)s]"
   ```

   Substitute `SKILL_DIR` with the skill's base directory. Success: one `Title [id]` line per
   video, ending with `🎉 Download done !` (nothing is downloaded with `-s`). Report the count to
   the user before a large real run.
5. **Real run** — same command without the simulate flags, plus any overrides:

   ```bash
   bash "SKILL_DIR/scripts/bulk-youtube-download.sh"
   ```

   Extra args are appended after the defaults; yt-dlp lets the later value win, so they
   override duplicates.
6. **Verify**: list `downloads/` and scan the log for `ERROR:` lines. `--ignore-errors` is in the
   defaults, so a failed URL does not stop the batch and the script still prints "done".

### Windows without Bash

Do not run the `.bat` as the agent (it ends in `pause`). Call yt-dlp directly with the same
defaults and a plain one-URL-per-line file (PowerShell; `urls.txt` in the current directory):

```powershell
yt-dlp -f "bestvideo+bestaudio/best" --embed-subs --embed-thumbnail --embed-metadata --embed-chapters --yes-playlist --windows-filenames --concurrent-fragments 4 --ignore-errors -P "downloads" -o "%(playlist_title|.)s/%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s" -a urls.txt
```

Success: a `downloads` folder with the files. In PowerShell `%` needs no escaping; inside a
`.bat` or Command Prompt `for` loop it must be doubled (`%%(title)s`).

## Defaults the script applies

```text
-f "bestvideo+bestaudio/best"
--embed-subs --embed-thumbnail --embed-metadata --embed-chapters
--yes-playlist --progress --console-title
--concurrent-fragments 4 --ignore-errors
-P "downloads"
-o "%(playlist_title|.)s/%(playlist_index&{} - |)s%(title)s [%(id)s].%(ext)s"
```

The `.bat` additionally passes `--windows-filenames`. Resulting layout:

```text
downloads/
├── Video title [VideoID].webm            # single video
└── Playlist or channel tab name/
    ├── 1 - Video title [VideoID].webm
    └── 2 - Video title [VideoID].webm
```

`bestvideo+bestaudio` usually merges to `.webm` or `.mkv`, not `.mp4`. If the user needs MP4,
add `--merge-output-format mp4` (or `-S ext:mp4:m4a` to prefer natively-MP4 streams and avoid a
remux). `--embed-subs` only works on mp4/webm/mkv containers.

## Common overrides

| Need | Append |
|---|---|
| Cap resolution | `-f "bestvideo[height<=720]+bestaudio/best"` |
| Audio only (MP3) | `-x --audio-format mp3` |
| Skip playlist expansion | `--no-playlist` |
| Private / age-restricted / members-only | `--cookies-from-browser chrome` (or `firefox`, `edge`, …) |
| List formats only | `-s -F` |
| Specific subtitle languages | `--sub-langs "en.*,es"` (list with `--list-subs`) |
| Strip sponsor segments | `--force-keyframes-at-cuts --sponsorblock-remove sponsor,selfpromo` |
| Re-runnable / incremental archive | `--download-archive downloaded.txt` |
| Throttle to avoid rate limits | `--sleep-requests 1 --sleep-interval 5 --max-sleep-interval 15` |

Full option reference: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

`--download-archive` is not in upstream defaults but is the right call for any channel or
playlist the user may re-sync: re-runs skip already-downloaded IDs instead of re-fetching
metadata for each file.

## Channels

yt-dlp expands `https://www.youtube.com/@handle/videos` and `/shorts` tabs directly — no need
for upstream's browser-console URL-scraping trick. Use the console snippet only when yt-dlp
cannot enumerate a page:

```js
copy(Array.from(new Set(Array.from(document.links).filter((l) => l.href?.includes("watch?v=")).map((x) => x.href.split("&")[0]))))
```

(Run in the browser DevTools console on the fully scrolled Videos tab; it copies a JSON array
ready to paste into `links.txt`.)

## Failure triage

| Symptom | Cause / fix |
|---|---|
| `No supported JavaScript runtime could be found` | Install Deno, or add `--js-runtimes node`. |
| `Sign in to confirm your age` / `Private video` | Add `--cookies-from-browser <browser>`. |
| `Sign in to confirm you're not a bot`, HTTP 429 | Rate limited — add cookies and the sleep flags above, retry later. |
| `Video unavailable in your country` | Geo-restriction; not fixable from the script. |
| Extraction errors on many videos at once | Outdated yt-dlp — update it first (`yt-dlp -U` for the standalone binary, `pip install -U "yt-dlp[default]"` for pip). |
| `ffprobe not found` | FFmpeg install lacks `ffprobe`; install a full FFmpeg build. |
