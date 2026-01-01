"""
지도 학습을 잘 되는지 평가. 여기서는 and or xor이라고 했지만 라벨값이 이미 정해져 있고
라벨값을 이용해서 학습 상태를 보는 것
"""
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

# sigmoid 함수 정의
def sigmoid(x):
    return 1/(1 + np.exp(-x))

######################################################## and gate
print("=========================and gate")
x = np.array([[1,1],[0,1],[1,0],[0,0]])
y = np.array([[1],[0],[0],[0]])

w = tf.random.normal([2], 0, 1)
b = tf.random.normal([1], 0, 1)

b_x = 1 # 바이어스도 똑 같이 업데이트 해주기 위해서 아래 코드 참조

for i in range(2000):
    loss_sum = 0

    for j in range(4):
        output = sigmoid(np.sum(x[j]*w)+b_x+b) # 행렬 곱한것을 하나의 값으로 전달하기 위해 sum
        loss = y[j][0] - output
        w = w+x[j]*0.1*loss
        b = b+b_x*0.1*loss

        loss_sum += loss

    if i % 200 == 0:
        print("epoch:{}\tweight:{}\tloss_sum:{}\tbias:{}".format(i+1,w,loss_sum,b))

# 평가를 보면
for i in range(4):
    print("x:{}\t y:{}\t output:{}".format(x[i],y[i],sigmoid(np.sum(x[i]*w)+b))) # todo w, b는 최종 가중치와 편향이 저장되어 있기 때문


######################################################## and or
print("=========================or gate")

x = np.array([[1,1],[0,1],[1,0],[0,0]])
y = np.array([[1],[1],[1],[0]]) # 라벨값만 달라진다

w = tf.random.normal([2], 0, 1)
b = tf.random.normal([1], 0, 1)

b_x = 1 # 바이어스도 똑 같이 업데이트 해주기 위해서 아래 코드 참조

for i in range(2000):
    loss_sum = 0

    for j in range(4):
        output = sigmoid(np.sum(x[j]*w)+b_x+b) # 행렬 곱한것을 하나의 값으로 전달하기 위해 sum
        loss = y[j][0] - output
        w = w+x[j]*0.1*loss
        b = b+b_x*0.1*loss

        loss_sum += loss

    if i % 200 == 0:
        print("epoch:{}\tweight:{}\tloss_sum:{}\tbias:{}".format(i+1,w,loss_sum,b))

# 평가를 보면
for i in range(4):
    print("x:{}\t y:{}\t output:{}".format(x[i],y[i],sigmoid(np.sum(x[i]*w)+b))) # todo w, b는 최종 가중치와 편향이 저장되어 있기 때문



######################################################## and xor
# xor은 학습이 제대로 되지 않는다.결과를 보면 알겠지만....
print("=========================xor gate")

x = np.array([[1,1],[0,1],[1,0],[0,0]])
y = np.array([[0],[1],[1],[0]]) # 라벨값만 달라진다

w = tf.random.normal([2], 0, 1)
b = tf.random.normal([1], 0, 1)

b_x = 1 # 바이어스도 똑 같이 업데이트 해주기 위해서 아래 코드 참조

for i in range(2000):
    loss_sum = 0

    for j in range(4):
        output = sigmoid(np.sum(x[j]*w)+b_x+b) # 행렬 곱한것을 하나의 값으로 전달하기 위해 sum
        loss = y[j][0] - output
        w = w+x[j]*0.1*loss
        b = b+b_x*0.1*loss

        loss_sum += loss

    if i % 200 == 0:
        print("epoch:{}\tweight:{}\tloss_sum:{}\tbias:{}".format(i+1,w,loss_sum,b))

# 평가를 보면
for i in range(4):
    print("x:{}\t y:{}\t output:{}".format(x[i],y[i],sigmoid(np.sum(x[i]*w)+b))) # todo w, b는 최종 가중치와 편향이 저장되어 있기 때문


# xor은 제대로 학습이 안되어서. 중간에 밀집층을 두고 다시한번 해보자
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

np.random.seed(111)

x = np.array([[1,1],[0,1],[1,0],[0,0]])
y = np.array([[0],[1],[1],[0]])

model = Sequential(
    [
        Dense(units=2, activation='sigmoid', input_shape=(2,)),
        Dense(units=1, activation='sigmoid')
    ]
)

model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1), loss='mse')
model.summary()

history = model.fit(x, y,epochs=2000, batch_size=1, verbose=1)

# 예측
pre = model.predict(x)
print(pre) # 0, 1, 1, 0에 각각 가깝게 나와야 한다. 그런데 잘 안되네....ㅎㅎㅎ

# 그래프로 보면
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.show()