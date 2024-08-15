from PIL import Image
import pytesseract
import sys


def color_to_black(imageName):
    image = Image.open(imageName)
    imageSize = image.size
    length, height = imageSize[0], imageSize[1]
    if image.mode != "RGB":
        image.convert("RGB")
    greyScale = Image.new("L", (length, height))
    for x in range(length):
        for y in range(height):
            R, G, B = image.getpixel((x, y))
            gray = int(0.2989 * R + 0.5870 * G + 0.1140 * B)
            greyScale.putpixel((x, y), gray)
    greyScale.show()


print(color_to_black(sys.argv[1]))
