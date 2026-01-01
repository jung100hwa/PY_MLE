# 라이브러리 불러오기
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
from tabulate import tabulate

# read_csv() 함수로 df 생성
df = pd.read_csv('./E_FILE/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

print(df.dtypes)
print('\n')

# 문자열을 nan으로 바꾼다음 dropna로 행을 삭제
print(df['horsepower'].unique())
print('\n')


# 1.문자열을 nan 처리하고
df['horsepower'].replace('?', np.nan, inplace=True)
print(df['horsepower'].unique())
print('\n')


# 2.nan을 삭제
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))
print(df['horsepower'].unique())
print(df.dtypes)
print('\n')


################## 예제 2번째
print(df.head())

df['origin'].replace({1:'KOR', 2:'EU', 3:'US'}, inplace=True)   # 바꾸는 방법
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))
print(df['origin'].unique())
print('\n')


# 범주형으로 변환
df['origin'] = df['origin'].astype('category')
print(df.dtypes)
print('\n')


################## 예제 3번째
print(tabulate(df, headers='keys', tablefmt='simple_outline'))
print(df['model year'].sample(3))
print('\n')

df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
print('\n')



################## 예제 4번째(정해진 카테고리만 기존 값을 바꾸고 없는 값은 NaN)
ser = pd.Series([1, 2, 3, 4], dtype='int32')
print(ser)

cat_dtype = CategoricalDtype(
    categories=[1, 2], ordered=False) # ordered의 의미는 모름
new_ser = ser.astype(cat_dtype)
print(new_ser)


################## 예제 5번째 : copy=False 이면 원본데이터 값도 바뀜 즉 s2를 변경하면 s1도 바뀜
# 이렇게 사용할 일이 없다. 그냥 넘어가자. 나중에 기억이나 나겠다.
# 타입이 같아야 함
s1 = pd.Series([1, 2])
s2 = s1.astype('int32', copy=False)
print(s1)       # type : int64
print(s2)       # type : int32

# copy = False임에도 s2시리즈 값을 바꾸어도 s1 값이 바뀌지 않음. 타입이 int64 -> int32이기때문 
s2[0] = 10.0
print(s2)
print(s1)

# 아래는 원본 값이 바뀜
s2 = s1.astype('int64', copy=False)
print(s1)
print(s2)

s2[0] = 20.0
print(s2)
print(s1)