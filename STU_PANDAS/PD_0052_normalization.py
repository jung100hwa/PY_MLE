# 정규화 함
# 1. 데이터 검토
# 2. 이상값 널처리
# 3. 널값 삭제 또는 대체
# 4. 타입변경

import pandas as pd
import os
import numpy as np

G_ExFilePos = os.getcwd()

df = pd.read_csv('./E_FILE/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 
print(df.head())
print(df.info())


print(df['horsepower'].values)
df['horsepower'].replace('?', np.nan, inplace=True)


print(df['horsepower'].values)
df.dropna(subset=['horsepower'], axis=0, inplace=True)

print(df['horsepower'].values)

df['horsepower'] = df['horsepower'].astype('float')

# 최대값을 확인
print(df['horsepower'].describe())

# 열의 최대값의 절대값으로 나누기
print('\n=============================')
# df.horsepower = df.horsepower / abs(df.horsepower.max())
# 이렇게 해도 동일한 값을 얻는다.
df.horsepower = df.horsepower / abs(df['horsepower'].max())
print(df.horsepower.head())
print(df.horsepower.describe())

# 테스트
raw_data = {'a': [1, 2, 3, 4],
            'b': [10, 20, 30, 40],
            'c': [100, 200, 300, 400]}

df = pd.DataFrame(raw_data)
print(df.a.max())
print(df.a.min())

# 이렇게 해도 된다.
print('\n=============================')
print(df['a'].max())