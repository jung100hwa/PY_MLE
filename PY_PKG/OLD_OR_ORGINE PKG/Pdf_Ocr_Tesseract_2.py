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
import SU_DirFile_MO as SD


saveFile = 'c:\\work\\PLangVim\\Procurement\\RESULT\\res.txt'

# 가능하면 파일명은 영문으로 하는게 낫다.
imgPath = "c:\\work\\PLangVim\\Procurement\\IMG\\test.jpeg"

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

# oem, psm 아래 사이트 참조
# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=johnsmithbrainseven&logNo=222242853850&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# oem은 1,3 둘중 하나만 적용, 경우에 따라 다르겠지만 1이 조금 낫다. psm은 4로 고정, 그리고 한글만 할 거면 "kor"만 하자
config = ('-l kor --oem 1 --psm 4')
# config = ('-l kor+eng --oem 1 --psm 4') 

# 이미지를 그레이 스케일로 읽어 온다.
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# 흑과백으로 되어 있는 바이너리 이미지로 만든다. 이때 경계값은 오츠의 알고리즘에서 나오는 경계값을 사용(선택1)
# 오츠의 알고리즘을 쓸때 두번째 인자(-1, 경계값)는 무시된다. 오츠알고리즘에서 알아서 선택 해준다.
ret, thresh_cv = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 흑과백으로 되어 있는 바이너리 이미지로 만든다. 경계값은 127로(선택2)
# ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 스레시 홀드 방법(조명이 일정치 않거나 배경색이 한종이에 틀릴때 적용)(선택3)
# blk_size = 9        # 블럭 사이즈
# C = 5               # 차감 상수
# thresh_cv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

subtext = pytesseract.image_to_string(thresh_cv, config=config)
SD.SU_MO_StrToText(subtext, saveFile)
print(subtext)