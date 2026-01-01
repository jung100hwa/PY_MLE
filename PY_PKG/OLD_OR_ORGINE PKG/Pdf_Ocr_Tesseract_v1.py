# 1. https://github.com/UB-Mannheim/tesseract/wiki 에서 tesseract 다운로드
# 2. 이미지 처리를 위해 pillow 모듈을 설치 pip install pillow
# 3. pytesseract 모듈설치 pip install pytesseract
# 4. 한글을 추출하기 위해 https://github.com/tesseract-ocr/tessdata/ 이사이트에서 kor.traineddata 받아서 c:\Program Files\Tesseract-OCR\tessdata\ 여기에 복사
#  기본적으로 tesseract를 세팅하면 있는데 여기서 받아서 세팅해야 제대로 나옴. 사이즈도 훨씬 크다. 가능하면 다른 언어도 여기서 받아온다. 
# 5. 이지미 추출의 확률을 위해 pip install opencv-python

import pytesseract
import os
import cv2
import easyocr
import numpy as np
import random
from PIL import Image
# import SU_DirFile_MO as SD


saveFile = 'c:\\work\\PLangVim\\Procurement\\RESULT\\'

# 과거 버전은 이미지 한글이름은 읽지 못하는 듯. 현재 tesseract 설치하니 한글파일명도 읽어냄
imgPath = r'c:\work\PLangVim\Procurement\IMG\test.jpeg'
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

config = ('-l kor --oem 3 --psm 4')
# config = ('-l kor+eng --oem 3 --psm 4')    # 이건 아닌듯 특히나 한글로만 되어 있는 문서에는

# 이미지를 그레이 스케일로 읽어 온다.
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# 흑과백으로 되어 있는 바이너리 이미지로 만든다. 이때 경계값은 오츠의 알고리즘에서 나오는 경계값을 사용
ret, thresh_cv = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 흑과백으로 되어 있는 바이너리 이미지로 만든다. 경계값은 127로
# ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 스레시 홀드 방법(조명이 일정치 않거나 배경색이 한종이에 틀릴때 적용)
blk_size = 9        # 블럭 사이즈
C = 5               # 차감 상수

thresh_cv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

subtext = pytesseract.image_to_string(thresh_cv, config=config)
print(subtext)