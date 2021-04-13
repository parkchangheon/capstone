from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\sean park\Desktop\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(Image.open("DL.jpg"),)

print(text)
