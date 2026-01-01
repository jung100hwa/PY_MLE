import pandas as pd
import seaborn as sns
from tabulate import tabulate


# 엑셀의 피봇과 동일. 그룹핑 개념
df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))


ndf = pd.pivot_table(df,                 # 피벗할 데이터프레임
                     index = 'class',    # 행 위치에 들어갈 열(자동 그룹화 한다)
                     columns = 'sex',    # 열 위치에 들어갈 열(그룹핑한 데이터를 구분하는 기준)
                     values = 'age',     # 데이터로 사용할 열(집계함수에서 사용할 값정도)
                     aggfunc = 'mean')   # 데이터 집계함수


print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))


ndf = pd.pivot_table(df,                         # 피벗할 데이터프레임
                     index = 'class',            # 행 위치에 들어갈 열
                     columns = 'sex',            # 열 위치에 들어갈 열
                     values = 'survived',        # 데이터로 사용할 열
                     aggfunc = ['mean', 'sum'])  # 데이터 집계함수

print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))


ndf = pd.pivot_table(df,
                     index = ['class','sex'],   # 항상 이것으로 그룹핑이 자동
                     columns = 'survived',      # 열 위치에 들어갈 열
                     values = ['age','fare'],   # 하나 일때는 열에 포함이 되지 않지만 2개 이상이면 들어감(상식)
                     aggfunc = ['mean','max'])

print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))


#  멀티 인덱스 기준으로 그룹
print("=" * 70)
print(df.head())
grouped = df.groupby(['class','sex'], observed=False)
gdf = grouped.mean()
print(gdf)


# 아래와 같이 두개 이상이면 무조건 데이터 프레임이다.
# 피봇을 만들때 index으로 설정을 했기 때문에 loc로 할수가 있는 것이다.
print("=" * 70)
print(gdf.loc['First'])


# 아래와 같이 한컬럼 일경우 이것은 시리즈이다.
# 그리고 멀티 인덱스 일 경우 아래와 같이[()] 이런형태로 적어야 한다.[[]] 아니다.
print("=" * 70)
print(gdf.loc[('First','female')])
print(gdf.loc[[('First','female'),('First','male')]]) # loc는 항상 이렇게 한다.


# 멀티 인덱스에서 조건에 맞게 추출, loc로 표현이 불가능한 경우
print("=" * 70)
print(gdf)
print(gdf.xs('male', level='sex'))
print(gdf.xs('First',level='class'))


# 인덱스를 초기화 하자.
print("=" * 70)
print(gdf.reset_index());


# 컬럼이 멀티 인덱스인 경우. 가독성이 떨어지는 것 같다. 상단에 명시한게 낫다.
# 그리고 먼저 다 구해놓고 컬럼만 추출하는 것은 성능상 바보 같은 짓이다.
print("=" * 70)
print(tabulate(df, headers='keys', tablefmt='simple_outline'))

print(df.info())


# 아래는  mean은 수행되지 않는다. category 타입이 있다.
# gdf2 = df.groupby('class').agg(['mean','max'])[['age','fare']]

gdf2 = df.groupby('class').agg(['min','max'])[['age','fare']]
print(tabulate(gdf2, headers='keys', tablefmt='simple_outline'))


################################# 추가. 위의 내용과 동일하게 작성. 위의 내용은 가독성이 떨어짐
gdf22 = df.groupby('class')
gdf22 = gdf22.agg(['max','min'])
# gdf22 = gdf22.agg(['max','mean'])
gdf22 = gdf22[['age','fare']]
print(gdf22)


# 컬럼이 멀티인덱스 일때 이중 구조를 하나의 행으로 만들기
# 개수를 순차적으로 적용한 것 뿐
print("=" * 70)
gdf2.columns = ['age_mean','age_max','fare_mean','fare_max']
print(gdf2)


# 멀티 피벗 테이블 응용
print(df.head())
print("=" * 70)
gdf3 = pd.pivot_table(df,
                     index = ['class','sex'],
                     columns = 'survived',
                     values = ['age','fare'],
                     aggfunc = ['mean','max'])

