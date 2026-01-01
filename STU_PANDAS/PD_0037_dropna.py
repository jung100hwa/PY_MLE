# 데이터프레임에 결측치가 있는 경우 처리
# 결측치 삭제, 다른 값으로 대체(평균, 이전값, 이후값 등)
# 결측치가 어디 행에 있는지 조회


# from typing_extensions import TypeVarTuple
from matplotlib.pyplot import axis
from tabulate import tabulate
import pandas as pd
import seaborn as sns
import numpy as np


df = sns.load_dataset('titanic')
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

# 정보확인
# 총 데이터 891개가 아닌 것은 결측치가 있다는 것
print('='*50)
print('기본정보 확인')
print(df.info())


# 데이터프레임 특정컬럼에 대한 고유값을 확인(dropna=False 옵션 주기)
print('='*50)
print('기본정보 확인')
print(df.deck.value_counts(dropna=False))   # 고유값의 개수까지
print(df.deck.unique())                     # 그냥 고유값만


# 가능하면 아래 방법이 나을 듯 하다. 괜히 혼동해서 쓰면 암기도 안됨
# print(df['deck'].value_counts(dropna=False))

# 결측치 탐색, 널이면 TRUE를 반환한다.
print('='*50)
print('결측치 탐색')
print(df.head(10).isnull())


# 결측치 함계, isnull은 결측치이면 True, True는 1로 계산됨
print('='*50)
print('결측치 합계')
print(df.isnull().sum()) # 컬럼단위로 계산(시리즈)


# 결측치가 하나라도 존재하는 값이 있으면 행삭제
print('='*50)
print('결측치가 하나라도 존재하면 그행 삭제')
ndf = df.copy()
print(df.info())
print(ndf.dropna().info())


# 결측치가 하나라도 존재하는 열삭제
# 결과는 컬럼 수가 줄어드는 것을 볼 수 있음
print('='*50)
print('결측치가 하나라도 존하면 열 삭제')
ndf = df.copy()
ndf.dropna(axis=1, inplace=True)
print('dropna 이후컬럼개수 : ' + str(len(ndf.columns)))
print('dropna 이전컬럼개수 : ' + str(len(df.columns)))


# 결측치가 500개 이상이면 삭제
print('='*50)
print('결측치가 500개 이상이면 열 삭제')
ndf = df.copy()

ndf.dropna(axis=1, thresh=500, inplace=True)

print('컬럼개수 : ' + str(len(df.columns)))
print('컬럼개수 : ' + str(len(ndf.columns)))


# 결측치가 있는 열과행에 대하여 any, all 옵션으로 삭제
# 주로 행에 대해서 한다.
print('='*50)
print('지정한 열에 대하여 결측치가 있는 행을 삭제')
ndf = df.copy()

# age열에 결측값이 1개라도 있으면 그 행을 삭제
print(df.info())
print('삭제전 : ', len(ndf))
print('삭제후 : ', len(ndf.dropna(subset=['age'], how='any', axis=0)))
print('삭제후 : ', len(ndf.dropna(subset=['age','deck'], how='any', axis=0)))

############################################## 결측치 테스트
# 빈값은 결측치가 아니다. 그리고 subset은 "or" 성격을 가진다.
# isnull은 결측치를 조사하는 함수이다. 빈값은 false나온다. 즉 결측치가 아니라고 나온다.
ndf = pd.DataFrame([[1, '', 3],[4, 5, 6],[7, 8, np.nan],[np.nan, 10, 11]],
                  columns=['A', 'B', 'C'])
print(ndf)
print(ndf.isnull())
n_ndf = ndf.dropna(subset=['A','C'], how='any', axis=0)
print(n_ndf)
##############################################

# 결측치를 다른 값으로 대체
print('=' * 50)
print('결측치를 다른 값으로 대체')
ndf = df.copy()
print(ndf)
print('age 결측치 총개수 :', ndf.age.isnull().sum())


ndf.age.fillna(ndf.age.mean(),inplace=True)
print('age 결측치 총개수 :', ndf.age.isnull().sum())


