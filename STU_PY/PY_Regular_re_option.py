import re

# re 옵션들

# 개행문자도 하나의 문자로
print(re.findall('a..', 'abc a  a\na'))
print(re.findall('a..', 'abc a  a\na', re.S))
print(re.findall('a..', 'abc a  a\na', re.DOTALL))

# 모드 변경자. 원노트에 보면 inline flag로 되어있는데 여하튼 systax, long syntax와 같은 의미 이다.
print(re.findall('(?s)a..', 'abc a  a\na'))         # 문자열 전체를 모두 문자로 취급
print(re.findall('(?is)a..', 'ABc Adb  a\na'))      # 문자열 전체를 모두 문자로 취급하데 대소문자도 가리지 않음

print(re.findall('(?is:a..) and abc is good',       # 문자열 전체를 모두 문자로 취급하고 대소문자는 앞에 나온것만 가리기 않음
'''
ABc and abc is good.
abc and Abc is good.                                 
'''))

print(re.findall('(?is)a.. and abc is good',        # 문자열 전체를 모두 문자로 취급하고 대소문자 가리지 않음. 위에 비교
'''
Abc and abc is good.
abc and Abc is good. 
'''))