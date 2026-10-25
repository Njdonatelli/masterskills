import os
import sys
import xml.etree.ElementTree as ET
import argparse
import re

DESIGNS_DIR = "vector-designs"

def get_design_path(design_name):
    return os.path.join(DESIGNS_DIR, design_name)

def list_designs():
    if not os.path.exists(DESIGNS_DIR):
        return []
    return [d for d in os.listdir(DESIGNS_DIR) if os.path.isdir(os.path.join(DESIGNS_DIR, d))]

def hex_to_rgb(hex_color):
    hex_color = hex_color.strip().lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    elif len(hex_color) == 3:
        return tuple(int(c*2, 16) for c in hex_color)
    return (0, 0, 0)

def get_luminance(rgb):
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

def get_all_colors(svg_content):
    colors = set()
    fill_matches = re.findall(r'fill="([^"]+)"', svg_content)
    stroke_matches = re.findall(r'stroke="([^"]+)"', svg_content)
    stop_color_matches = re.findall(r'stop-color="([^"]+)"', svg_content)
    
    for color in fill_matches + stroke_matches + stop_color_matches:
        if color.startswith('#') and len(color) in [4, 7]:
            colors.add(color)
        elif color.startswith('rgb'):
            colors.add(color)
        elif color.isdigit() and int(color) < 256:
            pass
    return colors

def check_gradient_usage(svg_content):
    has_gradients = '<linearGradient' in svg_content or '<radialGradient' in svg_content
    return has_gradients

