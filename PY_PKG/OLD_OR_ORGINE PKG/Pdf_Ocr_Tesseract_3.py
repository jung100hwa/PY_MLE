
import pytesseract
import os
import cv2
import easyocr
import numpy as np
import random
from PIL import Image
import SU_DirFile_MO as SD

# 결과 파일 저장(확인용)
saveFile = 'c:\\work\\PLangVim\\Procurement\\RESULT\\res.txt'

# 파일명은 가능하면 영문명
imgPath = "c:\\work\\PLangVim\\Procurement\\IMG\\test.jpeg"

# 테서엑트 실행 파일 지정
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

config = ('-l kor --oem 1 --psm 4')

# 이미지를 그레이 스케일로 읽어 온다.
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# threshold 지정
ret, thresh_cv = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

subtext = pytesseract.image_to_string(thresh_cv, config=config)
SD.SU_MO_StrToText(subtext, saveFile)
print(subtext)