# 식약처에서 이관 데이터에는 물질정보에 주성분이라는 것을 입력하지 않음
# 때문에 과학원에서 가지고 엑셀 DB를 가지고 업데이트 시키는 작업을 해야 함

import pandas as pd

df = pd.read_excel('./Pandas/안생DB.xlsx')
print(df.head())
print('\n')

# 양쪽 공백이 있으면 제거, str.strip() 이함수는 숫자는 오류, 또는 숫자를 NaN 처리 해버림
# 모든 컬럼을 위해 람다 함수 사용

df = df.apply(lambda x : x.str.strip() if type(x) == 'object' else x, axis = 1)
print(df.head())