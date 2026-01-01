import re

# "." 하나의 문자를 의미, [.]그냥 "." 그 자체
# 만약에 점을 6개를 연속어로 컴파일 옵션에 넣으면 6개 문자씩 그룹핑해서 출력한다.

text = "Regular expressions are powerful!!! "

# Regular에 R만 선택. 첫번째 항목만 출력된다.
print(re.search('.', text))

# 전체 문자열 선택. 문자하나씩 리스트 형태로 돌려준다.
print(re.findall('.', text))


# 문자를 6개(몇개를 선택하든 상관없이)를 옵션에 넣으면 6개 문자씩 그룹핑 해서 일치된 문자열을 리스트로 돌려준다.
print(re.findall('......', text))