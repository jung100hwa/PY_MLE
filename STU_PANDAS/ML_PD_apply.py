# 각 시리즈 객체에 사용자 정의 함수 매핑
# apply가 다양한 형태로 입력값을 받아 다양한 형태로 출력하기 때문에 가장 많이 사용한다.
# 그외 applymap(), pipe() 함수가 있는데 모두 apply() 가능하다.
# map => 시리즈만 사용 이 말은 데이터프레임에 컬럼단위로만 한다는 것, applymap => 데이터프레임, apply => 시리즈, 데이터프레임
# 그리고 map 파이썬 기본 함수 말고 데이터프레임에서 제공하는 하는 함수를 말함

import numpy as np
import seaborn as sns
import pandas as pd

def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b


def missing_value(series):
    return series.isnull()

def min_max(x):
    return x.max() - x.min()

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare','class']]
print(df.head(5))


# 첫번째 인자는 시리즈 자체의 값이 적용된다.
sr1 = df['age'].apply('max')
print(sr1)

# 각 행마다 수행된다.
sr1 = df['age'].apply(add_10)
print(sr1)


# 사용자 정의함수에서 그룹이 아닌이상 이렇게 하면 오류난다.
# 왜냐하면 class가 문자이기 때문이다. 원래 문자도 max, min 되는데 이 함수는 max-min 연산을 하니까 오류가 나는 것
# 아래와 같이 컬럼명을 지정하지 않으면 모든 컬럼에 대해서 수행한다.
# sr1 = df.apply(min_max)
# print(sr1)

# agg 함수도 똑 같네. 이건 알아서 한다고 하더니
# sr1 = df.agg(min_max)
# print(sr1)


# 이렇게 하면 오류가 발생하지 않는다. 그리고 시리즈(열)별로 계산된다.
# 당연히 숫자만 있으니 오류가 나지 않지
ndf = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})
print(ndf)

sr1 = ndf.apply(min_max)
print(sr1)

s1 = ndf.agg(min_max)
print(s1)

# 아래와 같이 하면 오류가 발생한다. class 컬럼은 숫자가 아니기 때문이다.
# ndf = df.apply(add_10)


# 계산 가능한 것만 선택해야 한다. 이때 agg 함수를 쓰면 편하다. agg 함수도 똑같은데....
# df만 하면 전체 데이터프레임에 적용된다. 첫번째 인자는 데이터프레임 자체의 값이 된다.
ndf = df.loc[:, ['age','fare']]
print(ndf.head())
print(ndf.apply(add_10))


# 숫자만 있으니까 가능하다.
sr1 = ndf.apply(min_max)
print(sr1)


# 즉 여기서도 a인자는 age값이 된다. TODO 결국 첫번째 인자는 컬럼값이 된다.
sr2 = df['age'].apply(add_two_obj, b=20)
print(sr2)


# 시리즈를 데이터프레임으로 변환
# ndf = pd.DataFrame(sr1)     # columns 속성을 주면 안됨, 이미 시리즈에 있음
# ndf.rename({'age':'age1'}, axis=1, inplace=True)
# ndf['age2'] = sr2
# ndf['age3'] = sr3

# 한꺼번에 3개의 시리즈를 딕셔너리로 만들어서 추가
# series = {'one':sr1, 'two':sr2, 'three':sr3}
# ndf = pd.DataFrame(series)

# 이 방법이 가장 나은 것 같네
# ndf = pd.DataFrame()
# ndf['age1'] = sr1
# ndf['age2'] = sr2
# ndf['age3'] = sr3


# axis = 0이면 열단위로 계산한다. 예를 들면 합계를 구할때 열단위 합계
# axis = 1이면 행단위로 계산한다. 예들 들면 합계를 구할때 행단위 합계
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data, index=['a','b','c'])
print(df)

print('\n 컬럼별 적용')
print(df.apply(np.sum, axis=0))


print('\n 행별 적용')
print(df.apply(np.sum, axis=1))


##################################################### 여기서 부터는 result_type을 위한 것
# 아래가 df의 기본이 된다.
# 기본프레임
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df)


# 컬럼인덱스 자동 확장(0,1,2.3....), result_type을 broadcast로 하면 오류 난다.
# 왜냐하면 컬럼이 'A', 'B' 2개로 상단에 정의를 했기 때문
ndf = df.apply(lambda x: [11, 22, 33, 44], axis=1, result_type='expand')
print(type(ndf))
print(ndf)


