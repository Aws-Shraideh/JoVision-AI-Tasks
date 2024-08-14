from PIL import Image
import pytesseract
import sys


def extract_text_from_image(imageName):
    image = Image.open(imageName)
    text = pytesseract.image_to_string(image)
    if text:
        return text
    else:
        return "No text found"


print(extract_text_from_image(sys.argv[1]))
