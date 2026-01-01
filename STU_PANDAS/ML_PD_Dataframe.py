import pandas as pd
import numpy as np
# from numpy import reshape

# 딕셔너리를 시리즈로 변경
dict_data = {'aa':11, 'bb':22, 'cc':33}
sr = pd.Series(dict_data)
print(sr)


# 딕셔너리를 데이터 프레임으로 변경, 여기서 인덱스는 좌측 행인덱스
# 딕셔너리 키에 해당하는 값의 구조가 같아야 한다. 아래는 모두 3개
df = pd.DataFrame(
    {"a": [4, 5, 6, np.nan],
     "b": [7, 8, 9, 10],
     "c": [10, 11, 12,13]},
    index=[1, 2, 3,4]
)
print(df)

aadf = df.iloc[1:3]
print(aadf)


#####################################################
print(df['a'].nunique())     # 널값을 계산하지 않는다
print(len(df['a'].unique())) # 널값을 계산한다.
print(df['a'].unique())
#####################################################

# 무작위로 추출하는데 1을 주면 무작위 섞는 효과가 발생 함
sss = df.sample(frac=1)
print(sss)


# 리스트를 시리즈로 변환, 행인덱스가 명시되지 않으면 0,1,3..순차적으로 매겨진다.
list_data = ["aaa", "bbb", "ccc"]
sr = pd.Series(list_data)
print(sr)


# 아래 같은 경우도 하나의 값으로 본다. 리스트 자체를 하나의 값으로 처리
list_data = [['a','b','c'], ['aa','bb','cc']]
sr = pd.Series(list_data)
print(sr)


# 리스트를 데이터프레임으로 변환. 시리즈는 하나열밖에 없기 때문에 리스트 자체를 값으로 처리함.
# todoo 이런 형태가 딥러닝의 전부다. 꼭 알아두어야 한다.
list_data = [['a','b','c'], ['aa','bb','cc']]
df = pd.DataFrame(list_data, index=[1,2], columns=['col1', 'col2', 'col3'])
print(df)


df = pd.DataFrame(data=list_data,  columns=['col1', 'col2', 'col3'])
print(df)

# 인덱스를 1번부터 시작
df = pd.DataFrame(data=list_data,  index=np.arange(1, len(list_data) + 1), columns=['col1', 'col2', 'col3'])
print(df)


# 튜플을 시리즈로 변환
tu_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tu_data, index=['이름','생년월일','성별','학생여부'])
print(sr)


# 튜플을 데이터프레임으로 변환
# 이것도 마찬가지로 딥러닝에서 많이 사용한다.
tu_data = (('a','b','c'), ('aa','bb','cc'))
df = pd.DataFrame(tu_data, index=[1,2], columns=['c011', 'col2', 'col3'])
print(df)


# 넘파이를 이용한 데이터 프레임 생성, 보통이렇게 많이한다.
# list_data = [[1,2,3,4], [5,6,7,8]]
num = np.array(range(20)).reshape(5,4)
df = pd.DataFrame(num, index=[1,2,3,4,5], columns=['col1', 'col2', 'col3', 'col4'])
print(df)