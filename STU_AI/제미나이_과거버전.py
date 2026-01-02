"""
제미나이를 이용해서 OCR 구현. 과거 TESSERACT 등을 이용했는데 이젠 옛말. 정말 무섭토록 정확하다.
todo 절차
1. https://aistudio.google.com/ 접근
2. 아무 프로젝트나 하나 생성 또는 Get API key 만들기
3. 키, 프로젝트, 생성일, 할당량 등급 이 있는데 반드시 todo 키를 선택하면 발급된 키가 나온다.
"""
import google.generativeai as genai
import PIL.Image
import time

start_time = time.perf_counter() # time.time()도 사용 가능
# API키 세팅
genai.configure(api_key="AIzaSyCwoWD6Mwulrb1dA2A4v7ARxTJDv1ag3es")

model = genai.GenerativeModel("gemini-2.5-flash")
img = PIL.Image.open("test_03.jpg")

response = model.generate_content(
    ["이 이미지에 있는 모든 텍스트를 정확하게 추출해줘.", img],
    generation_config=genai.types.GenerationConfig(temperature=0.0)
)

print(response.text)

end_time = time.perf_counter()

# 소요 시간 계산 및 출력
elapsed_time = end_time - start_time
print(f"소요 시간: {elapsed_time} 초")