print(tabulate(gdf3, headers='keys', tablefmt='simple_outline'))

# 인덱스로 잡혀 있기 때문에 아래가 가능하다.
print("=" * 70)
print(gdf3.loc['First'])

print("=" * 70)
print(gdf3.xs('male',level='sex'))


# 위에 동일하게 조회
print("=" * 70)
print(gdf3.xs('male',level=1))


# 행인덱스를 좀더 상세하게
# 피벗으로 구한 값들을 좀더 범위를 좁혀 간다고 생각하면 됨
print("=" * 70)
print(gdf3)
print(gdf3.xs(('Second','male'), level=[0,1]))

# level 안주면 시리즈 형태로 출력
print("=" * 70)
print(gdf3.xs(('First','female')))


# 컬럼에 대한 인덱싱
print("=" * 70)
print(gdf3.xs('mean', axis=1))


# 컬럼(!!!컬럼이 중요, axis=1이기 때문) 에 대한 멀티 인덱싱
print("=" * 70)
print(gdf3.columns)
print(gdf3.xs(('mean'), axis=1))
print(gdf3.xs(('mean','age'), axis=1))



# 추가적으로 연습했던 항목
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())



# 행, 열, 값, 집계에 사용할 열 지정
print('\n')
pdf1 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='age',
                      aggfunc='mean')
print(pdf1.head())


pdf2 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='survived',
                      aggfunc=['mean', 'sum'])
print(pdf2.head())
print(tabulate(pdf2, headers='keys', tablefmt='simple_outline'))



gdf3 = pd.pivot_table(df,

                      index=['class','sex'],
                      columns='survived',
                      values=['age','fare'],
                      aggfunc=['mean', 'sum'])
print(gdf3.head())
print(tabulate(gdf3, headers='keys', tablefmt='simple_outline'))


# xs 인덱스는 기본적으로 axix =0 즉 행인덱스를 사용한다.
print(gdf3.xs('First'))


# 행인덱스를 2개 지정하면 시리즈 행태로 출력된다. 한줄에 쪽 펼칠수가 없으니까
# 여하튼 판다스에서 행이 하나면 무조건 시리즈로 출력된다는 것만 알면 된다.
# 향후에는 아래와 같은 표현은 사라지니. "key" 키워드를 사용해야 한다.
# print(gdf3.index)
print(gdf3.xs(('First','female')))

# 행인덱스 중에서 조건을 주어서 출력, level로 수행
print(gdf3.xs('male', level='sex')) # 행인덱스 sex 중에서 male 것만 출력

print('\n')
print(gdf3.xs(('Second','male'), level=['class', 'sex'])) # class에서 Second만, sex에서 male만 조회

print('\n')
print(gdf3.xs(('Second','male'), level=[0, 1]))           # 위에와 동일한 쿼리, 단지 행인덱스로 접근(순서대로 0, 1, 2---)

# 그런데 컬럼을 가지고 올때는 ()으로 해야 되네
print('\n')
print(gdf3)

print('\n')
print(gdf3.xs(('Second','female'), level=[0, 1]))

# 위의 쿼리와 동일하다. 미래버전에서 없어질 것 같다고 하니 아래와 같이 리스트 형식은 사용하지 말자
print(gdf3.xs(['Second','female'], level=[0, 1]))


# 원하는 열만 가져오기
print('\n')
print(gdf3.xs(('mean', 'age'), axis=1))

# 컬럼을 찍어보면 튜플 형태로 되어 있다.
print(gdf3.columns)

# 아래와 같이 하면 안됨
# print(gdf3.xs(['mean', 'age', 0], axis=1))

# 컬럼도 원하는 것만 가져오기, 열인덱스를 사용한다.
print(gdf3.xs(1, level='survived', axis=1))

# 행인덱스와 마찬가지로 열인덱스로 가져온다.
# 행과 달리 열이름이 없는 경우가 있기 때문에 인덱스로 가져오는게 맞다.
print(gdf3.xs(('mean','fare',0), level=[0, 1, 2], axis=1))