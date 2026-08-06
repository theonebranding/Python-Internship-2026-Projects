from PIL import Image, ImageDraw, ImageFont
import os

text = "Hello World"

image = Image.new("RGB", (500, 200), "white")
draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()

draw.text((20, 50), text, fill="blue", font=font)

output = os.path.join(os.path.dirname(__file__), "demo1.png")
image.save(output)

print("Saved at:", output)
print("Exists:", os.path.exists(output))
print("END")