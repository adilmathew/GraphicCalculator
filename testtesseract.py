import pytesseract
from PIL import Image,ImageDraw
import PIL
from PIL import ImageGrab
img_cv = Image.open("adil.png")
img_rgb = img_cv.convert("RGB")
img_rgb=img_rgb.resize((40,40),PIL.Image.ANTIALIAS)
img_rgb.save("adil.png")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(img_rgb, config=
" --psm 10"
" -l osd"
" "
                                          ))
                                             

