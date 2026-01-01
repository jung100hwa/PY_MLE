# 불러온 데이터에서 컬럼의 순서를 바꾼다.
# 원하는 컬럼만 표출한다. 컬럼의 순서를 바꿀일은 거의 없다.

import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']

print(df.head())
print('\n')

# 알파벳 순서로 열의 순서를 바꾼다.
columns = list(df.columns.values)
columns = sorted(columns)
print(columns)
ndf = df[columns]   # 이렇게도 표현할 수 있네
print(ndf)

# 현재의 역순으로 바꾼다.
columns = list(ndf.columns.values)
columns = reversed(columns)
ndf = ndf[columns]
print(ndf)

# 임의의 순서로 바꿀 수 있다. 어차피 리스트 이니까
columns = ['pclass','sex','age','survived']
ndf = ndf[columns]
print(ndf)