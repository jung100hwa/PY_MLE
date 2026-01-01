# 데이터의 정해진 구간으로 분리해서 구간마다 이름을 정하기

import pandas as pd
import numpy as np

df = pd.DataFrame({
'a': [1,2,3,4, 5, 6, 7,8,9,10],
'b': [10, 20, 30, 40, 50, 60,70,80,90,100]
})

print(df)

# 단계1 컬럼 'a'에 해당하는 값을 3구간으로 나눌 경계값을  구한다.
count, bin_dividers = np.histogram(df['a'], bins=3)
print(bin_dividers)

# 단계2 새로운 컬럼에 'a' 값을 경계값과 비교하여 각 경계값에 맞는 문자 또는 값을 새로운 컬럼 넣는다.
bin_names = ['하', '중', '상']
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