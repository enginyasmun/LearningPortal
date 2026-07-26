"""Generate the ten built-in academy portrait avatars.

Flat illustrated portraits, drawn at 4x and downsampled for smooth edges.
Run from the project root:  python tools/make_avatars.py
Output: avatars/realistic-male-01.png ... realistic-female-05.png
"""
from pathlib import Path

from PIL import Image, ImageDraw

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "avatars"
OUT.mkdir(parents=True, exist_ok=True)

S = 4                 # supersample factor
SIZE = 400            # final pixel size
D = SIZE * S          # drawing canvas


def lighten(color, amount):
    return tuple(min(255, int(c + (255 - c) * amount)) for c in color)


def darken(color, amount):
    return tuple(max(0, int(c * (1 - amount))) for c in color)


def radial_background(draw, top, bottom):
    """Soft radial gradient: light near the head, deeper at the rim."""
    steps = 90
    for i in range(steps, 0, -1):
        t = i / steps
        color = tuple(int(top[j] + (bottom[j] - top[j]) * (t ** 1.5)) for j in range(3))
        r = int(D * 0.78 * t)
        draw.ellipse([D // 2 - r, int(D * 0.42) - r, D // 2 + r, int(D * 0.42) + r], fill=color)


def draw_portrait(spec):
    img = Image.new("RGB", (D, D), spec["bg_bottom"])
    d = ImageDraw.Draw(img)
    radial_background(d, spec["bg_top"], spec["bg_bottom"])

    skin = spec["skin"]
    shadow = darken(skin, 0.12)
    hair = spec["hair"]
    cloth = spec["cloth"]
    cloth_dark = darken(cloth, 0.18)

    cx = D // 2

    # ---- shoulders / torso ----
    torso_top = int(D * 0.70)
    d.ellipse([int(D * 0.10), torso_top, int(D * 0.90), int(D * 1.42)], fill=cloth)
    # collar shading
    d.ellipse([int(D * 0.30), torso_top - int(D * 0.02), int(D * 0.70), torso_top + int(D * 0.18)],
              fill=cloth_dark)

    # ---- neck ----
    neck_w = int(D * 0.115)
    d.rounded_rectangle(
        [cx - neck_w, int(D * 0.575), cx + neck_w, int(D * 0.78)],
        radius=int(D * 0.05), fill=shadow,
    )

    # ---- ears ----
    ear_y = int(D * 0.44)
    ear_r = int(D * 0.045)
    for sx in (-1, 1):
        ex = cx + sx * int(D * 0.185)
        d.ellipse([ex - ear_r, ear_y - ear_r, ex + ear_r, ear_y + int(ear_r * 1.5)], fill=shadow)

    # ---- head ----
    head_l, head_r = int(D * 0.315), int(D * 0.685)
    head_t, head_b = int(D * 0.215), int(D * 0.655)
    d.ellipse([head_l, head_t, head_r, head_b], fill=skin)

    # ---- hair ----
    style = spec["hair_style"]
    if style == "short":
        d.ellipse([head_l - int(D * 0.012), head_t - int(D * 0.045),
                   head_r + int(D * 0.012), head_t + int(D * 0.27)], fill=hair)
        d.ellipse([head_l + int(D * 0.028), head_t + int(D * 0.10),
                   head_r - int(D * 0.028), head_t + int(D * 0.35)], fill=skin)
    elif style == "buzz":
        d.ellipse([head_l - int(D * 0.004), head_t - int(D * 0.016),
                   head_r + int(D * 0.004), head_t + int(D * 0.235)], fill=hair)
        d.ellipse([head_l + int(D * 0.014), head_t + int(D * 0.052),
                   head_r - int(D * 0.014), head_t + int(D * 0.30)], fill=skin)
        # sideburns down past the temples
        for sx in (-1, 1):
            ex = cx + sx * int(D * 0.168)
            d.ellipse([ex - int(D * 0.026), head_t + int(D * 0.10),
                       ex + int(D * 0.026), head_t + int(D * 0.20)], fill=hair)
    elif style == "sidepart":
        d.ellipse([head_l - int(D * 0.015), head_t - int(D * 0.05),
                   head_r + int(D * 0.015), head_t + int(D * 0.26)], fill=hair)
        d.ellipse([head_l + int(D * 0.075), head_t + int(D * 0.075),
                   head_r + int(D * 0.02), head_t + int(D * 0.33)], fill=skin)
    elif style == "wavy_long":
        d.ellipse([head_l - int(D * 0.055), head_t - int(D * 0.05),
                   head_r + int(D * 0.055), int(D * 0.86)], fill=hair)
        d.ellipse([head_l + int(D * 0.012), head_t + int(D * 0.05),
                   head_r - int(D * 0.012), head_b + int(D * 0.02)], fill=skin)
        d.ellipse([head_l + int(D * 0.03), head_t - int(D * 0.02),
                   head_r - int(D * 0.03), head_t + int(D * 0.20)], fill=hair)
    elif style == "afro":
        r = int(D * 0.235)
        d.ellipse([cx - r, head_t - int(D * 0.115), cx + r, head_t + int(D * 0.33)], fill=hair)
        d.ellipse([head_l + int(D * 0.022), head_t + int(D * 0.055),
                   head_r - int(D * 0.022), head_b], fill=skin)
    elif style == "bun":
        br = int(D * 0.075)
        d.ellipse([cx - br, head_t - int(D * 0.135), cx + br, head_t + int(D * 0.015)], fill=hair)
        d.ellipse([head_l - int(D * 0.015), head_t - int(D * 0.045),
                   head_r + int(D * 0.015), head_t + int(D * 0.24)], fill=hair)
        d.ellipse([head_l + int(D * 0.032), head_t + int(D * 0.085),
                   head_r - int(D * 0.032), head_t + int(D * 0.33)], fill=skin)
    elif style == "shoulder":
        d.ellipse([head_l - int(D * 0.048), head_t - int(D * 0.042),
                   head_r + int(D * 0.048), int(D * 0.775)], fill=hair)
        d.ellipse([head_l + int(D * 0.015), head_t + int(D * 0.058),
                   head_r - int(D * 0.015), head_b + int(D * 0.01)], fill=skin)
        d.ellipse([head_l + int(D * 0.035), head_t - int(D * 0.015),
                   head_r - int(D * 0.035), head_t + int(D * 0.185)], fill=hair)

    # ---- beard ----
    if spec.get("beard"):
        beard = spec.get("beard_color", darken(hair, 0.08))
        d.ellipse([head_l + int(D * 0.022), head_t + int(D * 0.175),
                   head_r - int(D * 0.022), head_b + int(D * 0.022)], fill=beard)
        d.ellipse([head_l + int(D * 0.052), head_t + int(D * 0.135),
                   head_r - int(D * 0.052), head_b - int(D * 0.062)], fill=skin)

    # ---- shadow under the jaw for depth ----
    d.ellipse([head_l + int(D * 0.055), head_b - int(D * 0.075),
               head_r - int(D * 0.055), head_b + int(D * 0.055)], fill=darken(skin, 0.07))
    d.ellipse([head_l + int(D * 0.012), head_t + int(D * 0.055),
               head_r - int(D * 0.012), head_b - int(D * 0.012)], fill=skin)

    # ---- cheek blush ----
    blush = lighten(spec.get("blush", (214, 122, 110)), 0.35)
    for sx in (-1, 1):
        bxc = cx + sx * int(D * 0.108)
        d.ellipse([bxc - int(D * 0.040), int(D * 0.505) - int(D * 0.022),
                   bxc + int(D * 0.040), int(D * 0.505) + int(D * 0.022)],
                  fill=tuple(int(skin[i] * 0.78 + blush[i] * 0.22) for i in range(3)))

    # ---- eyebrows ----
    brow = darken(hair, 0.25)
    brow_y = int(D * 0.415)
    for sx in (-1, 1):
        ex = cx + sx * int(D * 0.077)
        d.rounded_rectangle(
            [ex - int(D * 0.042), brow_y - int(D * 0.011),
             ex + int(D * 0.042), brow_y + int(D * 0.011)],
            radius=int(D * 0.011), fill=brow,
        )

    # ---- eyes ----
    eye_y = int(D * 0.465)
    eye_rx, eye_ry = int(D * 0.029), int(D * 0.033)
    for sx in (-1, 1):
        ex = cx + sx * int(D * 0.077)
        d.ellipse([ex - eye_rx, eye_y - eye_ry, ex + eye_rx, eye_y + eye_ry], fill=(255, 255, 255))
        d.ellipse([ex - int(D * 0.016), eye_y - int(D * 0.016),
                   ex + int(D * 0.016), eye_y + int(D * 0.016)], fill=spec["eye"])
        d.ellipse([ex - int(D * 0.006) + int(D * 0.005), eye_y - int(D * 0.009),
                   ex + int(D * 0.003) + int(D * 0.005), eye_y - int(D * 0.001)], fill=(255, 255, 255))

    # ---- nose ----
    d.line([(cx, int(D * 0.495)), (cx, int(D * 0.535))], fill=shadow, width=int(D * 0.011))

    # ---- mouth (gentle smile) ----
    d.arc([cx - int(D * 0.052), int(D * 0.525), cx + int(D * 0.052), int(D * 0.595)],
          start=15, end=165, fill=darken(skin, 0.42), width=int(D * 0.014))

    # ---- glasses ----
    if spec.get("glasses"):
        g = spec.get("glass_color", (55, 58, 62))
        w = int(D * 0.010)
        for sx in (-1, 1):
            ex = cx + sx * int(D * 0.077)
            d.ellipse([ex - int(D * 0.052), eye_y - int(D * 0.050),
                       ex + int(D * 0.052), eye_y + int(D * 0.050)], outline=g, width=w)
        d.line([(cx - int(D * 0.025), eye_y), (cx + int(D * 0.025), eye_y)], fill=g, width=w)
        d.line([(cx - int(D * 0.129), eye_y - int(D * 0.006)),
                (head_l - int(D * 0.004), eye_y - int(D * 0.020))], fill=g, width=w)
        d.line([(cx + int(D * 0.129), eye_y - int(D * 0.006)),
                (head_r + int(D * 0.004), eye_y - int(D * 0.020))], fill=g, width=w)

    # ---- mask to a circle with transparency ----
    img = img.resize((SIZE, SIZE), Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", (D, D), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, D - 1, D - 1], fill=255)
    img.putalpha(mask.resize((SIZE, SIZE), Image.LANCZOS))
    return img


PORTRAITS = [
    # ---------------- male ----------------
    dict(name="realistic-male-01", skin=(226, 178, 140), hair=(64, 42, 30), eye=(74, 52, 38),
         cloth=(38, 58, 96), bg_top=(214, 231, 244), bg_bottom=(176, 205, 231),
         hair_style="short", glasses=True),
    dict(name="realistic-male-02", skin=(126, 82, 54), hair=(28, 22, 20), eye=(46, 32, 26),
         cloth=(16, 122, 116), bg_top=(207, 240, 236), bg_bottom=(166, 216, 212),
         hair_style="buzz"),
    dict(name="realistic-male-03", skin=(241, 205, 175), hair=(138, 96, 56), eye=(96, 118, 92),
         cloth=(92, 98, 108), bg_top=(236, 233, 226), bg_bottom=(210, 206, 197),
         hair_style="sidepart", beard=True, beard_color=(120, 84, 50)),
    dict(name="realistic-male-04", skin=(198, 148, 108), hair=(32, 26, 24), eye=(58, 40, 30),
         cloth=(128, 44, 58), bg_top=(246, 224, 226), bg_bottom=(226, 191, 195),
         hair_style="short"),
    dict(name="realistic-male-05", skin=(246, 218, 192), hair=(196, 158, 92), eye=(84, 122, 148),
         cloth=(30, 104, 72), bg_top=(216, 240, 226), bg_bottom=(182, 218, 199),
         hair_style="sidepart", glasses=True, glass_color=(140, 106, 60)),
    # ---------------- female ----------------
    dict(name="realistic-female-01", skin=(228, 182, 146), hair=(62, 40, 30), eye=(72, 50, 36),
         cloth=(118, 56, 118), bg_top=(240, 226, 244), bg_bottom=(215, 195, 228),
         hair_style="wavy_long"),
    dict(name="realistic-female-02", skin=(120, 78, 52), hair=(26, 20, 18), eye=(44, 30, 24),
         cloth=(196, 142, 34), bg_top=(250, 236, 208), bg_bottom=(234, 210, 168),
         hair_style="afro"),
    dict(name="realistic-female-03", skin=(247, 220, 196), hair=(208, 172, 108), eye=(88, 126, 152),
         cloth=(36, 96, 158), bg_top=(216, 232, 248), bg_bottom=(184, 209, 235),
         hair_style="shoulder"),
    dict(name="realistic-female-04", skin=(202, 152, 112), hair=(34, 28, 26), eye=(60, 42, 32),
         cloth=(18, 118, 112), bg_top=(210, 238, 234), bg_bottom=(172, 214, 210),
         hair_style="bun"),
    dict(name="realistic-female-05", skin=(243, 208, 182), hair=(150, 74, 42), eye=(94, 120, 90),
         cloth=(34, 88, 62), bg_top=(226, 240, 230), bg_bottom=(196, 220, 203),
         hair_style="shoulder", glasses=True),
]

if __name__ == "__main__":
    for spec in PORTRAITS:
        path = OUT / f"{spec['name']}.png"
        draw_portrait(spec).save(path, "PNG", optimize=True)
        print(f"  wrote {path.name}  ({path.stat().st_size // 1024} KB)")
    print(f"\n{len(PORTRAITS)} portraits written to {OUT}")
