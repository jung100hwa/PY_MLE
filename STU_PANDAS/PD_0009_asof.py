import pandas as pd
import numpy as np

# 이 함수가 유용한지는 모르겠지만 인덱스를 기준으로 하기 때문에 그렇게 활용가치가 있어 보이지는 않는다.

# 주어진 인덱스값 이전까지 결측치가 없는 마지막 행을 리턴
s = pd.Series([1, 2, np.nan, 4], index=[10, 20, 30, 40])
print(s)

# 인덱스가 20보다 같거나 작으면서 결측치가 없는 마지막 값을 리턴
print(s.asof(20))

row = [10,20,30,40,50,60]
data = {'A':[1,np.nan,np.nan,4,5,6],'B':[7,8,9,10,np.nan,12]}
df = pd.DataFrame(data=data, index = row)
print(df)

# 인덱스가 45보다 작은 값 중에서 널이 아닌 마지막 값. 아래는 컬럼이 주어지지 않아 모든 컬럼에 대해 수행
print(df.asof(where=45))
print(df.asof(where=30))


# where 리스트이면  각 요소이전의 결측치가 없는 마지막 행을 리턴
print(df.asof(where=[10,45,60]))
print(df.asof(where=[10,35,60]))


# subset을 활용하여 특정한 컬럼에만 적용. 결측치가 없는 컬럼 지정
print(df.asof(where=[10,35,60],subset='A'))
print(df)


# 인덱스가 시간일때
df = pd.DataFrame({'a': [10, 20, 30, 40, 50],
'b': [None, None, None, None, 500]},
index=pd.DatetimeIndex(['2018-02-27 09:01:00',
'2018-02-27 09:02:00',
'2018-02-27 09:03:00',
'2018-02-27 09:04:00',
'2018-02-27 09:05:00']))
print(df)

# 전체 컬럼을 대상으로 하기 때문에 값이 없음
ndf = df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
'2018-02-27 09:04:30']))
print(ndf)


# a 컬럼만 작용
df.asof(pd.DatetimeIndex(['2018-02-27 09:03:30',
'2018-02-27 09:04:30']),
subset=['a'])


########################################################
row = [10,20,30,40,50,60]
data = {'A':[1,None,None,4,5,6],'B':[7,8,9,10,None,12]}
df = pd.DataFrame(data=data, index = row)
print(df)

ndf = df.asof(where=30)
print(ndf)


# 이것도 역시 전체 컬럼 중에서 전체 다 Null이 아닌것 
ndf = df.asof(30)
print(ndf)


# 인덱스가 30보다 같거나 작은 B컬럼 중에서 값이 있는 최소 로우 
ndf = df.asof(where=30, subset='B')
print(ndf)