# broadcast 옵션은 기반데이터프레임 데이터 값과 일치하는 것을 보장한다.
# 아마도 최초 데이터 타입과 일치하도록 자동 변경한다. 대신 실수->정수 이렇게 한다.
# 문자를 정수나 실수로 변경할 수 없다.
# 조건이 없으니까 아래는 무조건 실행

# x 대신에 리스트 자체를 삽입
ndf = df.apply(lambda x: ['a', 2], axis=1)
print(type(ndf))
print(ndf)


# x 대신에 값으로 대체
ndf = df.apply(lambda x: ['a', 2], axis=1, result_type='expand')
print(type(ndf))
print(ndf)

# 정수가 아닌 실수를 했을 경우 => 타입을 정수로 변경
ndf = df.apply(lambda x: [1.0, 2.0], axis=1, result_type='broadcast')
print(ndf)

# 아래과 같은 경우는 오류. 문자열 변경이 안됨. 최초 컬럼과 
ndf = df.apply(lambda x: ['a', 2], axis=1, result_type='broadcast')
print(ndf)
# ##############################################################################여기까지


# 보통은 컬럼이나 인덱스별로 적용을 하는데 각 요소별로 접근하고자 할 때
df = pd.DataFrame([[1, 2.12], [3.356, 4.567]], columns=['a','b'])
print(df)

# 각 요소별로 100을 더했음
ndf = df.apply(lambda x: x + 100)
print(ndf)


# 아래 함수는 쓰지 않는게 맞다.
# ndf = df.applymap(lambda x: x + 100)
# print(ndf)


# 이렇게 단순 존재하는 함수를 쓸 때에는 그냥 연산을 하는 것이 훨씬 낫다. 판다스에서도 이렇게 추천한다.
ndf = df + 100
print(ndf)

# 구조가 같기 때문이다.
ndf = df + (df * 0.1)
print(ndf)


# 각 요소별로 길이를 구하고자 할 때 이럴때에는 applymap() 함수를 사용해야 한다.(앞으로 없어질 함수. 쓰지 말자. TODO 그냥 map 함수를 쓰자)
# 즉 apply는 로우와 컬럼단위 접근이고, applymap는 개별원소 접근인데 단순계산할 때는 차이가 없다.
# todo 단지 차이가 있을 때는 각 개별요소의 길이를 구할 때. apply는 로우전체의 길이, applymap은 각 개별요소의 길이
# 이거 하나 차이가 있는 듯
# 아래는 이해되지 않은 결과값이 출력된다.
# 중요 lambda 함수를 사용할 때 x의 변수가 apply는 시리즈이다. 그리고 applymap은 개별 요소이다. 단순덧셈일 때는 시리즈 + 100을 해도 시리즈 내부요소에 자동으로 100을 더하기 때문
# 그런데 x자체의 길이를 구할 때는 얘기는 틀려진다.
print(df)
ndf = df.apply(lambda x: len(str(x)))
print(ndf)

# 아래가 원하는 값이다.
print(df) 
ndf = df.applymap(lambda x : len(str(x)))
print(ndf)


# 앞으로는 applymap은 사용하지 말고 아래 함수만 쓰자
print(df) 
ndf = df.map(lambda x : len(str(x)))
print(ndf)


# 테스트
print(len(str(1.000)))


# 함수를 요소별도 적용할 때 na값은 무시할 수 있다.
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, np.nan]}
df = pd.DataFrame(exam_data, index=['a','b','c'])
print(df)

# 널인것은 계산하지 않는다. 이게 옵션인지 모르겠네 어차피 널은 무슨 계산을 하든 널이지.
ndf = df.applymap(lambda x : x + (x * 0.1), na_action ='ignore')
print(ndf)


ndf = df.map(lambda x : x + (x * 0.1), na_action ='ignore')
print(ndf)


# applymap이 옵션을 더 가지고 있는 듯 한데 결국 apply를 쓰는게 나을 듯 하다.
ndf = df.apply(lambda x : x + (x * 0.1))
print(ndf)


# 단순계산은 그냥 데이터프레임 연산으로 하는게 낫다. 위에 처럼 하지 말고
ndf = df + (df * 0.1)
print(ndf)

################################################### 업그레이드
# group by를 참고하시라