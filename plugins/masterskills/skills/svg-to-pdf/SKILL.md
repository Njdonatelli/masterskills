---
name: svg-to-pdf
description: >-
  C—o—n—v—e—r—t— —o—n—e— —o—r— —m—o—r—e— —S—V—G— —f—i—l—e—s— —t—o— —P—D—F— —u—s—i—n—g— —I—n—k—s—c—a—p—e—.— —U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —a—s—k—s— —t—o— —c—o—n—v—e—r—t— —S—V—G—(—s—)— —t—o— —P—D—F—,— —b—a—t—c—h—-—c—o—n—v—e—r—t— —a— —f—o—l—d—e—r— —o—f— —S—V—G—s—,— —o—r— —e—x—p—o—r—t— —v—e—c—t—o—r— —g—r—a—p—h—i—c—s— —t—o— —P—D—F.
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
