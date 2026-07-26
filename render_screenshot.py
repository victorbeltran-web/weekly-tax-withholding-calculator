"""
Renders a plain-text terminal transcript as a PNG image styled like a
real terminal window (title bar with traffic-light buttons, dark background,
monospace font) so it can be used as a "screenshot" in the deliverable.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
]


def get_font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold \
        else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    return ImageFont.truetype(path, size)


def render(transcript_path, title, out_path):
    with open(transcript_path) as f:
        lines = f.read().rstrip("\n").split("\n")

    font_size = 16
    font = get_font(font_size)
    line_height = int(font_size * 1.5)
    pad_x = 24
    pad_top = 56  # room for title bar
    pad_bottom = 24

    # Determine width based on the longest line
    tmp_img = Image.new("RGB", (10, 10))
    tmp_draw = ImageDraw.Draw(tmp_img)
    max_width = 0
    for line in lines:
        bbox = tmp_draw.textbbox((0, 0), line, font=font)
        max_width = max(max_width, bbox[2] - bbox[0])

    width = max(max_width + pad_x * 2, 640)
    height = pad_top + pad_bottom + line_height * len(lines)

    bg_color = (30, 30, 30)
    title_bar_color = (45, 45, 45)
    text_color = (0, 230, 118)          # bright green terminal text
    prompt_color = (220, 220, 220)
    header_color = (86, 182, 255)
    error_color = (255, 99, 99)

    img = Image.new("RGB", (int(width), int(height)), bg_color)
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, width, pad_top - 8], fill=title_bar_color)
    for i, color in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        draw.ellipse([16 + i * 24, 16, 16 + i * 24 + 12, 28], fill=color)
    title_font = get_font(15, bold=True)
    draw.text((100, 14), title, font=title_font, fill=(200, 200, 200))

    y = pad_top
    for line in lines:
        if "Error" in line:
            color = error_color
        elif "====" in line or "WEEKLY TAX" in line or "SUMMARY" in line or "----" in line:
            color = header_color
        elif line.strip() == "":
            color = text_color
        else:
            color = text_color
        draw.text((pad_x, y), line, font=font, fill=color)
        y += line_height

    img.save(out_path)
    print(f"Saved {out_path} ({width}x{height})")


if __name__ == "__main__":
    render("transcript_sample_run.txt", "python3 tax_withholding.py — Sample Run", "screenshot_sample_run.png")
    render("transcript_boundary_run.txt", "python3 tax_withholding.py — Boundary & Validation Test", "screenshot_boundary_run.png")
