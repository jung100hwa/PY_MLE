"""
제미나이를 이용해서 OCR 구현. 과거 TESSERACT 등을 이용했는데 이젠 옛말. 정말 무섭토록 정확하다.
todo 절차
1. https://aistudio.google.com/ 접근
2. 아무 프로젝트나 하나 생성 또는 Get API key 만들기
3. 키, 프로젝트, 생성일, 할당량 등급 이 있는데 반드시 todo 키를 선택하면 발급된 키가 나온다.
4. 현재 버전으로 업데이트

https://github.com/googleapis/python-genai 여기 사이트에 다양한 예제가 있으니 참고

"""

# 키 불러오기
import os
from dotenv import load_dotenv
load_dotenv()
genAI_KEY = os.getenv('genAI')

import PIL.Image
from google import genai
from google.genai import types

client = genai.Client(api_key=genAI_KEY)


############################################################# 1. 기본 사용법
# response = client.models.generate_content(
#     model='gemini-2.5-flash', # 모델 마다 비용이 지불이 필요하네. 요 버전으로...
#     contents=types.Part.from_text(text='이순신은 누구야?'),
#     config=types.GenerateContentConfig(
#         temperature=0,
#         top_p=0.95,
#         top_k=20,
#     ),
# )
# print(response.text)

############################################################# 2. 기본 사용법. type 대신에 아래 처럼 딕셔너리 형태로 가능
# response = client.models.generate_content(
#     model='gemini-2.5-flash',
#     contents={'text': '이순신은 누구입니까'},
#     config={
#         'temperature':0,
#         'top_p':0.95,
#         'top_k':20,
#     },
# )
# print(response.text)


############################################################# 3. 이미지 처리
def extract_text_from_image(image_path):
    img = PIL.Image.open(image_path)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            img,
            "이 이미지에 포함된 모든 텍스트를 있는 그대로 추출해줘. 표가 있다면 구조를 유지해줘."
        ]
    )

    return response.text

extracted_text = extract_text_from_image('test_03.jpg')
print(extracted_text)
