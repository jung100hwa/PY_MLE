import pandas as pd
import numpy as np

# 두개의 프레임을 이용하여 데이터 업데이트 하기
df1 = pd.DataFrame({'A': [1, 4], 'B': [4, 4]})
df2 = pd.DataFrame({'A': [2, 1], 'B': [3, 5]})

# 컬럼단위로 수행을 하되 값은 요소를 리턴
# 1. 아래의 필터는 컬럼의 합을 비교(이건 당연 컬럼 단위, 행단위면 타입 다를 수 있으니. 상식적으로 생각)
# 2. 합이 적으면 적은 쪽의 요소를 리턴. 전체 합을 리턴하는 것이 아님
take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2

print(df1)
print(df2)

ndf = df1.combine(df2, take_smaller)
print(ndf)

# 컬럼단위의 sum 등 비교아닌 요소각각을 비교하려면 아래와 같이 numpy를 사용
# 오히려 이걸 더 많이 사용할 것 같네.
df1 = pd.DataFrame({'A': [5, 0], 'B': [2, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
ndf = df1.combine(df2, np.minimum)
print(ndf)


# 컬럼이 일치하지 않으면 NaN, 그리고 중요한 것은 sum에서 None은 0 처리함
df1 = pd.DataFrame({'A': [5, 0], 'B': [2, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'C': [3, 10]})

print(df1)
print(df2)
ndf = df1.combine(df2, take_smaller)
print(ndf)

# 없는 칼럼을 값으로 채워놓고 계산
ndf = df1.combine(df2, take_smaller, fill_value=10)
print(ndf)

df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2

print(df1)
print(df2)


# 여기는 없는 값을 -5로 채워놓고 계산
ndf = df1.combine(df2, take_smaller, fill_value=-5)
print(ndf)


# 만약에 컬럼, 인덱스가 일치하지 않는 경우, NaN, None은 시리즈에서 sum할 때 0으로 간주한다.
# 그래서 아래 결과가 이해가 안될 수도 있다. 여기 참조. https://zephyrus1111.tistory.com/128
df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
df2 = pd.DataFrame({'B': [3, 3], 'C': [-10, 1], }, index=[1, 2])
ndf = df1.combine(df2, take_smaller)
print(ndf)

# NaN일 때 오버라이트 해버리기 위해서는 아래와 같이. df2기준
df1 = pd.DataFrame({'A': [5, 0], 'B': [2, 4], 'C':[1,1]})
df2 = pd.DataFrame({'A': [4, 1], 'B': [3, 3]})
ndf = df2.combine_first(df1)
print(ndf)

# df1기준
df1 = pd.DataFrame({'A': [None, 0], 'B': [None, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
ndf = df1.combine_first(df2)
print(ndf)

# 인덱스도 틀리고 컬럼도 없을 때, df1 기준
df1 = pd.DataFrame({'A': [None, 0], 'B': [4, None]})
df2 = pd.DataFrame({'B': [3, 3], 'C': [1, 1]}, index=[1, 2])
ndf = df1.combine_first(df2)
print(ndf)