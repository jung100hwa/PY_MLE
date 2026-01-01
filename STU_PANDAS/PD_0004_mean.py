import pandas as pd
import numpy as np

data = {'name': ['Oliver', 'Harry', 'George', 'Noah'],
        'mat': [90, 99, 50, 65],
        'eng': [88, 76, 95, 79],
        'kor': [10,40,10,np.nan]}
                
df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)
print('\n')


# 전체 열에 대한 평균, nan은 제거한다.
print(df.mean())

# nan은 행은 계산하지 않는다. 이렇게 사용하는 게  나을 듯 
print(df['kor'].mean())

# describe() 함수를 이용할 수도 있다.
print(df.describe())

# describe() 함수를 이용해서 특정 컬럼만 할수도 있다.
print(df['kor'].describe())

# 이렇게 중간값만 구할수 있다. describe 리턴이 시리즈라면 아래처럼 딕션너리 키값을 이용하 듯 구할 수 있다.
# 이때는 반드시 인덱스명이어야 한다. 인덱트명은 무조건 있는거 아니야!!
print(df['kor'].describe()['mean'])

# 시리즈라면 아래와 같이 인덱스명으로 구할 수 있다.
dict_data = {'aa':11, 'bb':22, 'cc':33}
sr = pd.Series(dict_data)
print(sr)
print(sr['cc'])