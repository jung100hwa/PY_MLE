import pandas as pd

# 특정한 길이로 만든다음 빈 공간은 정의된 문자로 채운다.
# 거의 사용할 일이 없다.

s = pd.Series(['Mouse', 'dog', 'house and parrot'])
print(s)

# 시리즈 요소 중 가장 긴 요소의 길이로 맞추고 나머지는 지정만 문자로 채운다.
print(s.str.pad(width=s.str.len().max(), side='left', fillchar='_'))

print(s.str.pad(width=s.str.len().max(), side='right', fillchar='_'))

print(s.str.pad(width=s.str.len().max(), side='both', fillchar='_'))