import re

# $ 끝문자열. 마찬가지이다 하나의 라인에서 문장 끝을 의미 함
print('\n==============> $ 끝문자열')
print(re.search('short$', 'life is too short'))

# $ 마찬가지 멀리라인 옵션을 주면 각 라인의 끝에 매칭단어가 있으면 참으로 인식한다.
data = """python one
life is too short \npython two
you need one
python three"""

p = re.compile("one$", re.MULTILINE)
print(p.findall(data))