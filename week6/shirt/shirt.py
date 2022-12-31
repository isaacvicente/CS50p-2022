from PIL import Image, ImageOps
import sys
import os

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]

# Get the file extension from both input and output files
# (splitext returns a list, and we want the second element from it, i.e. the file extension)
input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid input")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

size = shirt.size

img = ImageOps.fit(img, size)

img.paste(shirt, shirt)

img.save(sys.argv[2])
