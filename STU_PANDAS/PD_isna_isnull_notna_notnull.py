import pandas as pd
import numpy as np

"""
-isnull과 isna는 완전동일
-notnull과 notna는 완전동일
"""

col  = ['col1','col2','col3','col4']
row  = ['row1','row2','row3']
data = [[1,2,pd.NA,4],
        [np.nan,6,7,8],
        [9,10,11,None]]
df = pd.DataFrame(data,row,col)
print(df)
print()

################################################### 기본
print(df.isna())
print()

print(df.isnull())
print()

print(df.notna())
print()

print(df.notnull())
print()

################################################### 응용
print(df.isnull().values)
print()

# 행찾기
print(df[df['col1'].isna()])