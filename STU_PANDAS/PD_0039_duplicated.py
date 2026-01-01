import pandas as pd
import seaborn as sns
import numpy as np

# NaN이 아닌 그냥 빈값이 있으면 정확한 비교가 되지 않는다.
# 가능하면 데이터가 필수인 컬럼을 지정해서 중복제거해야 한다.

df = pd.DataFrame({'c1' : ['a','a', 'b', 'a', 'a', 'c', 'c'],
                  'c2' : [1, 1, 1, 2, 1,1,1],
                   'c3' : [1, 1, 2, 2, 1,np.nan,np.nan]})
print(df.head(10))

#  현재행이 앞에 한번이라도 나오면 True 값, 전체행을 비교함
print('=' * 50)
print('중복데이터 조회')
print(df.duplicated())

#  시리즈에도 가능하다.
print('=' * 50)
print('시리즈에도 적용 가능')
test = pd.Series([3,1,2,1,2,2,3])
print(test)
print(test.duplicated())


# 시리즈에 가능하니 데이터프레임의 열에도 적용 가능. 이건 좀 쓸모가 있을 것 같다.
print('=' * 50)
print('데이터프레임의 열에 중복값 조회 적용')
print(df)
print(df.c2.duplicated())

# 아래와 같이 해도 된다. 이렇게 해도 되는 함수가 있고 subset 파라미터를 이용하는 함수가 있다.
print(df['c2'].duplicated())

# 중복데이터를 제거, True값을 제거, 이것도 쓸모가 많을 것 같음
ndf = df.copy()
print('=' * 50)
print('중복데이터를 제거')
print(df)
ndf2 = ndf.drop_duplicates()
print(ndf2)


ndf2 = df.copy()
ndf2['c4'] = '' # 여기서 c4 컬럼이 추가 되었구나
print(ndf2)
print('빈 컬럼을 포함한 중복데이터를 제거')
ndf2 = ndf2.drop_duplicates(subset=['c1','c4'])
print(ndf2)

# 전체 행의 값이 아닌 특정 열에 대한 행의 값 중복 제거
# 이럴 경우 지정한 컬럼의 첫번째 값만 남기고 나머지는 행은 삭제
ndf = df.copy()
print('=' * 50)
print('전체 행의 값이 아닌 지정한 컬럼값만 중복체크해서 제거')
print(ndf)

print('\n')
ndf2= ndf.drop_duplicates(subset=['c2','c3'])
print(ndf2)

# subset과 의미는 같으나 아래는 컬럼이 c2, c3만 나온다.
# 아래와 같은 방법은 주로 조회용으로 사용한다.
print('\n')
ndf = df.copy()
print(ndf[['c2','c3']].drop_duplicates())

# todo 이렇게 하자
print('\n')
ndf = df.copy()
print(ndf)
print(ndf.drop_duplicates(subset=['c2']))

# 아래는 컬럼이 하나이니 시리즈로 나오겠지
print('\n')
ndf = df.copy()
ndf2 = ndf['c2'].drop_duplicates()
print(ndf2)


df = pd.DataFrame({'c1' : ['a','a','a'],
                  'c2' : [1, 1, 3],
                   'c3' : [1, 2, 3]})
print(df)

print(df.drop_duplicates(subset=['c1','c2', 'c3']))


