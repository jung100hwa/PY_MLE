import re

# 본격적인 정규표현식
data1 = "abc dec"
data2 = "ab1c12"
data3 = "12abc efg"
data4 = "123 abc abcd"
data5 = "bcd"

# []가로안에 표시된 문자중 하나
# ? : 0 또는 1,  + : 하나 이상, * : 0번 이상
p = re.compile("[a-z]+")


# 처음에 매칭되는 것만 찾아서 리턴
# 즉 처음부터(자리수) 따짐
print('\n---------->match는 처음부터 매칭되는 것을 찾는다')
print(p.match(data1))
print(p.match(data2))
print(p.match(data3))
print(p.match(data4))
print(p.match(data5))

print('\n---------->group()함수는 결과를 리턴. 처음한번만')
strTest = 'abc  addd bbb'
m = p.match(strTest)
print(m.group())

# 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색, 중간에 있어도 상관없다.
# 처음에 매칭되는 것만 찾아서 리턴
print("\n---------->search()")
print(p.search(data1))
print(p.search(data2))
print(p.search(data3))
print(p.search(data4))


# 이것은 문자열 전체를 검색하여 매치되는 것만 리스트 형식으로 리턴
print("\n---------->findall() serach 해당하는 모든 물자열 출력")
data4 = "123 abc abcd"
print(p.findall(data4))  # abc와 abcd 둘다 해당 됨
result = p.findall("life 8is too short")
print(result)

# findall 매칭 대상 다시 테스트. t다음에 공백이 있음
matchObj = re.findall('\t ', 'a\tb\tc\t \t d')
print(matchObj)

# 컴파일 옵션. 옵션이 없으면 줄바꿈 문자는 제외한다. 
# "." 정규식은 줄바꿈문자를 제외하고 모든 문자와 대칭
# [.]안에 있는 "." 는 그냥 "."의미함
print("\n---------->'a.b'")
p = re.compile('a.b')
m = p.match('abb')
print(m)

# re.DOTALL 줄바꿈 문자 포함
print("\n---------->'a.b', re.DOTALL")
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
print(m.group())

########################################## 정리
# match, serarch, findall 차이
# match : 맨처음에 일치 여부. 첫 일치 하는 단어만 리턴
# serarch : 전체에서 일치 여부. 첫 일치하는 단어만 리턴
# findall : 전체에서 일치 여부. 일치하는 단어 전체 리턴.

# match
p = re.compile('a.b', re.DOTALL)
m = p.match('123 a\nb c\nb')
print(m)

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())  # <html~~~~title> 이러니까 다 나오는 구나
print(re.match('<.*?>', s).group()) # ?문자 앞에 점(.), + 등과 함께 쓰면 최소한의 반복을 수행

# serarch
p = re.compile('a.b', re.DOTALL)
m = p.search('123 a\nb a\nbb')
print(m)

# findall
p = re.compile('a.b', re.DOTALL)
m = p.findall('123 a\nb a\nbb')
print(m)




