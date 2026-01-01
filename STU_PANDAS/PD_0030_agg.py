from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3],[4, 5, 6],[7, 8, 9],[np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])
print(df)

# 기본이 컬럼 단위로 계산을 한다.
print(df.agg(['sum','min']))


# 컬럼마다 다른 함수를 적용
print(df.agg({'A' : ['sum','min'], 'B':['min','max']}))


# 컬럼마다 다른 함수를 적용하고 인덱스 명을 바꾸는 것
print(df.agg(x=('A', max), y=('B', 'min'), z=('C', np.mean)))


# 행단위로 계산
print(df)
print(df.agg('min', axis=1))
print(df.agg(['max','min'], axis=1))


################################################### 추가
# 커럼을 추가 할 수 있다. 이게 유용할 것 같다.
df['D'] = df.agg('min', axis=1)
print(df)


# 컬럼단위
print(df.agg(['min'], axis=0))


# 하나의 컬럼에 대해 불러오기
print(df['A'].agg('max'))
print(df.agg('min', axis=0))    # 시리즈로 반환
print(df.agg(['min'], axis=0))  # 데이터프레임으로 반환

################################################### 추가
# 컬럼단위로 한다면 이렇게 직접 적어도 되네.
print(df.agg('mean', axis='columns'))

################################################### 업그레이드
# group by를 참고하시라
# apply보다는 agg만 사용
# - agg는 알아서 계산 가능한 열만 계산한다.
# - apply는 계산할 수 없는 열이 포함되어 있을 때 오류를 출력한다.