def critique_svg(filepath):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return 0

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        tree = ET.parse(filepath)
        root = tree.getroot()
    except Exception as e:
        print(f"[FAIL] Could not parse SVG: {e}")
        return 0

    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    score = 100
    checks = []

    # === ANTI-SLOP CHECKS (Premium Guidance) ===
    
    # Check 1: Purple-to-blue gradient (AI signature)
    ai_purple_patterns = ['#6366f1', '#8b5cf6', '#a855f7', '#a78bfa', '#7c3aed']
    has_ai_purple = any(c.lower() in svg_content.lower() for c in ai_purple_patterns)
    if has_ai_purple:
        checks.append("[FAIL] color — purple tones are AI generic. Use brand-specific colors.")
        score -= 20
    
    # Check 2: Generic gradient usage
    if '<linearGradient' in svg_content or '<radialGradient' in svg_content:
        checks.append("[WARN] gradient — gradients often signal AI. Solid colors feel more premium.")
        score -= 10
    
    # Check 3: All rounded rectangles (AI modern look)
    rounded_rects = root.findall('.//svg:rect', ns)
    rounded_count = sum(1 for r in rounded_rects if r.get('rx') or r.get('ry'))
    if len(rounded_rects) > 0 and rounded_count == len(rounded_rects):
        checks.append("[FAIL] shape — fully rounded = AI generic. Mix in sharp corners for premium.")
        score -= 15
    
    # Check 4: Inter font
    if 'font-family="Inter"' in svg_content or "font-family='Inter'" in svg_content:
        checks.append("[FAIL] font — Inter is AI default. Use Helvetica, Arial, or brand font.")
        score -= 15
    
    # Check 5: Template text patterns
    template_texts = ['WELCOME', 'GET STARTED', 'LEARN MORE', 'READ MORE', 'CLICK HERE']
    has_template = any(t.lower() in svg_content.lower() for t in template_texts)
    if has_template:
        checks.append("[FAIL] text — generic template text. Use brand-specific copy.")
        score -= 15
    
    # Check 6: Excessive centered text
    centered_count = 0
    for text in root.findall('.//svg:text', ns):
        if text.get('text-anchor') == 'middle':
            centered_count += 1
    if centered_count > 3:
        checks.append("[WARN] layout — too much centered text. Use asymmetry for premium.")
        score -= 10
    
    # Check 7: Too many colors (>5)
    colors = get_all_colors(svg_content)
    if len(colors) > 5:
        checks.append(f"[FAIL] color — {len(colors)} colors (max 5). Premium = restrained.")
        score -= 15
    elif len(colors) <= 5:
        checks.append(f"[PASS] color economy — {len(colors)} colors (restrained)")
    
    # === STRUCTURE CHECKS ===
    
    missing_ids = 0
    for el in root.findall('.//svg:text', ns) + root.findall('./svg:g', ns):
        if 'id' not in el.attrib:
            missing_ids += 1
    
    if missing_ids > 0:
        checks.append(f"[WARN] IDs — {missing_ids} elements missing 'id' (harder to maintain)")
        score -= min(15, missing_ids * 2)
    else:
        checks.append("[PASS] IDs — all elements labeled")
    
    empty_groups = len([g for g in root.findall('.//svg:g', ns) if len(g) == 0])
    if empty_groups > 0:
        checks.append(f"[WARN] empty groups — {empty_groups} unused <g> elements")
        score -= empty_groups * 2
    else:
        checks.append("[PASS] no empty groups")
    
    if 'viewBox' not in root.attrib:
        checks.append("[FAIL] viewBox missing — layout will break on render")
        score -= 20
    else:
        checks.append("[PASS] viewBox present")
    
    # === COMPOSITION CHECKS ===
    
    shape_count = (
        len(root.findall('.//svg:rect', ns)) +
        len(root.findall('.//svg:circle', ns)) +
        len(root.findall('.//svg:ellipse', ns)) +
        len(root.findall('.//svg:polygon', ns)) +
        len(root.findall('.//svg:path', ns))
    )
    
    if shape_count > 12:
        checks.append(f"[FAIL] complexity — {shape_count} shapes (too many). Premium = simple.")
        score -= 15
    elif shape_count < 2 and len(colors) < 2:
        checks.append("[WARN] composition — too simple. Add more intentional elements.")
        score -= 5
    else:
        checks.append(f"[PASS] composition — {shape_count} shapes (good balance)")
    
    # Typography hierarchy
    text_elements = root.findall('.//svg:text', ns)
    font_sizes = [float(t.get('font-size', '0')) for t in text_elements if t.get('font-size')]
    if len(set(font_sizes)) >= 2:
        checks.append("[PASS] typography hierarchy — size contrast present")
    elif len(font_sizes) == 1 and font_sizes[0] > 0:
        checks.append("[PASS] typography — clean single-size")


    print("\n" + "="*50)
    print("CRITIQUE REPORT")
    print("="*50)
    for check in checks:
        print(check)
    
    final_score = max(0, score)
    print("\n" + "="*50)
    if final_score >= 90:
        print(f"→ score: {final_score}/100 [EXCELLENT]")
    elif final_score >= 75:
        print(f"→ score: {final_score}/100 [GOOD]")
    elif final_score >= 60:
        print(f"→ score: {final_score}/100 [NEEDS WORK]")
    else:
        print(f"→ score: {final_score}/100 [REVISIONS NEEDED]")
    print("="*50)
    
    return final_score

def main():
    parser = argparse.ArgumentParser(description="Critique SVG design (enhanced anti-slop)")
    parser.add_argument("--design", "-d", help="Design name (folder in vector-designs/)")
    parser.add_argument("--list", "-l", action="store_true", help="List all designs")
    args = parser.parse_args()

    if args.list:
        designs = list_designs()
        if designs:
            print("Available designs:")
            for d in designs:
                print(f"  - {d}")
        else:
            print("No designs found.")
        sys.exit(0)

    if args.design:
        design_path = get_design_path(args.design)
    else:
        designs = list_designs()
        if not designs:
            print("No designs found. Use --design to specify one.")
            sys.exit(1)
        design_name = max(designs, key=lambda d: os.path.getmtime(os.path.join(DESIGNS_DIR, d)))
        design_path = get_design_path(design_name)
        print(f"Critiquing design: {design_name}")

    canvas_path = os.path.join(design_path, "canvas.svg")
    critique_svg(canvas_path)

if __name__ == "__main__":
    main()