# 결측치가 어느 행에 있는지 인덱스를 이용한 찾기
print('=' * 50)
print('결측치가 있는 행을 찾자')
ndf = df.copy()
print(ndf.head(5))
print('결측치 개수 확인 : ', ndf.embark_town.isnull().sum())


# 아래 코드를 유심히 봐야 함. 인덱스 구하는 공식. False:0, True:1이니까
# 이코드 대박이다. 머리가 아주 좋다. 누가 시작했는지. 즉 해당열의 참인 값에 대한 인덱스번호 출력
print('결측치가 존재하는 인덱스 : ', ndf.index[ndf.embark_town.isnull()])
print(ndf.embark_town.isnull())
# print(ndf.index[1])

# # 61, 829 행에 결측치가 존재하는 확인
# print(ndf.loc[[61, 829]])

print('=' * 50)
print('결측치를 최빈값으로 대체')
print(ndf.embark_town.value_counts(dropna=True))
print(ndf.embark_town.value_counts(dropna=False))
print(ndf.embark_town.unique()) # 값만 나옴


# 고유값의 개수를 구하고 최빈값을 대체
# 여기서 인덱스 곧 값을 얘기함(두줄이닌까)
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))
print(df.embark_town.value_counts(dropna=True).idxmax())
# print(df.embark_town.value_counts(dropna=True))

dd = df.embark_town.value_counts(dropna=True).idxmax()

# 널이었던 인덱스 61, 829가 채워짐
print(tabulate(ndf.loc[[61, 829]], headers='keys', tablefmt='simple_outline'))
ndf.embark_town.fillna(dd, inplace=True)
print(tabulate(ndf.loc[[61, 829]], headers='keys', tablefmt='simple_outline'))


# 결측치를 이웃값으로 대체
print('=' * 50)
print('결측치를 바로 이전 이후 값으로 대체')
ndf = df.copy()
print(ndf.loc[[60, 61, 62, 827, 828, 829, 830]])


print('바로이전값으로 대체') # 827, 828 데이터를 확인
ndf.fillna(method='ffill', inplace=True)
print(ndf.loc[[60, 61, 62, 827, 828, 829, 830]])

print('바로이후값으로 대체')
ndf = df.copy()
ndf.fillna(method='bfill', inplace=True)
print(ndf.loc[[60, 61, 62, 828, 829, 830]])


df = sns.load_dataset('titanic')
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

# deck 하나라도 널이 있으면 삭제
df.dropna(subset=['deck'], how='any', axis=0, inplace=True)
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))



exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}


df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))


# 컬럼 삭제
ndf = df.copy()
print('\n')
print('컬럼삭제')
ndf.drop(['수학'], axis=1, inplace=True)
print(ndf)

# 행 삭제
ndf = df.copy()
print('\n')
print('행삭제')
ndf.drop(['서준'], axis=0, inplace=True)
print(ndf)


exam_data = {'수학' : [ 90, np.nan, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))


# 컬럼을 삭제(nan)
ndf = df.copy()
print('\n')
print('컬럼삭제')
# 우현이라는 행에 널이 하나라도 있는 컬럼 삭제
ndf.dropna(subset=['우현'], how='any', axis=1, inplace=True)
print(ndf)


# 행을 삭제(nan)
ndf = df.copy()
print('\n')
print('행삭제')
# 수학이라는 컬럼에 널이 있는 행은 삭제
ndf.dropna(subset=['수학'], how='any', axis=0, inplace=True)
print(ndf)

print('\n')
ndf = df[:]
print(ndf)

# 아래 방식으로 하면 절대 안됨
ndf2 = ndf['수학'].dropna(inplace=True)
print(ndf2)

############################################################################ 빈값을 nan으로 대체
ndf = pd.DataFrame([[1, '', 3],[4, 5, 6],[7, 8, np.nan],[np.nan, 10, 11]],
                  columns=['A', 'B', 'C'])
print(ndf)

ndf['B'] = pd.to_numeric(ndf['B'], errors='coerce')
print(ndf)


ndf = pd.DataFrame([[1, '', 3],[4, 5, 6],[7, 8, np.nan],[np.nan, 10, 11]],
                  columns=['A', 'B', 'C'])
print(ndf)
ndf['B'].replace('',np.nan, inplace=True)
print(ndf)
