import  re

# sub 문자열 바꾸기, replace를 써도 된다.


# blue, yellow를 colour로 변경
print("\n===============>문자열을 바꾸기")
p = re.compile('blue|yellow')
print(p.sub('colour', 'blue and yellow and red is my favorite color'))


# sub 메소드의 참조를 이용하여 이름과 전화번호의 순서를 바꿈
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park3 010-1234-5678"))