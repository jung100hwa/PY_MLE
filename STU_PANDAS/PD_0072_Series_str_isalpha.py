import pandas as pd

# 문자 숫자 등을 확인한다. is~ 계열
s = pd.Series(['one', 'one1', '1', ''])

print(s.str.isalpha())
print(s.str.isnumeric())
print(s.str.isalnum())

s = pd.Series(['A B', '1.5', '3,000'])

# 공백이나 점(.), 쉬표(,) 모두 false
print(s.str.isalnum())

s3 = pd.Series(['23','', ''])
print(s3.str.isdecimal())

# isdecimal과 동일하나 윗첨자의 숫자를 True로 인식
print(s3.str.isdigit())
print(s3.str.isnumeric())

s4 = pd.Series([' ', '\t\r\n ', ''])
print(s4.str.isspace())

# 대소문자는 전체가 소문자 대문자일때 참
s5 = pd.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])
print(s5.str.islower())

print(s5.str.isupper())

# 첫글자만 참(사용하는데가 있나)
print(s5.str.istitle())