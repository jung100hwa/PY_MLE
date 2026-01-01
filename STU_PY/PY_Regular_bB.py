import re

# 원노트 정리 된 것 참고

text = "Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English."
print(re.findall(r'\b.', text))

text = "Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English."
print(re.findall(r'\b.\b', text))


tList = ['foo', 'foo.', '(foo)', 'bar foo baz', 'foo_', 'foobar','foo3']

for item in tList:
    print(item + " ===> ", end="")
    print(re.findall(r'\b.', item))


# 아래는 'foo_', 'foobar','foo3' 둘은 일치하지 않음
for item in tList:
    result = re.search(r'\bfoo\b', item)
    if result:
        print(item + " ==> " + result.group())


# 아래는 모두 선택된다.
p = re.compile(r'\b[a-zA-Z]+\b')
m = p.findall('no class as all')
print(m)


p = re.compile(r'\Bclass\B')
m = p.search('noclassed at all')
print(m)


# 양쪽에 문자난 숫자로 되어 있는 연속된 문자열을 출력
# class -> las, all->l 이렇게 출력된다.
p = re.compile(r'\B[a-zA-Z]+\B')
m = p.findall('no class as all')
print(m)