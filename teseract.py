from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd= r"D:\ocr_tes_lang\Tesseract-OCR\tesseract.exe"


#img=Image.open('speed_2.PNG')

custom_config = r'--oem 3 --psm 6'

image=cv2.imread('vikas_1_1.jpg')
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray= cv2.medianBlur(gray, 3)
text=pytesseract.image_to_string(gray)
print(text)
cv2.imshow('snap',gray)




#print(text)
#print(text[0],text[1],text[2],text[3],text[4],text[5],text[6],text[7],text[8],text[9],text[11],text[12],text[18])

