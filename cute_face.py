from PIL import Image, ImageDraw

# Create blank image
img = Image.new('RGB', (300, 300), color='white')
draw = ImageDraw.Draw(img)

# Draw face
draw.ellipse((50, 50, 250, 250), fill='lightpink')

# Eyes
draw.ellipse((90, 100, 120, 130), fill='black')
draw.ellipse((180, 100, 210, 130), fill='black')

# Smile
draw.arc((100, 140, 200, 220), start=0, end=180, fill='black', width=3)

# Save image
img.save('cute_face.png')

img.show()