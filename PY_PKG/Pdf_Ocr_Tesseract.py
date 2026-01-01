# 1. https://github.com/UB-Mannheim/tesseract/wiki 에서 tesseract 다운로드
# 2. 이미지 처리를 위해 pillow 모듈을 설치 pip install pillow
# 3. pytesseract 모듈설치 pip install pytesseract
# 4. 한글을 추출하기 위해 https://github.com/tesseract-ocr/tessdata/ 이사이트에서 kor.traineddata 받아서 c:\Program Files\Tesseract-OCR\tessdata\ 여기에 복사
#  기본적으로 tesseract를 세팅하면 있는데 여기서 받아서 세팅해야 제대로 나옴. 사이즈도 훨씬 크다.
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
imPath = r'c:\work\PLangVim\test.jpeg'
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

print("============> 디폴트 처리 \n")
subtext = pytesseract.image_to_string(Image.open(imPath), lang='kor')
# SD.SU_MO_StrToText(subtext, saveFile+"디폴트 처리.txt")
print(subtext)

#
# config = ('-l kor --oem 3 --psm 4')
# config2 = ('-l kor+eng --oem 3 --psm 4')    # 이건 아닌듯 특히나 한글로만 되어 있는 문서에는
#
#
# print("============> openCV 기본\n")
# img = cv2.imread(imPath, cv2.IMREAD_COLOR)
# subtext = pytesseract.image_to_string(img, config=config2)
# SD.SU_MO_StrToText(subtext, saveFile+"openCV기본.txt")
# print(subtext)
#
# print("============> openCV 그레이처리후\n")
# img_gray = cv2.imread(imPath, cv2.IMREAD_GRAYSCALE)
# subtext = pytesseract.image_to_string(img_gray, config=config)
# SD.SU_MO_StrToText(subtext, saveFile+"openCV그레이.txt")
# print(subtext)
#
# # 제일정확하기 한데 왠놈의 시간이 이렇게 걸린데이
# print("============> easyOCR\n")
# reader = easyocr.Reader(['ko','en'], gpu=False) # need to run only once to load model into memory
# # subtext = reader.readtext(imPath)
# subtext = reader.readtext(imPath,detail=0)
# # SD.SU_MO_StrToText(subtext, saveFile+"easyOCR.txt")
# print(subtext)
#
# np.random.seed(42)
# COLORS = np.random.randint(0, 255, size=(255, 3),dtype=np.uint8)
# img = cv2.imread(imPath)
#
# for i in result :
#     x = i[0][0][0]
#     y = i[0][0][1]
#     w = i[0][1][0] - i[0][0][0]
#     h = i[0][2][1] - i[0][1][1]
#     color_idx = random.randint(0,255)
#     color = [int(c) for c in COLORS[color_idx]]
#     cv2.putText(img, str(i[1]), (int((x + x + w) / 2) , y-2), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
#     img = cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
#
# cv2.imshow("test",img)
# cv2.waitKey(0)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

