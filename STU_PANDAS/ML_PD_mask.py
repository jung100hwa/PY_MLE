import pandas as pd

data = {'A': [1,2,3,3,3], 'B': ['hello','world','python','pandas','query']}
df = pd.DataFrame(data)
print(df)

# todo 쿼리, 조건은 주로 컬럼에 주는 것이다. sql를 생각해라.

# 바로 df에 줄 수 있다.
mask = df['A'] > 2
print(df[mask])

# 마스크라는 함수는 마스크 원래 정의를 실현하는 함수이다. 즉 아래는 조건에 맞는 값을 NaN처리한다.
print(df.mask(mask))

# loc를 이용할 수 있다.
print(df.loc[mask])