
import pandas as pd

df = pd.DataFrame({'angles': [0, 3, 4],
'degrees': [360, 180, 360]},
index=['circle', 'triangle', 'rectangle'])

print(df)

# 단순하게 더하기
print(df +1)

# 함수로 사칙연산
print(df.add(1))
print(df.sub(10))
print(df.mul(10))
print(df.div(10))


# 사칙연산에 의해 첫번째 컬럼은 1을 연산 두번째 컬럼은 2를 연산한다.
# 이걸 조금 쓸 것 같은데 그닥. 컬럼마다 각각 더하면 되는거 아닌가
print(df)
print(df + [1,2])
print(df - [1,2])
print(df / [1,2])
print(df * [1,2])


# 위의 내용과 같음
print(df.add([1,2], axis='columns'))
print(df.sub([1,2], axis='columns'))
print(df.mul([1,2], axis='columns'))
print(df.div([1,2], axis='columns'))


# 데이터프레임간 사칙연산은 기본적으로 컬럼명이 같은 것끼리 계산한다.
# 컬럼명이 다르거나 없으면 널처리된다.
other = pd.DataFrame({'angles': [0, 3, 4]}, index=['circle', 'triangle', 'rectangle'])
print(other)
print(df.add(other))


# 존재하지 않은 컬럼은 fill_value로 채워서 계산하기, 계산결과가 아닌 피연산자를 대상에 맞춰서 행과열을 맞춘다.
print(df)
print(df.info())  # int타입
df_n = df.add(other, fill_value=0)
print(df_n)
print(df_n.info()) # float타입으로 자동 변경됨
 
print(df.add(other, fill_value=0))
print(df.mul(other, fill_value=0))


# 멀티인덱스 데이터 프레임과 계산
df_m = pd.DataFrame({'angles': [0, 3, 4, 4, 5, 6],
'degrees': [360, 180, 360, 360, 540, 720]},
index=[['A', 'A', 'A', 'B', 'B', 'B'],
['circle', 'triangle', 'rectangle',
'square', 'pentagon', 'hexagon']])


# level 인자를 이용한다. 항상 대칭되는 것만 계산. 즉 로우 인덱스가 같은 값끼리. 이렇게 까지 사용할 일은 없을듯
# 여기서는 circle, triangle, rectangle 만 계산
print(df)
print(df_m)
print(df.add(df_m, level=1, fill_value=0))


# 데이터프레임간 비교는 차집합의 개념이 아닌 대칭되는 값끼리 연산을 수행한다.
df_1 = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})
print(df_1)


df_2 = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [110, 50, -30, -50]
})
print(df_2)

df = df_1.sub(df_2)
print(df)
