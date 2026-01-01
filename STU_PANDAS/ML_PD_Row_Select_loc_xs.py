import numpy as np
import pandas as pd
import seaborn as sns

# 시리즈
s1 = pd.Series([100, 200, 300, 400, 500, 600], index=[
               ['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2]])
print(s1)
print(type(s1))

print('\n')
print(s1.loc['a'])

# 레벨이 다르기 때문에 loc로 아래와 같이 할 수 없다.
# print('\n')
# print(s1.loc[['a','1']])

# 인덱스를 출력해서 한행을 출력
print(s1.index)
print(s1.loc[('a',1)])


# 레벨이 같은 경우는 loc로 가능하다
print('\n')
print(s1.loc[['a', 'b']])


# 상위레벨 하나만 선택하는 방법. 3가지 방법이 있을 것 같음
print('\n')
print(s1.loc['a'])
print(s1['a'])          # 시리즈에서는 이게 가능하다. 컬럼명이 없으니
print(s1.xs('a'))


# xs를 이용해서 레벨이 다른 인덱스를 선택
print('\n')
print(s1.xs(('a', 1), level=[0, 1]))


# 아래와 같이 레벨이 없으면 하나의 값만 출력 됨
print(s1)
print(s1.xs(('a',1)))


# todo 행인덱스 레벨을 아래와 같이 지정할 수 있음. 이건 다른데서 써먹을만 하다.
print('\n')
print(s1)
print(s1.xs(2, level=1))


# 아래와 같이 슬라이싱 할 수 있다, 시리즈이니까 가능하다.
print('\n')
print(s1)
print(s1[:, 2])


# 데이터프레임
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head(5))


# todo 여기가 대박이네. query로 할때 컬럼명이 class이면 키워드로 인식해서 먹지 않음
# 그래서 아래와 같이 데이터프레임을 복사해서 컬럼명을 바꿔서 한번 해봄.*********************중요
df_str = df.copy()
df_str.columns=['age', 'sex', 'class_mod', 'fare', 'survived']
strq = "(class_mod=='First') and (sex=='female')"
print(df_str.query(strq))



# todo 중요 포인트. 피봇과 그룹의 차이점은 피봇은 자동으로 함수로 그룹핑된 값을 계산한다.
# 그룹은 말 그대로 하나의 그룹에 여러개의 요소들이 있다


# 지금부터는 컬럼에 적용해 보자
print('\n')
print(df.head(5))
gdf = pd.pivot_table(df,
                     index=['class', 'sex'],
                     columns='survived',
                     values=['age', 'fare'],
                     aggfunc='mean')
print(gdf)


print('\n')
print(gdf[('age',0)]['First'])   # 원래 단일 인덱스 일때는 안된다. 이런건 하지 말자
print(gdf[('age',0)].loc['First'])


print('\n')
print(gdf.loc['First', 'age'])


# 컬럼을 한번 조회하면 역시 튜플로 되어 있다.
print('\n')
print(gdf.columns)


# 즉 아래가 하나의 컬럼이다.
print('\n')
print(gdf[('age', 0)])


# 아래처럼 하면 하나의 값만 출력. 튜플 단위로 행과 열이 정의되기 때문에 아래처럼 가능하다.
print('\n')
print(gdf.loc[('First', 'female'), ('age', 0)])
print(gdf.loc[[('First', 'female'),('First', 'male')], ('age', 0)])

# xs로 바꾸어 보자, 컬럼이닌까 axis=1
print('\n')
print(gdf.xs(0, axis=1, level=1))


# loc는 반드시 행인덱스와 열인덱스로 잡혀 있어야 한다.
# 중요한 것은 다중인덱스, 다중열인덱스 일경우 행이든 열이든 순서대로 (,)에 적는다.
# 다중은 행, 열은 당연 슬라이싱은 안된다. 같은 행레벨, 열레벨이 안되기 때문에!!!
df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["a", "b", "c"],
                  columns=["A", "B", "C", "D"])
print(df)


# 시리즈로 출력
print('=' * 50, '\n')
print(df.loc['a'])


# 데이터 프레임으로 출력
print('=' * 50, '\n')
print(df.loc[['a']])


# 슬라이싱, 2개 이상일때는 무조건 데이터 프레임이니까. [[]] 할 필요가 없다
print('=' * 50, '\n')
print(df.loc['a':'b'])


# 배열로 할때는 슬라이싱이 아니라 각각 써주어야 한다. 슬라이싱이 아니라 선택의 의미이다.
print('=' * 50, '\n')
print(df.loc[['a', 'b']])

# todo 필터 또는 마스크, query() 함수도 비슷
print('=' * 50, '\n')
mask = (df.B == 15) | (df.B == 19)
print(df.loc[mask])


# 행과 열을 모두 받기
print('=' * 50, '\n')
print(df.loc['a':'c', 'A':'C'])


print('=' * 50, '\n')
print(df.loc[['a', 'c'], ['A', 'C']])


print('=' * 50, '\n')
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())


