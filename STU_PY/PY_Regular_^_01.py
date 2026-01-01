import re

# []안에서 ^의 의미는 각각의 문자가 포함되지 않은 것. [^abc] 라고 하면 a, b, c 어느 문자도 포함되지 않은 걱을 찾는다.
# 아래의 결과는 모두 None
s = re.compile("[^abc]")
print(s.search("ab"))
print(s.search("b"))
print(s.search("c"))


# [] 안이 아니면 ^시작문자열을 나타낸다.
# ^ 시작문자열(한줄에서 시작점을 의미 함. 중간에 있는 동일 문자열은 아님)
# 그리고 멀티라인을 인식시키기 위해서는  TODO : re.MULTILINE 이 옵션을 사용해야 한다.
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life is too short')) # 출력되지 않음


# 멀티라인 & ^의 조합
p = re.compile('^Life',re.MULTILINE)


# Life 시작하지 않음
m = p.search('My Life is too short')
print(m)


# \n 멀티 라인, re.MULTILINE 이 조건이 있기때문에 일치
m = p.findall('My \nLife is too short')
print(m)


# 테스트 멀티 라인 1. 이렇게 변수에 받아서 하면 멀티 라인으로 인정
data = """My 
Life is too short"""
m = p.search(data)
print(m)

# 테스트 멀티 라인이 맞기 맞는데 앞에가 공백이 있기 때문 Life로 시작하지 않음
data = """My 
                Life is too short"""
m = p.search(data)
print(m)


data = """python one
life is too short
python two
you need python
python three"""

# python으로 시작하고(^) 화이트스페이스가(\s) 있고 뒤에 하나 이상의 문자{\w)가 와야 함
p = re.compile("^python\s\w+")
print(p.findall(data))  # python one만 출력


# re.MULTLINE
data = """python one
life is too short \npython two
you need python
python three"""

print(data)

# 위에 데이터 처럼 줄바꿈이 있을 때 시작문장이 python으로 시작되는 것만
#  결국 re.compile('python\s\w+')와 동일하다.
print('\n============>re.MULTILINE')
p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))