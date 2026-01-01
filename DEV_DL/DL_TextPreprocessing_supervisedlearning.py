import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

values = [['당신에게 드리는 마지막 혜택!', 1],
['내일 뵐 수 있을지 확인 부탁드...', 0],
['도연씨. 잘 지내시죠? 오랜만입...', 0],
['(광고) AI로 주가를 예측할 수 있다!', 1]]
columns = ['메일 본문', '스팸 메일 유무']


print('\n====================>판다스를 이용한 데이터 분리')
df = pd.DataFrame(values, columns=columns)
print(df)

x=df['메일 본문']
y=df['스팸 메일 유무']
print(x)
print(y)

print('\n====================>넘파이를 이용한 데이터 분리')
ar = np.arange(0,16).reshape((4,4))
print(ar)

print('\n')
X=ar[:, :3]
print(X)

print('\n')
y=ar[:, 3]
print(y)

print('\n====================>사이럿킷을 이용한 테스트 데이터 분리')
x, y = np.arange(10).reshape((5, 2)), range(5)
print(x)
print(list(y)) #레이블 데이터

print('\n')

#3분의 1만 test 데이터로 지정.
#random_state 지정으로 인해 순서가 섞인 채로 훈련 데이터와 테스트 데이터가 나눠진다.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1234)
print(x_train)
print('\n')
print(x_test)


print('\n====================>수동으로 분리하는 방법')
import numpy as np
x, y = np.arange(0,24).reshape((12,2)), range(12)
# 실습을 위해 임의로 X와 y가 이미 분리 된 데이터를 생성
print(x)
print(list(y))

n_of_train = int(len(x) * 0.8) # 데이터의 전체 길이의 80%에 해당하는 길이값을 구한다.
n_of_test = int(len(x) - n_of_train) # 전체 길이에서 80%에 해당하는 길이를 뺀다.

print('\n===>훈련데이터와 테스트데이터 나눌 개수 구함')
print(n_of_train)
print(n_of_test)

print('\n===>훈련데이터와 테스트데이터 개수 만큼 분리')
x_test = x[n_of_train:] #전체 데이터 중에서 20%만큼 뒤의 데이터 저장
y_test = y[n_of_train:] #전체 데이터 중에서 20%만큼 뒤의 데이터 저장
x_train = x[:n_of_train] #전체 데이터 중에서 80%만큼 앞의 데이터 저장
y_train = y[:n_of_train] #전체 데이터 중에서 80%만큼 앞의 데이터 저장

print('\n===>x테스트 데이터')
print(x_test)

print('\n===>x훈련 데이터')
print(x_train)

print('\n===>y테스트 데이터')
print(list(y_test))

print('\n===>y훈련 데이터')
print(list(y_train))
