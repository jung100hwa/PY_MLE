# 옷의 지퍼를 올리듯 쌍으로 만들어 준다.
import os

os.chdir(r"c:\\projects\\PY_MLE")

import pandas as pd


numbers = [1, 2, 3]
letters = ["A", "B", "C"]


###################################### 순차적으로 쌍으로 만든다.
for pair in zip(numbers, letters):
    print(pair)


# 받는 인자의 개수로 나누어서..(파이썬의 기본 기능)
print("#" * 50)
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)


# 여기는 통으로 하나 터플로 받음
print("\n")
for tot in zip("12345", "ABCDE", "abcde"):
    print(tot)


# 아래 pairs는 zip 타입이기 때문에 바로 출력 불가, for 문으로 해야 함
print("\n")
pairs = zip(numbers, letters)
print(pairs)


# 리스트형으로 전환후 출력
print("\n")
pairs = list(zip(numbers, letters))
print(pairs)


###################################### * 붙으면 반대 작업
print("\n")
numbers, letters = zip(*pairs)
print(numbers)
print(letters)


# 무조건 튜플형태로 리턴함
print("\n")
pairs = zip(numbers, letters)
numbers, lettes = zip(*pairs)
print(numbers)
print(lettes)


####################################### zip 함수를 이용하는 최고의 방법
# 데이터프레임에서 원하는 컬럼만 불러오기

df = pd.read_excel("E_FILE\서울지역 대학교 위치.xlsx", index_col=0)
print(df)

#  컬럼이 많을 경우 원하는 컬럼으로 하나의 이터레이터를 생성
for name, x, y in zip(df.index, df.위도, df.경도):
    print(name, x, y)

for info in zip(df.index, df.위도, df.경도):
    print(info)


# 터블이 아닌 딕셔너리로 만들 수 있음. 원리 dict,list, tupple 등은 상호 변환이 가능함
keys = [1, 2, 3]
values = ["A", "B", "C"]

dic = dict(zip(keys, values))
print(dic)
