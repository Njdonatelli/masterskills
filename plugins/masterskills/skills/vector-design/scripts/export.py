import argparse
import subprocess
import os
import sys

DESIGNS_DIR = "vector-designs"

def get_design_path(design_name):
    return os.path.join(DESIGNS_DIR, design_name)

def export_svg(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    cmd = [
        "inkscape",
        input_path,
        "--export-type=pdf",
        f"--export-filename={output_path}"
    ]
    cmd.append("--export-area-page")

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        print(f"Export failed:\n{result.stderr}")
    else:
        print(f"→ exported {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Export SVG to Print PDF via Inkscape CLI")
    parser.add_argument("--output", required=True, help="Output PDF path")
    parser.add_argument("--design", "-d", help="Design name (folder in vector-designs/)")
    args = parser.parse_args()

    if args.design:
        design_path = get_design_path(args.design)
    else:
        designs = [d for d in os.listdir(DESIGNS_DIR) if os.path.isdir(os.path.join(DESIGNS_DIR, d))]
        if not designs:
            print("No designs found. Use --design to specify one.")
            sys.exit(1)
        design_name = max(designs, key=lambda d: os.path.getmtime(os.path.join(DESIGNS_DIR, d)))
        design_path = get_design_path(design_name)
        print(f"Using design: {design_name}")

    input_svg = os.path.join(design_path, "canvas.svg")
    export_svg(input_svg, args.output)

if __name__ == "__main__":
    main()