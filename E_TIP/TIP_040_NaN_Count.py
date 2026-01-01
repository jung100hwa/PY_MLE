 # 결측치를 계산하는 방법은 많은 아래는 방법은 정말 쇼킹
 # 파이썬은 False는 0, True는 1롤 처리한다. 그리고 NaN는 널로 인식한다.
 # isnull()이라는 함수를 이용해서 컬럼단위로 NaN 개수를 구해보자

import pandas as pd
import numpy as np

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ np.nan, np.nan, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

# 하나의 컬럼에 대해 유니크한 값의 개수
print(df['체육'].value_counts(dropna=False))


# 이렇게도 가능. 컬럼값이 문자일 경우 이렇게 가능한줄 알고 있음
print(df.체육.value_counts(dropna=False))


# 아래는 하나의 행의 개수를 구하는 것이다. 중복되지 않았으면 무조건 1
print("#" * 100)
print(df.value_counts(dropna=False))


######################## isnull을 이용한 컬럼별 NaN의 개수
num = df.isnull().sum()
print(num)

######################## NaN이 있는 행의 인덱스를 구함
print(df.index[df['체육'].isnull()])