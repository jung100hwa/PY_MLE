import pandas as pd

a = {'A' : [1, 1, 1, 2, 2, 2], 'B' : ['가', '가', '나', '나', '다', '다']}
df = pd.DataFrame(a)

print(df)

# 같은 의미
print(pd.unique(df['A']))
print(df['A'].unique())

print(pd.unique(df['B']))

print(df[['A','B']].values)

##################################### 모든 값을 펼치면서 중복값은 제외 함
# 아래와 같은 형태는 오류 남. 데이터프레임에는 unique()함수가 없음
# print(df[['A','B']].unique())

print(df[['A','B']].values.ravel())
print(pd.unique(df[['A','B']].values.ravel()))



# pd.nunique 이런 함수는 없다.
# 개수를 구하는 함수이다.
print(df)
print(df['A'].nunique())