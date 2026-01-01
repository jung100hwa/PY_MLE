# 1. 데이터정비(데이터정리->널삭제->숫자타입변경)
# 2. 범주(경계)로 사용할 컬럼을 np.histogram으로 경계값을 구함
# 3. cut 함수로 하나의 컬럼에 범주화 함
# 4. 원핫 코딩은 옵션(범주를 컬럼화 하여 0,1로 값을 채움)

import pandas as pd
import numpy as np
from tabulate import tabulate

# read_csv() 함수로 df 생성
df = pd.read_csv('./E_FILE/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

print(df.info())

# 사전처리(데이터정리->널삭제->타입변경)
print(df['horsepower'].unique())
df['horsepower'] = df['horsepower'].replace('?',np.nan)

print(df['horsepower'].unique())
df.dropna(subset = ['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
print(tabulate(df, headers='keys', tablefmt='simple_outline'))

print(df['horsepower'].unique())
print('\n')

#################################################################### 활용1
# 넘파이 histogram 함수를 이용하여 경계값 리스트 구하기(이 함수가 핵심인듯)
# 예제처럼 3개로 나누어서 자동으로 구역의 경계값을 추출
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)
print('\n')

print(df['horsepower'].min())

# 구해진 경계값으로 구간을 분리하고 구간이름열 지정하여 새로운 컬럼에 적용
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(
    x=df['horsepower'],
    bins = bin_dividers,
    labels=bin_names,
    include_lowest=True)
# print(df[['horsepower','hp_bin']].head(15))
print(tabulate(df[['horsepower','hp_bin']].head(15), headers='keys', tablefmt='simple_outline'))
print('\n')
####################################################################


# 특정열을 구간으로 분리한 다음 구간마다 열을 만드는데 값은 0, 1 원핫 코딩이라고 함
df_dummy = pd.get_dummies(df['hp_bin'])
# print(df_dummy) # 이렇게 하니까  0,1 이 아닌 True, False로 출력이 되네
# 아래 처럼 하니까 제대로 출력되는 듯
print(tabulate(df_dummy.head(10), headers='keys', tablefmt='simple_outline'))

print('\n')

# 결과를 합쳐 보자
ndf = df[['horsepower','hp_bin']]
print(tabulate(ndf.head(10), headers='keys', tablefmt='simple_outline'))

print('\n')

# 원핫코딩시 불필요한 메모리낭비가 심함
jdf = pd.concat([ndf, df_dummy], axis=1, join='outer')
print(tabulate(jdf.head(10), headers='keys', tablefmt='simple_outline'))

print('\n')