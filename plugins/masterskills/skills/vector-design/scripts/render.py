import argparse
import sys
import os

try:
    import resvg_py
except ImportError:
    print("Error: resvg-py not found. Run with: uv run --with resvg-py python render.py")
    sys.exit(1)

# Auto-detect skill location (works when installed via npx or run from project)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
DESIGNS_DIR = os.path.join(SKILL_DIR, "vector-designs")

def get_design_path(design_name):
    return os.path.join(DESIGNS_DIR, design_name)

def list_designs():
    if not os.path.exists(DESIGNS_DIR):
        return []
    return [d for d in os.listdir(DESIGNS_DIR) if os.path.isdir(os.path.join(DESIGNS_DIR, d))]

def create_design(design_name):
    path = get_design_path(design_name)
    if os.path.exists(path):
        print(f"Design '{design_name}' already exists at {path}")
        return path
    os.makedirs(path)
    
    default_svg = '''<svg width="800" height="800" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <!-- PREMIUM DESIGN GUIDANCE:
       - Avoid: purple gradients, Inter font, all rounded corners
       - Use: solid colors, sharp/sharp+rounded mix, Helvetica/Arial
       - Aim for: asymmetry, intentional hierarchy, restrained palette
       - Remember: Intentional > Generic
  -->
  <rect id="background" width="80" height="80" fill="#0A0A0A"/>
  
  <!-- Symbol (logomark) — geometric, interconnected paths
       Examples: intersecting lines, peaks/waves, layered shapes
       Premium tip: Keep it simple. 2-3 shapes max.
  -->
  <g id="symbol">
    <!-- Your symbol geometry here -->
  </g>
  
  <!-- Wordmark (logotype) — optional
       Use: font-weight="bold" letter-spacing for caps
  -->
  <text id="wordmark" x="40" y="70" font-family="Helvetica, Arial, sans-serif" 
        font-size="10" font-weight="bold" fill="#FFFFFF" 
        text-anchor="middle" letter-spacing="0.15em">BRAND</text>
</svg>'''
    with open(os.path.join(path, "canvas.svg"), "w") as f:
        f.write(default_svg)
    print(f"Created design '{design_name}' at {path}")
    return path

def create_brief(design_name):
    """Interactive brief gathering for premium design."""
    print("\n" + "="*50)
    print("BRIEF GATHERING — Premium Design")
    print("="*50)
    print("Answer these to ensure unique, non-generic output:\n")
    
    path = get_design_path(design_name)
    os.makedirs(path, exist_ok=True)
    
    print("1. References — What logos/brands do you like?")
    print("   (Give names or URLs — we'll extract what makes them work)")
    references = input("   > ").strip() or "None provided"
    
    print("\n2. What to AVOID — Any styles you hate?")
    print("   (e.g., gradients, rounded, purple, modern generic)")
    avoid = input("   > ").strip() or "None"
    
    print("\n3. Colors — Any brand colors to use? Or preferences?")
    print("   (e.g., 'red and black', 'navy', 'warm tones')")
    colors = input("   > ").strip() or "None provided"
    
    print("\n4. Mood — 3 keywords describing desired feel")
    print("   (e.g., bold, minimal, luxurious, playful)")
    mood = input("   > ").strip() or "To be determined"
    
    print("\n5. Industry/Use — What is this for?")
    industry = input("   > ").strip() or "To be determined"
    
    brief_content = f"""# Brief: {design_name}

## References
- Likes: {references}
- Avoid: {avoid}

## Colors
- Brand/Preferred: {colors}
- Notes: 

## Mood
- Keywords: {mood}

## Industry/Use
{industry}

## Direction chosen
(TBD after swatch review)

---
*Brief gathered: automated*
"""
    
    brief_path = os.path.join(path, "BRIEF.md")
    with open(brief_path, "w") as f:
        f.write(brief_content)
    
    print(f"\n→ Brief saved to {brief_path}")
    print("\nNext: python render.py --create {design_name} --brief")
    
    return path

def render(design_name=None, dpi=150):
    if not design_name:
        designs = list_designs()
        if not designs:
            print("No designs found. Create one with: python render.py --create my-design")
            sys.exit(1)
        design_name = max(designs, key=lambda d: os.path.getmtime(os.path.join(DESIGNS_DIR, d)))
        print(f"Using design: {design_name}")
    
    design_path = get_design_path(design_name)
    canvas_path = os.path.join(design_path, "canvas.svg")
    preview_path = os.path.join(design_path, "preview.png")
    
    if not os.path.exists(canvas_path):
        print(f"Error: Canvas file not found at {canvas_path}")
        return

    try:
        with open(canvas_path, 'r', encoding='utf-8') as f:
            svg_string = f.read()

        png_bytes = resvg_py.svg_to_bytes(svg_string)
        
        with open(preview_path, 'wb') as f:
            f.write(png_bytes)
        
        print(f"→ rendered to {preview_path} @ {dpi}dpi")
    except Exception as e:
        print(f"→ [WARN] Parse warning or error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Render SVG to PNG via resvg.")
    parser.add_argument("--check", action="store_true", help="Check rasterizer installation")
    parser.add_argument("--design", "-d", help="Design name (folder in vector-designs/)")
    parser.add_argument("--create", "-c", help="Create a new design with given name")
    parser.add_argument("--brief", "-b", action="store_true", help="Gather brief before creating")
    parser.add_argument("--list", "-l", action="store_true", help="List all designs")
    args = parser.parse_args()

    if args.check:
        print("resvg-py is installed and ready.")
        sys.exit(0)

    if args.list:
        designs = list_designs()
        if designs:
            print("Available designs:")
            for d in designs:
                print(f"  - {d}")
        else:
            print("No designs found. Create one with: python render.py --create my-design")
        sys.exit(0)

    if args.brief and args.create:
        create_brief(args.create)
        sys.exit(0)
    
    if args.brief:
        print("Error: --brief requires --create <name>")
        sys.exit(1)

    if args.create:
        create_design(args.create)
        sys.exit(0)

    render(args.design)

if __name__ == "__main__":
    main()