"""Generate entry.png: a newspaper front page summing up 20 Nov 2026 world news.

Run locally (needs Pillow + DejaVu fonts). The submitted program main.py only
copies the committed entry.png to /output/entry.png (stdlib only in sandbox).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
INK = (22, 22, 22)
RED = (163, 22, 33)
BLUE = (31, 58, 95)
GREY = (110, 108, 100)
RULE = (60, 58, 52)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(draw, x, y, text, fnt, width, leading, color=INK):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer frame ----
d.rectangle([14, 14, W - 15, H - 15], outline=RULE, width=3)
d.rectangle([22, 22, W - 23, H - 23], outline=RULE, width=1)

# ---- masthead ----
d.text((512, 38), "THE WORLD", font=font(SERIF_B, 96), fill=INK, anchor="ma")
d.text((512, 148), "IN ONE PAGE", font=font(SANS_B, 30), fill=RED, anchor="ma")
d.line([60, 196, 964, 196], fill=RULE, width=3)
d.text((512, 206), "FRIDAY, 20 NOVEMBER 2026  \u2022  THE DAY'S WORLD NEWS, SUMMED UP",
       font=font(SANS_B, 20), fill=INK, anchor="ma")
d.line([60, 240, 964, 240], fill=RULE, width=2)

# ---- lead story ----
y = 258
d.text((60, y), "DIPLOMACY  \u2022  SHENZHEN, CHINA", font=font(SANS_B, 19), fill=RED)
y += 30
d.text((60, y), "Three leaders, one", font=font(SERIF_B, 48), fill=INK)
y += 54
d.text((60, y), "declaration of peace", font=font(SERIF_B, 48), fill=INK)
y += 60
lead = ("Donald Trump, Vladimir Putin and Xi Jinping held the first-ever "
        "three-way summit of the US, Russian and Chinese leaders, on the "
        "sidelines of APEC in Shenzhen. They signed a joint \u201cDeclaration "
        "towards Peace\u201d, reaffirming that \u201ca nuclear war cannot be won "
        "and must never be fought\u201d. It made no mention of Ukraine.")
y = para(d, 60, y, lead, font(SERIF, 20), 600, 27)
lead_end = y

# flags panel, right of lead text
fx, fy, fw, fh = 700, 258, 264, 218
d.rectangle([fx, fy, fx + fw, fy + fh], outline=RULE, width=2)
ux, uy, uw, uh = fx + 14, fy + 14, 76, 52
for i in range(7):
    d.rectangle([ux, uy + i * uh // 7, ux + uw, uy + (i + 1) * uh // 7],
                fill=RED if i % 2 == 0 else PAPER)
d.rectangle([ux, uy, ux + uw * 2 // 5, uy + uh * 4 // 7], fill=BLUE)
for r in range(3):
    for c in range(4):
        d.ellipse([ux + 6 + c * 13, uy + 5 + r * 10, ux + 11 + c * 13, uy + 10 + r * 10],
                  fill=(255, 255, 255))
cx, cy, cw, ch = fx + 14, fy + 82, 76, 52
d.rectangle([cx, cy, cx + cw, cy + ch], fill=RED)
d.polygon([(cx + 12, cy + 8), (cx + 16, cy + 18), (cx + 26, cy + 18),
           (cx + 18, cy + 24), (cx + 21, cy + 34), (cx + 12, cy + 28),
           (cx + 3, cy + 34), (cx + 6, cy + 24), (cx - 2, cy + 18),
           (cx + 8, cy + 18)], fill=(255, 222, 0))
rx, ry, rw, rh = fx + 14, fy + 150, 76, 52
d.rectangle([rx, ry, rx + rw, ry + rh // 3], fill=(255, 255, 255))
d.rectangle([rx, ry + rh // 3, rx + rw, ry + 2 * rh // 3], fill=(0, 57, 166))
d.rectangle([rx, ry + 2 * rh // 3, rx + rw, ry + rh], fill=(213, 0, 50))
d.text((fx + 104, fy + 22), "USA", font=font(SANS_B, 18), fill=INK)
d.text((fx + 104, fy + 96), "CHINA", font=font(SANS_B, 18), fill=INK)
d.text((fx + 104, fy + 168), "RUSSIA", font=font(SANS_B, 18), fill=INK)
d.text((fx + 104, fy + 44), "Trump", font=font(SANS, 16), fill=GREY)
d.text((fx + 104, fy + 118), "Xi Jinping", font=font(SANS, 16), fill=GREY)
d.text((fx + 104, fy + 190), "Putin", font=font(SANS, 16), fill=GREY)

div1 = lead_end + 12
d.line([60, div1, 964, div1], fill=RULE, width=2)

# ---- 2x2 grid ----
def story(x, y, w, kicker, head, body):
    d.text((x, y), kicker, font=font(SANS_B, 17), fill=RED)
    yy = y + 26
    for line in wrap(d, head, font(SERIF_B, 25), w):
        d.text((x, yy), line, font=font(SERIF_B, 25), fill=INK)
        yy += 31
    yy += 4
    return para(d, x, yy, body, font(SERIF, 18), w, 24)

gx = 60
gw = 442
gy = div1 + 16
story(gx, gy, gw, "TECHNOLOGY  \u2022  NEW YORK",
      "Anthropic's record debut",
      "AI firm Anthropic began trading on the Nasdaq in a record IPO, valued "
      "at close to $2 trillion \u2014 the biggest market debut yet.")
story(gx + gw + 20, gy, gw, "WAR  \u2022  UKRAINE",
      "Crimea bridge hit again",
      "Putin vowed a forceful reply after Ukraine hit the Crimea bridge a "
      "third time this week. Zelensky urged allies to cut trade with Russia.")
mid = gy + 158
d.line([60, mid, 964, mid], fill=RULE, width=1)
gy2 = mid + 12
story(gx, gy2, gw, "CLIMATE  \u2022  ANTALYA, T\u00dcRKIYE",
      "COP31 closes its doors",
      "The UN climate talks wrap up in Antalya, as the IEA warns data-centre "
      "emissions could rise 70% in four years on AI power demand.")
story(gx + gw + 20, gy2, gw, "WEATHER  \u2022  INDIA",
      "Cyclone Akvan makes landfall",
      "Cyclonic storm Akvan came ashore on India's east coast, hitting the "
      "Andhra Pradesh\u2013Odisha shoreline with heavy rain and wind.")
grid_end = gy2 + 158
d.line([512, div1 + 16, 512, grid_end], fill=RULE, width=1)
d.line([60, grid_end + 8, 964, grid_end + 8], fill=RULE, width=2)

# ---- also today strip ----
sy = grid_end + 20
d.text((60, sy), "ALSO TODAY", font=font(SANS_B, 17), fill=RED)
briefs = ("F1: Las Vegas GP qualifying  \u2022  US and Venezuela restore "
          "military ties  \u2022  World Children's Day  \u2022  NZ pay-equity ruling")
d.text((60, sy + 26), briefs, font=font(SANS, 15), fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size, "lead_end", lead_end, "grid_end", grid_end)
