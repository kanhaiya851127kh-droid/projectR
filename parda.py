from PIL import Image, ImageDraw, ImageFont
import math
import random

# -----------------------------
# SETTINGS
# -----------------------------
W, H = 1000, 900
BG = (245, 245, 210)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Font
try:
    font = ImageFont.truetype("arial.ttf", 14)
    small_font = ImageFont.truetype("arial.ttf", 12)
except:
    font = ImageFont.load_default()
    small_font = ImageFont.load_default()

text = "I Love You My Sweetheart "

random.seed(10)

# -----------------------------
# TOP TEXT
# -----------------------------
top_text = "I Love You My Sweetheart"

draw.text(
    (W // 2, 35),
    top_text,
    fill=(150, 55, 55),
    font=font,
    anchor="ma"
)

# -----------------------------
# CURTAIN / STRING EFFECT
# -----------------------------
center_x = W // 2

for i in range(55):

    # Starting position at top
    x = 245 + i * 9

    # Different string lengths
    length = random.randint(250, 600)

    # Curve amount
    curve = random.uniform(-100, 100)

    # Text color
    color = random.choice([
        (150, 55, 55),
        (175, 65, 65),
        (190, 80, 80),
        (130, 60, 60)
    ])

    # Create one long text string
    words = text * 20

    for j, char in enumerate(words):

        y = 75 + j * 8

        if y > 75 + length:
            break

        # Curve / hanging curtain
        progress = (y - 75) / length

        # Parabola-like hanging shape
        offset = curve * math.sin(progress * math.pi)

        # Slight wave
        wave = 8 * math.sin(progress * 12 + i)

        xx = x + offset + wave

        draw.text(
            (xx, y),
            char,
            fill=color,
            font=small_font
        )

# -----------------------------
# CENTER PINK HEART AREA
# -----------------------------
heart_x = center_x
heart_y = 600

for i in range(350):

    angle = random.uniform(0, 2 * math.pi)
    radius = random.uniform(5, 105)

    # Heart-like coordinates
    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    x = heart_x + x * radius / 16
    y = heart_y - y * radius / 16

    draw.text(
        (x, y),
        random.choice(["I", "Love", "You", "❤"]),
        fill=(210, random.randint(60, 120), random.randint(90, 130)),
        font=small_font
    )

# -----------------------------
# SAVE
# -----------------------------
#img.save("string_confession.png")

#print("Done! Image saved as string_confession.png")