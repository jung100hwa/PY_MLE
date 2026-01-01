import numpy as np
import pandas as pd
import seaborn as sns

# 가장 많이 사용하지 않을까 하는 느낌이 든다.
# 마스크와 함께 가장 많이 사용할 것 같음

data = {"age": [10, 10, 21, 22], "weight": [20, 30, 60, 70]}
df = pd.DataFrame(data)
print(df)


# 비교 연산자 사용
print("=" * 20)
strQ = "age == 10"
ndf = df.query(strQ)
print(ndf)


# 위내용을 마스크로 표현
print("mask로 동일하게 표현")
mask = df.age  == 10
ndf = df.loc[mask]
print(ndf)


# in 연산자, 변수를 이용할려면 @를 붙여야 한다.
print("=" * 20)
aa = 10
bb = 21
strQ = "age in [@aa, @bb]"
ndf = df.query(strQ)
print(ndf)


# 논리 연산자, loc 같은 경우는 and, or이 아니고 & | 이다
print("=" * 20)
strQ = "(age == 10) and (weight == 20)"
ndf = df.query(strQ)
print(ndf)


# 마스크로 구현하면 항상 & | 일경우 ()를 사용해야 한다. 그렇치 않으면 엉뚱한 결과가 나온다.
print("=" * 20)
mask = (df['age'] == 10) & (df['weight'] == 20)
ndf = df.loc[mask]
print(ndf)


# 위와 같은 결과를 출력
mask = (df.age == 10) & (df.weight == 20)
ndf = df.loc[mask]
print(ndf)


# 외부 변수를 이용한 쿼리. 이부분이 가장 많이 사용될 것 같음
print("=" * 20)
aa = 21
bb = 60
strQ = "(age == @aa) and (weight == @bb)"
ndf = df.query(strQ)
print(ndf)

# TODO 사용자 점의 함수를 이용한 쿼리도 가능하다. 함수도 @를 사용
def add(a, b):
    return a + b

print("=" * 20)
aa = 20
bb = 1
strQ = "age ==@add(@aa, @bb)"
ndf = df.query(strQ)
print(ndf)


# 파이썬 내장 함수를 사용하면 오류가 난다네. 내장함수 인자가 정해져 있나??. 당연 오류날것 같은데
# print(df)
# strQ = "age == @max(21,20)"
# ndf = df.query(strQ)
# print(ndf)


# 파이썬 내장함수를 활용하기 위해서는 사용자 함수에서 사용해서 사용자 함수를 인자로 받는다.
def my_max(a,b):
    return max(a,b)

aa = 22
bb = 1
strQ = "age == @my_max(@aa, @bb)"
ndf = df.query(strQ)
print(ndf)
print(df)


# 행인덱스를 검색, 여기서 "index" 행인덱스를 말함, index는 키워드로 사용 됨
print("=" * 20)
strQ = "(index >= 2) and (age == 21)"
ndf = df.query(strQ)
print(ndf)


# todo 문자열 검색도 가능 함. 즉 query 짱
data = {"name": ["White tiger", "Black tiger", "Red tiger"], "age": [5, 7, 9]}
df = pd.DataFrame(data)
print(df)


# 문자열 검색. 여하튼 이 방법이 많이 사용될 듯 함.
print("=" * 20)
aa = 'tiger'
strQ = "name.str.contains(@aa)"
ndf = df.query(strQ)
print(ndf)


# 대소문자를 구분 없이
print("=" * 20)
aa = 'tiger'
strQ = "name.str.contains(@aa, case=False)"
ndf = df.query(strQ)
print(ndf)


# 특정문자열로 시작하는 로우 선택
print("=" * 20)
aa = 'Tiger'
strQ = "name.str.startswith(@aa)"
ndf = df.query(strQ)
print(ndf)


# 특정문자열로 끝나는 로우 선택
print("=" * 20)
aa = 'tiger'
strQ = "name.str.endswith(@aa)"
ndf = df.query(strQ)
print(ndf)
