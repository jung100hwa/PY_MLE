import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Dave','Ellen','Frank'],
                   'age': [24,42,18,68,24,57],
                   'state': ['NY','CA','CA','TX','CA','NY'],
                   'point': [64,24,70,70,88,57]}
                  )
print(df)

ndf = df.copy()

# 데이터 프레임차원(전체 값)의 replace
print('\n')
df.replace(57,56,inplace=True)
print(df)


# 특정컬럼만 바꾸기
print('\n')
df['age'].replace(24,19,inplace=True)
print(df)

# 여러개를 한번에 바꾸기
print('\n')
print(ndf)
print('\n')
ndf['name'].replace({'Alice':'jung1hwa', 'Bob':'jung2hwa'}, inplace=True)
print(ndf)

# 딕셔너리가 아닌 리스트로 개수를 맞추면 된다. 즉 'NY' -> 'AA', 'CA' -> 'BB' 이렇게 쉽게 적어야지
print('\n')
ndf['state'].replace(['NY','CA'],['AA','BB'], inplace=True)
print(ndf)


# 열거한 리스트의 값을 하나로 변경
print('\n')
ndf['state'].replace(['AA','BB','TX'],'CC', inplace=True)
print(ndf)

# 하나의 컬럼 뿐만아니라 여러 컬럼을 지정하는 방법
print('\n')
ndf.replace({'age':24, 'point':64}, 0, inplace=True)
print(ndf)


print('\n')
ndf.replace({'age':[0,42,18], 'state':['CC']}, 11, inplace=True)
print(ndf)


# 아래 예제는 na를 replace로 값 대체, fillna로 하는 것이 확실함
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,np.nan]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)

# 널을 이렇게도 처리가 가능하구나
# df['c4'].replace({np.nan : 100}, inplace=True)
df['c4'].replace(np.nan, 100, inplace=True)
print(df)


################################################## 25.03.13 추가
"""
그냥 문자열.replace 정규식이 안되는 것 같은데
판다스에서 제공하는 replace 정규식이 되는 것 같음
"""
df = pd.DataFrame({'aaa': ['Alice','Bob is 12old'],
                   'bbb': [24,42]}
                  )
print(df)

print("#" * 50)

df['aaa'] = df['aaa'].str.replace('[^a-zA-Z]', '', regex=True)
print(df)
