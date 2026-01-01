import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('../E_FILE/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head())

# method = 'pearson', 'spearman', 'kendall'이것들 중의 하나
# +1은 양의 상관관계,-1은 음의 상관관계. 여하튼 +, - 이면 관계가 있다는 것이다.
# 0이면 관계가 없다는 것이다. 관계파악에서 필요할 듯

# 일단 실수만 되는 듯. 문자열은 안되는 듯
print(df.isnull().any()) # 이렇게 하면 각열에 대하여 nan여부 출력

df.replace("?", np.nan, inplace=True)
print(df.isnull().values.any())
df.dropna(inplace=True)

print(df.isnull().values.any())   # 이렇게 하면 하나의 값으로 nan 출력. 컬럼에 하나라도 nan 있으면 True

# 문자열 삭제
df.drop('name',axis=1, inplace=True)

ndf = df.corr(method='pearson')
print(ndf)