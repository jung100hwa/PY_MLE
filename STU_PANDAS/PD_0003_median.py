import pandas as pd
import numpy as np

data = {'name': ['Oliver', 'Harry', 'George', 'Noah'],
        'mat': [90, 99, 50, 65],
        'eng': [88, 76, 95, 79],
        'kor': [20,40,10,np.nan]}
                
df = pd.DataFrame(data)

df.set_index('name', inplace=True)
print(df)
print('\n')

# 중간값이란 순서대로 나열했을 때 중앙에 위치하는 값
# todo 만약에 짝수일 때에는 중앙값이 2개이니까 이 2개의 값을 평균낸다.
print(df.median())
print(df.agg(['median']))         # 위의 값과 같은데 데이터프레임을 리턴한다.
print(df['kor'].agg(['median']))  # agg도 값이 하나일때는 시리즈로 리턴한다.

print(df['kor'].median())         # Null은 제외하고 구한다. 이게 중요한 듯. 널은 항상 제외