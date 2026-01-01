import re

# [] 중괄호 안의 문자 하나와 일치 여부, 문자열이 아님. 각각의 하나의 문자와 매칭을 의미

text = "How do you do? "

# 아래 예제의 핵심은 [] 각각의 문자. 즉 or의 성격이라는 것
print(re.findall('[oyu]', text))

# []밖의 점"."은 하나의 문자를 의미 한다. 즉 아래에는 d로 시작하고 다음에 아무문자. H로 시작하고 다음에 아무문자까지의 으미
print(re.findall('[dH].', text))

print(re.findall('[owy][yow]', text))


# 점(.)은 []안에서는 하나의 문자를 의미 한다
print("\n---------->'a[.]b'")
p = re.compile('a[.]b')
m = p.match('a..b') # .이 2개라서 매칭 안됨
if m:
    print(m.group())
else:
    print('no matching')


# re.IGNORECASE 대소문자 관계없이 즉 [A-Z] 할필요 없는 거지
# 첫번째 시작문자가 알파벳인것,하나이상이 아님
p = re.compile('[a-z]', re.IGNORECASE)
m = p.match('Abc bbbc')
if m:
    print(m.group())
else:
    print('no matching')


# 한글 매칭
text = "I Love 홍"
reList = re.findall("[가-힣]", text)
print(reList)