import pandas as pd
import numpy as np

# argsort를 이용한 배열 정렬 기능

s = pd.Series([-1.10, 2, -3.33, 4])
print(s.abs())

df = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})

print(df)

# 아래 내용 코딩 참조
###################
s = (df.c - 49)
print(s)


s = s.abs()
print(s)
###################

print((df.c-49).abs().argsort())


a = np.array([1.5, 0.2, 4.2, 2.5])
s = a.argsort()  # 정렬의 인덱스를 반환한다.

# s는 정렬을 위한 인덱스. 정렬을 이렇게 하는 구나
print(s)
print(a[s])

# 내림차순
a = np.array([1.5, 0.2, 4.2, 2.5])
s = a.argsort()

print(a)
print(s) # 인덱스를 반환
print(a[s])
print(a[s][::-1])

###################################### 위에 코드가 이런 의미임
alist = [2, 1, 3, 4] # 리스트값
alistindex = [1, 0, 2, 3] # alist 인덱스값을 어느 인덱스부터 출력할 것인가.
print(a[alistindex]) # 결국 이러면 오름차순이 됨
######################################

# 내림차순시 보통 이렇게 한다. 위에 방법은 너무 복잡함
s2 = (-a).argsort()
print(s2)
print(a[s2])


a = np.array([-5, 3, 2, -2])
s = a.argsort()
print(s)
print(a[s])


df = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})

print(df)
print(df['c'])
s = df['c'].argsort()
print(s)

# 특정컬럼을 기준으로 오름차순..음 좋구만
print(df.loc[s])
print(df.loc[df.c.argsort()])