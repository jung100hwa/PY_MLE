import pandas as pd

# 공백을 제거하는 함수
s = pd.Series([' Mouse', '\tdog ', ' house and parrot ', 'cat \n'])

print(s.str.lstrip())

print(s.str.rstrip())

print(s.str.strip())