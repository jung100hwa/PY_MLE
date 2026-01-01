import  re

# 판다스 split과 비교
print('\n===============>문자열 특정 키워드로 분리하기')
text = "사과 딸기 수박 메론 바나나"
text = re.split(" ", text)
print(text)

text = """사과
딸기
수박
메론
바나나"""
text = re.split("\n", text)
print(text)

text = "사과+딸기+수박+메론+바나나"
text = re.split("\+", text)
print(text)

# 이렇게 정규식을 이용하여 분리를 하면 분리자를 여러게 지정이 가능하구나!!!아주중요
# 스페이스 2개이상을 구분자로 사용하는 것 보니 정말 대단함
text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

text = re.split('\s+', text)
print(text)


text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""
text = re.findall('\d+', text)
print(text)

# 이렇게도 가능하다. 즉 숫자를 기준으로 분리 가능.
text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""
text = re.split('\d+', text)
print(text)

# 이게 좀 더 확실하다. 하나의 문장이 있을 때 숫자중심으로 분리. 위에는 \n 문자까지 출력됨
text = "100 hgl 200 jung 300 min"
text = re.split('\d+', text)
print(text)


# 대문자만 봅아 내고 싶을 때
text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

# 이렇게 하면 문자 하나씩 뽑아낸다.
text = re.findall('[A-Z]', text)
print(text)

# 대문자이고 대문자가 4개이상 반복되는 단어로 구분
text = """100 John    PROFG
101 James   STUD
102 Mac   STUD"""
text = re.findall('[A-Z]{4}', text)
print(text)

# 1개 이상의 대문자만 추출
text = """100 John    PROFG
101 James   STUD
102 Mac   STUD"""
text = re.findall('[A-Z]+', text)
print(text)