print('=' * 50, '\n')
ndf = pd.pivot_table(df,
                     index=['class', 'sex'],
                     columns='survived',
                     values=['age'],
                     aggfunc=['mean']) # todo ['mean'] 이렇게 하면 상위에 mean 컬럼이 생긴다.
print(ndf.head())
print('=' * 50, '\n')


# 역시 인덱스는 튜플로 되어 있다.
print(ndf.index)


# 다중인덱스 일경우에는 튜플로 지정해야 함
print(ndf.loc[('First', 'female')])


print('=' * 50, '\n')
print('컬럼도 마찬가지')
print(ndf.columns)
print(ndf.loc['First', ('mean', 'age')])

# 열이 3단계인데 마지막 단계까지 할려면 위에서부터 순서대로 해주면 된다.
print(ndf.loc['First', ('mean', 'age', 0)])


df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)


# 보통 컬럼을 추출해서 아래와 같이 사용
col_list = list(df.columns)
for item in col_list:
    print(item)


# 인덱스와 컬럼을 통한 for문으로 값 뽑아내기
row_list = list(df.index)
for ritem in row_list:
    for citem in col_list:
        print(df.loc[ritem,citem])

# 컬럼별 데이터 타입
print(df.dtypes)


# 데이터프레임이 비어있는지 확인
print(df.empty)


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
print(df)

# print(df.loc[pd.Index(["cobra", "viper"], name="foo")])
# print(df["shield"])

# 인덱스를 true/false, 아래는 인덱스가 0,1 것만 출력됨
# 짜증나네. 아래의 의미는 두번째 행만 출력하라는 의미. 각 행마다 다 이렇게 정의해야 함
print(df.loc[[False, True, False]])

# todo 조건문에 컬럼을 지정한다. 주로 컬럼에 대한 조건을 지정한다. sql도 마찬가지잖아
mask = df.shield > 6
print(df.loc[mask, 'shield'])
print(df.loc[mask]) # 행전체가 나온다.


# todo 마스크를 사용할 때는 and, or가 아니고 &, |을 사용해야 하고 반드시 ()로 묶어야 한다.
# todo query를 사용할 때는 and, or로 해야 한다.
# 마스크는 컬럼에만 되는게 아니고 행인텍스에도 적용 가능하다. 이렇게도 하는데 어떤 바보가 이렇게 하겠냐
print(df)
mask = df.index == 'cobra'
print(df.loc[mask])


# 가능은 하지만 행 인덱스를 이용하는 사람은 없다. 보통 테이블은 인덱스가 0, 1,2,3,....이렇게 나가는데.
mask = (df.index == 'viper') | (df.index == 'cobra')
print(df.loc[mask])


# 람다를 변수로 받아서 하는게 깔금하다.
mask = (lambda df: df.shield == 8)
print(df.loc[mask])


# 멀티인덱스
tuples = [
    ('cobra', 'mark i'), ('cobra', 'mark ii'),
    ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
    ('viper', 'mark ii'), ('viper', 'mark iii')
]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20],
          [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
print(df)


# values만, 넘파이 배열로만
print(df.values)


# 하나의 값으로 시리즈로 리턴
print(df.loc[('cobra', 'mark i')])


# 동일하게 데이터 프레임으로 할려면 [] 하나 더하면 된다.
print(df.loc[[('cobra', 'mark i')]])


############################################################ iloc함수를 이용한 접근
# 인덱스를 이용한 접근
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
{'a': 100, 'b': 200, 'c': 300, 'd': 400},
{'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

df = pd.DataFrame(mydict)
print(df)

# 행인덱스
print(df.iloc[0])       # 시리즈
print(df.iloc[[0]])     # 데이터프레임
print(df.iloc[0:2])     # todo 마지막값은 출력되지 않다. 인덱스일 경우에만

print(df.iloc[[False,False,True]])

# 이렇게는 조금 사용할 듯
im = df.iloc[lambda x : x.index % 2 == 0]
print(im)


# 행과 컬럼을 동시에 지정
print(df.iloc[[0],[0,1]])


# 슬라이싱 할 때는 별도 [] 하지 않아도 된다.
print(df.iloc[0:1,0:2])