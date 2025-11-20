from PIL import Image

img = Image.open("/home/vladyslav/photo_2025-11-18_17-19-03.jpg").convert("RGB")
img.save("output.pdf")
