import pandas as pd
import numpy as np

# 요소를 정의된 문자로 분리한다.
s = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)
print(s)

print(s.str.split())

# 분리하고자 하는 개수, 1이면 2개로, 2이면 3개로
# 정의된 개수보다 적으면 상관없다. 분리된 개수가 많을 때 최소 정의된 개수만큼만 분리
# 왼쪽 부터 개수를 적용한다.
print(s.str.split(n=1))

# 오른쪽에서부터 개수를 적용한다.
print(s.str.rsplit(n=1))

# 분리자를 지정한다.
print(s.str.split(pat='/'))

# 데이터프레임과 멀티로 리턴 
print(s.str.split(expand=True))

# 뒤에서부터 분리자는 '/', n=2 임으로 3개로 분리하고 데이터프레임으로 결과 출력
print(s.str.rsplit(pat='/', n=2, expand=True))

s = pd.Series(["1+1=2"])
print(s)

# +를 정규식으로 정의하기 위해서 r'' 이것과 \ 을 사용함, split는 정규식을 지원함.
print(s.str.split(pat=r'\+|=', expand=True))