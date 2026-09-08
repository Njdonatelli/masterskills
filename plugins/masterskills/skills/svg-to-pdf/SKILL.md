---
name: svg-to-pdf
description: Convert one or more SVG files to PDF using Inkscape. Use when the user asks to convert SVG(s) to PDF, batch-convert a folder of SVGs, or export vector graphics to PDF.
---

# SVG to PDF Conversion

Converts SVG files to PDF using the Inkscape CLI (installed at `C:\Program Files\Inkscape\bin\inkscape.exe` on this machine).

## Steps

1. Identify the target: a single SVG file, a list of files, or a folder to batch-convert (`*.svg`).
2. Verify Inkscape is available:
   ```
   where inkscape
   ```
   If missing, fall back to `rsvg-convert` or Python `cairosvg` if installed; otherwise tell the user Inkscape needs to be installed.
3. Convert a single file:
   ```bash
   "/c/Program Files/Inkscape/bin/inkscape.exe" "input.svg" --export-type=pdf --export-filename="output.pdf"
   ```
4. Batch-convert a folder (same basename, .pdf extension, written alongside the source SVGs):
   ```bash
   cd "<folder>" && for f in *.svg; do
     "/c/Program Files/Inkscape/bin/inkscape.exe" "$f" --export-type=pdf --export-filename="${f%.svg}.pdf"
   done
   ```
5. Verify output count matches input count (`ls *.pdf | wc -l`) before reporting done.

## Notes

- Default output location is the same directory as the source SVG, same base filename, unless the user specifies otherwise.
- Do not overwrite existing PDFs without confirming if they look like pre-existing (non-generated) files — check `git status`/timestamps if in doubt.
- This is a one-shot batch operation — no need to build a general-purpose tool or script file beyond the inline loop.
