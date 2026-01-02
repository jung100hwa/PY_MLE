"""
1. chatGPT유료 계정과 openAI API계정과는 별개다. 각각 결제수단을 등록해야 한다.
2. https://platform.openai.com/docs/overview 이곳으로 들어가서 하면된다.
"""

import openai
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()
openAPI_KEY = os.getenv('openAPI')
client = openai.OpenAI(api_key=openAPI_KEY)


############################################################# 1. 가장 기초적인 활용
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role" : "system", "content" : "답변은 반말로 해줘"}, # 이 부분은 아래 답변에 대한 규칙이나 방향성을 알려주는 역할
        {"role" : "user","content" : "2020년 월드시리즈에서는 누가 우승했어?"}
    ]
)
print(completion.choices[0].message.content)


############################################################# 2. 역활과 함수를 활용
# def return_answer(input_text = ''):
#     system_prompt = """특정 문서가 입력되면 다음과 같은 형태로 문서를분석하십시오.
#     1.주어진 입력 문서에 대해서 반드시 주제:, 요약:, 가능한 질문: 이 세가지를순차적으로작성해야합니다.
#     2.주제:는 입력 문서의 주제를 한줄로 요약합니다.
#     3.요약:은 입력 문서를 5줄로 요약합니다.
#     4.가능한 질문:은 입력 문서로부부터 사람들이 할 수 있는 질문 세가지를 파이썬 리스트 형태로 작성합니다.
#     5.가능한질문:이 반드시["질문1","질문2","질문3"]과 같이 파이썬 리스트 형태로 작성되어야하는 점에 유의하십시오.
#     이제시작합니다."""
#
#     # user_content = "입력: " + input_text + "\n 주제:" # 굳이 이렇게 하지 않아도 되는 듯 한데
#     user_content = input_text
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role" : "system", "content" : system_prompt},
#             {"role" : "user","content" : user_content}
#         ]
#     )
#
#     return completion.choices[0].message.content
#
# text ="""
# 부산일보가 올해 창간 80주년을 맞는다. 1946년 격동의 해방 직후, 지역 사회의 눈과 귀가 되겠다는 다짐은 80년간
# 이어져 부산·울산·경남의 역사와 함께 호흡해 왔다. 산업화, 민주화와 지역의 성장,
# 시민의 희로애락까지. 지면에는 늘 시대의 맥박과 지역의 목소리가 함께 했다.
# ‘지역의 진실을 밝히고 공공의 이익을 옹호한다’는 창간사는 80년 부산일보의 흔들리지 않는 독립성,
# 현장성, 책임감의 기준이자 시민들에게 한 약속이기도 했다. 매일의 취재와 보도에 이 약속을 담아내고자 부산일보는 현장을 뛰고 또 뛰었다.
# 창간 직후 피란 수도 부산의 일상, 생존의 기록은 전국 일간지 중 부산일보는 가장 먼저,
# 가장 밀착해 보도했다. 1950년 8월 18일부터 10월 27일까지, 1951년 1월 4일부터 1953년 8월 15일까지.
# 두 차례 임시 수도가 된 부산에서 지역 대표 신문은 전국 대표 신문으로 시민들의 알 권리를 충족시켰다.
# 항만, 철도, 부산 판자촌의 풍경은 훗날 한국전쟁의 삶을 어떤 자료보다 생생하게 증언하는 사료가 됐다.
# 1960년 4월 12일 부산일보에 보도된 마산만에 떠오른 김주열 열사의 사진은 민주화의 불씨를 지폈다.
# 김 열사의 머리와 눈에 최루탄이 박힌 사진은 대대적인 학생 시위로 이어졌고 4.19 혁명의 도화선이 됐다.
# 부산일보는 ‘나는 마산 소요를 목격했다’ 시리즈를 15회에 걸쳐 오직 시민과 민주주의의 편에서 보도를 이어갔다.
# """
#
# result = return_answer(text)

############################################################# 3. 지시자에게 예시를 들어 방향성 결정
# 아래의 Example은 세부적으로 어떠한 방향성을 지시할 때 사용하는데 설명하기기 곤란할때 사용하면 적절하다.
# 예를들면 3개의 리스트 앞에 keyword1. keyword2, keyword3을 붙이는 것을 말로 설명해도 되지만 길어진다.

