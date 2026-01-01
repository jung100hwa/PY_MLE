# 각 컬럼마다 범위값으로만 세팅, 범위를 넘어서는 값은 최대값과 최소값으로 변경

import pandas as pd
import numpy as np

data = {'col_0': [9, -3, 0, -1, 5], 'col_1': [-2, -7, 6, 8, -5]}
df = pd.DataFrame(data)
print(df)

# 최소값 -4, 최대값 6으로 세팅, 범위를 넘어서면 -4, 6 으로 변경
ndf = df.clip(-4, 6)
print(ndf)

# 행마다 매치시키기 위해
lower_line = pd.Series([2, -4, -1, 6, 3])
upper_line = lower_line + 5
print(lower_line)
print(upper_line)

# https://blog.naver.com/PostView.nhn?blogId=youji4ever&logNo=222198720634 이사이트 참조하면 빠르고
# 각 행마다. 아래와 같이 하면 (2,7),(-4,1),(-1,4),(6,11),(3,8) 최소값과 최대값으로 df의 각행과 1:1로 매칭
print(df)
ndf = df.clip(lower_line, upper_line, axis=0)
print(ndf)

ndf['origine_a'] = df['col_0']
ndf['origine_b'] = df['col_1']
ndf['최소'] = lower_line
ndf['최대'] = upper_line

print(ndf)

t = pd.Series([2, -4, np.NaN, 6, 3])
print(t)

# 최소값만 정의할 수도 있음
print(df)
ndf = df.clip(t, axis=0)
print(ndf)

# 보통 이렇게 사용한다.
# ndf = df.copy()
# ndf.English[df.English >=600] = 600
# print(ndf)

################################################## 활용1
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)

mask = df.c0 == 1
df.loc[mask, 'c0'] = 100        # 해당되는 셀만 바꿈, 원래 이렇게도 가능했나???
df.loc[mask] = 100              # 해당되는 행 전체가 100으로 채워짐
print(df)

df.c0[df.c0 == 100] = 200       # 해당되는 셀만 바꿈
print(df)