import sys
sys.path.append("c:\\work\\PLangVim")

import pytesseract
import os
import cv2
# import easyocr
import numpy as np
import random
from PIL import Image
import PY_PKG.SU_DirFile_MO as SD

# 결과 파일 저장(확인용)
saveFile = "c:\\work\\PLangVim\\ALL_FILE\\DV_PROCUREMENT\\IMG\\res.txt"

# 파일명은 가능하면 영문명
imgPath = "c:\\work\\PLangVim\\ALL_FILE\\DV_PROCUREMENT\\IMG\\test.jpg"

# 테서엑트 실행 파일 지정
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

config = ('-l kor --oem 1 --psm 4')

# 이미지를 그레이 스케일로 읽어 온다.
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# threshold 지정
ret, thresh_cv = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 아래는 블러링 효과(필요한지는 이미지마다 다름)
# thresh_cv = cv2.GaussianBlur(img, (3,3), 0)

# 한글 파일로 저장
subtext = pytesseract.image_to_string(thresh_cv, config=config)
SD.SU_MO_StrToText(subtext, saveFile)
print(subtext)