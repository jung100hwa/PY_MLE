import pandas as pd
import numpy as np

data = {'name': ['Oliver', 'Harry', 'George', 'Noah'],
        'mat': [90, 99, 50, 65],
        'eng': [88, 76, 95, 79],
        'kor': [20, 40, 10, np.nan]}

df = pd.DataFrame(data)
print(df)

# 1단계) 데이터 전처리
df.fillna(method='ffill', inplace=True)
print(df)

# 2단계) 데이터타입 숫자형, 타입은 inplace 인자가 없기때문에 자신것으로 받아야 함
df = df.astype({'kor':'int64'})
print(df.info())

# 3단계) 점수라는 컬럼을 자동을 만들고 kor 점수를 대상으로 상중하로 구분
df.loc[df.eval('kor >= 40'), 'score'] = '상'
df.loc[df.eval('20 <= kor and kor < 40'), 'score'] = '중'
df.loc[df.eval('kor <= 10'), 'score'] = '하'
print(df)

# 3단계가 기능한 이유는 loc[['리스트'],['리스트']] 즉 kor >=40 라는 조건을 먼저 df전체에 수행한다.
# 그리고 그 다음 조건을 또 df 전체에. 그다음 조건을 또 전체 그려면 아마도 [True, False, True...] 이렇게 얻어 질터인데
# True는 1, False 0 결국 각행에 1인 것만 출력 또는 입력한다. 아래 소스 참조
data = {'aa': [95, 70, 65, 45, 85],
        'bb': [170, 170, 170, 170, 170]}
df = pd.DataFrame(data)
print(df)

df.loc[[True,True,True,True,True],'cc'] = 300
print(df)