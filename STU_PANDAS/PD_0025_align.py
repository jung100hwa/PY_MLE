
# 그냥 join을 활용하자. 이렇게 복잡해서 join 결과가 데이터프레임이다. 튜플이 아니다.
# 좀더 디테일하게 하고 싶을 때에는 merger를 사용하자. 
# 거의 사용하지 않을 듯. 너무 이해할려 하지 말자

from ntpath import join
import pandas as pd
import numpy as np


n=np.NaN
col1 = ['col1','col2','col3']
row1 = ['row1','row2','row3']
data1 = [[1,2,3],[5,6,7],[9,n,11]]

col2 = ['col2','col3','col4']
row2 = ['row3','row4','row5']
data2 = [[10,11,12],[14,n,16],[18,19,20]]

df1 = pd.DataFrame(data1,row1,col1)
df2 = pd.DataFrame(data2,row2,col2)

print(df1)
print(df2)


# join 이용을 함, 디폴트는 outer, 결과는 튜플형태, left, right를 합친것
ndf = df1.align(df2)
print(ndf)


# 결과가 항상 튜플형태로 나오니까 첫번째 것을 리스트로 뽑아내보자
print(ndf[0])
print(ndf[1])


# left, 왼쪽 기준에만 있는 것 즉 df1에만 있는 것
ndf = df1.align(df2, join='left')
print(ndf)
print(ndf[0])
print(ndf[1])


# inner, 공통된것만 나옴
ndf = df1.align(df2, join='inner', axis=None)
print("#" * 50)
print(df1)
print(df2)
print(ndf)
print(ndf[0])
print(ndf[1])

# axis = None 디폴트, 0=인덱스, 1=컬럼, 즉 0이면 인덱스를 기준으로 조인. None 로우와 컬럼 둘다 동일한 것만 조인하는 듯
ndf = df1.align(df2, join='inner', axis=0)
print(df1)
print(df2)
print(ndf)
print(ndf[0])
print(ndf[1])

# axis = None 디폴트, 0=인덱스, 1=컬럼, 즉 1이면 인덱스를 기준으로 조인
ndf = df1.align(df2, join='inner', axis=1)
print(df1)
print(df2)
print(ndf)
print(ndf[0])
print(ndf[1])

# fill_values 결측치를 채우는데 원래 부터 가지고 있는 결측치는 바뀌지 않는다.
ndf = df1.align(df2, join='outer', fill_value='X')
print(ndf[0])

# method, 결측치를 채우는 방법, 원래 가지고 있던 결측값으로 채운다. ffill =이전값
# 이전값이 널이면 대상값도 널이다.
ndf = df1.align(df2, join='outer', method='ffill')
print(ndf[0])

# limit는 method를 몇개까지 적용할지. 이때 기존 nan은 개수에 포함되지 않는다.
# fill_axis는 method의 ffill, bfill를 가로로 할 지 세로로 할지
print(df1.align(df2, join='outer')[0])
ndf = df1.align(df2, join='outer', method='ffill')
print(ndf[0])

# 즉 limit는 몇개까지 앞의 값 또는 뒤의값을 적용할지 범위. 만약에 1이고 ffill이면
# 조인해서 나온(!!!!.중요함 원래 자기가 가지고 있던 NaN은 그대로 NaN으로 표시됨) 최초 나온값 NaN을 한번만
# 앞에 값을 적용한다.
print(df1.align(df2, join='outer')[0])
ndf = df1.align(df2, join='outer', method='ffill', limit=1)
print(ndf[0])

# 이번에는 인덱스 기준이 아닌 컬럼 기준으로 변경해 보자, ffill, bfill 실행해보고 나름 개념을 잡자.
# fill_axis=0이면 같은 컬럼의 바로 위아래 값을 참조, fill_axis=1이면 같은 행의 좌우를 값을 참조한다.  
# 이걸 쓸이유는 없다. 컬럼은 말그대로 고유의 성질이 있는데...
print(df1.align(df2, join='outer')[0])
ndf = df1.align(df2, join='outer', method='ffill', fill_axis=1)
print(ndf[0])