# def return_answer(input_text = ''):
#     system_prompt = """입력 문서에서 키워드를 3개만 추출하고 추출된 키워드는 파이썬 리스트 형식으로 보여주세요.
#
#     [Example]
#     input:지방 자치가 본격화한 1995년 이후 지방 행정 감시, 정책 검증 보도도 부산일보의 몫이었다. 도시 개발 문제부터 재개발, 시민 안전 문제 등 지역의 관심사를 조명했다. 부산일보의 외침은 공론화의 메아리가 돼 돌아왔다. 부산일보가 지키려 했던 금정산은 2025년 국립공원이 됐다. 2002년 부울경 지역에서 발생한 역사상 최악의 참사 중 하나인 김해 돗대산 항공기 추락 사고 이후 지역에 새로운 공항이 필요하다는 ‘가덕신공항’ 어젠다는 20여년동안 부산일보가 지역 민의의 창구로 필요성을 역설하고 있는 사명이기도 하다.
#     keyword:['keyword1:재개발', 'keyword2:부산일보', 'keyword3:가덕신공항']
#     """
#
#
#     user_content = input_text
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role" : "system", "content" : system_prompt},
#             {"role" : "user","content" : user_content}
#         ]
#     )
#
#     return completion.choices[0].message.content
#
#
# text ="""
# 부산일보가 올해 창간 80주년을 맞는다. 1946년 격동의 해방 직후, 지역 사회의 눈과 귀가 되겠다는 다짐은 80년간
# 이어져 부산·울산·경남의 역사와 함께 호흡해 왔다. 산업화, 민주화와 지역의 성장,
# 시민의 희로애락까지. 지면에는 늘 시대의 맥박과 지역의 목소리가 함께 했다.
# ‘지역의 진실을 밝히고 공공의 이익을 옹호한다’는 창간사는 80년 부산일보의 흔들리지 않는 독립성,
# 현장성, 책임감의 기준이자 시민들에게 한 약속이기도 했다. 매일의 취재와 보도에 이 약속을 담아내고자 부산일보는 현장을 뛰고 또 뛰었다.
# 창간 직후 피란 수도 부산의 일상, 생존의 기록은 전국 일간지 중 부산일보는 가장 먼저,
# 가장 밀착해 보도했다. 1950년 8월 18일부터 10월 27일까지, 1951년 1월 4일부터 1953년 8월 15일까지.
# 두 차례 임시 수도가 된 부산에서 지역 대표 신문은 전국 대표 신문으로 시민들의 알 권리를 충족시켰다.
# 항만, 철도, 부산 판자촌의 풍경은 훗날 한국전쟁의 삶을 어떤 자료보다 생생하게 증언하는 사료가 됐다.
# 1960년 4월 12일 부산일보에 보도된 마산만에 떠오른 김주열 열사의 사진은 민주화의 불씨를 지폈다.
# 김 열사의 머리와 눈에 최루탄이 박힌 사진은 대대적인 학생 시위로 이어졌고 4.19 혁명의 도화선이 됐다.
# 부산일보는 ‘나는 마산 소요를 목격했다’ 시리즈를 15회에 걸쳐 오직 시민과 민주주의의 편에서 보도를 이어갔다.
# """
#
# result = return_answer(text)
# print(result)


############################################################# 4. 조금 확장해서 감성분류를 해보자.
# 앞에서 수행한 네이버 영화평론을 예로 해보자

# def return_answer(input_text=''):
#     system_prompt = """주어진 텍스트가 긍정인지 부정인지 중립인지 예측하시오. 답변은 긍정, 부정, 중립 
#     3가지 형태로 답변을 해야만 합니다. 답변시 주어진 택스트를 같이 출력해야만 합니다.
    
#     ex) "무슨 영화가 이래" ==> "부정"
#     """

#     user_content = input_text
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": user_content}
#         ]
#     )

#     return completion.choices[0].message.content


# df = pd.read_table('ratings_test.txt')
# df = df['document'].loc[2:5]


# for index, _ in enumerate(range(0,len(df))):
#     text = df.iloc[index]
#     result = return_answer(text)
#     print(result)