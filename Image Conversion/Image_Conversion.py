from PIL import Image # Image Processing

import glob

print(glob.glob("*.png")) # Gives list of files with extension .png

# Based on Stack Overflow Answer: https://stackoverflow.com/a/43258974/5086355
for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert("RGB")
    rgb_im.save(file.replace("png", "jpg"), quality=95)
