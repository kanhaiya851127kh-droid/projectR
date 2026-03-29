from PIL import Image, ImageDraw

# Canvas
W, H = 400, 400
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Center
cx, cy = W//2, H//2

# Face
r = 120
draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill="white", outline="black", width=3)

# Ears
ear_r = 35
draw.ellipse((cx-70-ear_r, cy-120-ear_r, cx-70+ear_r, cy-120+ear_r), fill="black")
draw.ellipse((cx+70-ear_r, cy-120-ear_r, cx+70+ear_r, cy-120+ear_r), fill="black")

# Eye patches
draw.ellipse((cx-60, cy-30, cx-20, cy+20), fill="black")
draw.ellipse((cx+20, cy-30, cx+60, cy+20), fill="black")

# Eyes
draw.ellipse((cx-50, cy-20, cx-30, cy), fill="white")
draw.ellipse((cx+30, cy-20, cx+50, cy), fill="white")

# Pupils
draw.ellipse((cx-45, cy-15, cx-38, cy-8), fill="black")
draw.ellipse((cx+35, cy-15, cx+42, cy-8), fill="black")

# Nose
draw.ellipse((cx-10, cy+10, cx+10, cy+25), fill="black")

# Mouth (cute)
draw.arc((cx-30, cy+20, cx, cy+50), 200, 340, fill="black", width=2)
draw.arc((cx, cy+20, cx+30, cy+50), 200, 340, fill="black", width=2)

# Blush
draw.ellipse((cx-90, cy+10, cx-60, cy+40), fill="#ffb6c1")
draw.ellipse((cx+60, cy+10, cx+90, cy+40), fill="#ffb6c1")

# Show
img.show()