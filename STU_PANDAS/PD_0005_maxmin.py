import pandas as pd
import numpy as np

data = {'name': ['Oliver', 'Harry', 'George', 'Noah'],
        'mat': [90, 99, 50, 65],
        'eng': [88, 76, 95, 79],
        'kor': [10,40,10,np.nan],
        'git': ['상','중','하','꽝']}
                
df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)
print('\n')

# 숫자와 문자열이 석이거나 문자열이면 모두 문자열로 변환해서 아스키코드값을 비교한다.
# mean, mdian에서 문자열은 적용되지 않는다. 문자열에 해당 함수를 쓰려고 하면 오류 난다.
print(df.max())
print(df['kor'].max())

print(df.min())
print(df['kor'].min())

# 표준편차는 아에 문자열은 계산에서 자동 제외한다. 자동으로 제외되지 않은 듯 한데. 오류난다.
# print(df.std())

# 이렇게 해도 된다. agg라는 함수 참 유용하다.
print(df.agg(['max']))
print(df.agg(['max','min']))