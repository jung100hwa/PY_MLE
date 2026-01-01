# 1. 데이터정비(데이터정리->널삭제->숫자타입변경)
# 2. 범주(경계)로 사용할 컬럼을 np.histogram으로 경계값을 구함(여기 부분을 활용할 기회가 많을 듯 함)
# 3. cut 함수로 하나의 컬럼에 범주화 함
# 4. 원핫 코딩은 옵션(범주를 컬럼화 하여 0,1로 값을 채움)

########### 활용방안
# 어떤 컬럼의 값을 3개 또는 원하는 개수로 그룹핑하여 누구는 어디에 속하는지 등등

import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('../E_FILE/PANDAS/auto-mpg.csv')

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df)
print('\n')


# 사전처리(데이터정리->널삭제->타입변경)
print(df['horsepower'].unique())
df['horsepower'] = df['horsepower'].replace('?',np.nan)

print(df['horsepower'].unique())
df.dropna(subset = ['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
print(df)

print(df['horsepower'].unique())
print('\n')

# 넘파이 histogram 함수를 이용하여 경계값 리스트 구하기(이 함수가 핵심인듯)
# 예제처럼 3개로 나누어서 자동으로 구역의 경계값을 추출
print("####################### histogram")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)
print('\n')

# 구해진 경계값으로 구간을 분리하고 구간이름열 지정하여 새로운 컬럼에 적용
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(
    x=df['horsepower'],
    bins = bin_dividers,
    labels=bin_names,
    include_lowest=True)
print(df[['horsepower','hp_bin']].head(15))
print('\n')

print("####################### get_dummies")
df_dummy = pd.get_dummies(df['hp_bin'])
print(df_dummy)
print('\n')

# 결과를 합쳐 보자
ndf = df[['horsepower','hp_bin']]
print(ndf)
print('\n')

# 원핫코딩시 불필요한 메모리낭비가 심함
jdf = pd.concat([ndf, df_dummy], axis=1, join='outer')
print(jdf)
print('\n')



df = pd.DataFrame({
'a': [1,2,3,4, 5, 6, 7,8,9,10],
'b': [10, 20, 30, 40, 50, 60,70,80,90,100]
})

print(df)

# 단계1 컬럼 'a'에 해당하는 값을 3구간으로 나눌 경계값을  구한다.
count, bin_dividers = np.histogram(df['a'], bins=3)
print(bin_dividers)

# 단계2 새로운 컬럼에 'a' 값을 경계값과 비교하여 각 경계값에 맞는 문자 또는 값을 새로운 컬럼 넣는다.
bin_names = ['상', '중', '하']
df['hp_bin'] = pd.cut(
    x=df['a'],
    bins = bin_dividers,
    labels=bin_names,
    include_lowest=True)

print(df)

# 단계3 원핫코딩
df_dummy = pd.get_dummies(df['hp_bin'])
print(df_dummy)
print('\n')

# 단계4 원핫코딩과 원래의 df를 합치자
jdf = pd.concat([df, df_dummy], axis=1, join='outer')
print(jdf)
print('\n')