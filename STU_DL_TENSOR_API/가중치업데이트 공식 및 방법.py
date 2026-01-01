"""
가중치 업데이트 공식은 일반적으로 w + n(y-y~)x 이다.
w:원래 가중치
n:학습율
(y-y~): loss
x:입력값
"""

import tensorflow as tf
import numpy as np

# 시그모이드 함수 정의
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 뉴런을 만들고 활성화함수(시그모이드 통과)
def Neuron(x,w,bias=0):
    z = w*x+bias
    return sigmoid(z)

x = 1
y = 0
w = tf.random.normal([1], 0, 1)
print(Neuron(x,w)) # 활성화 함수를 지난 값(가중치가 아님)

# 여기서 알고자 하는 것은 가중치가 공식에 의해서 계속 개선된다는 것이다
for i in range(1000):
    output = Neuron(x,w)
    loss = y - output

    w = w + x * 0.1 * loss

    if i % 100 == 99:
        print("{}\t{}\t{}\t{}".format(i+1, w, output, loss))



############################################## 에제 2
def Neuron2(x,w,bias=0):
    z = tf.matmul(x,w,transpose_b=True) + bias
    return sigmoid(z)

x = tf.random.normal((1,3), 0, 1)
y = tf.ones(1) # 기본 초기값으로 그냥 설정
w = tf.random.normal((1,3), 0, 1)

# # 데이터한번찍어보고
# print(x)
# print(y)
# print(w)
# print(tf.transpose(x))
# print(tf.matmul(x,w,transpose_b=True))

print()
print("================sigmoid pass value")
print(Neuron2(x,w))

print()
print("================가중치 등 출력")


for i in range(1000):
    output = Neuron2(x,w)
    loss = y - output

    w = w + x * 0.1 * loss

    if i % 100 == 99: # 100개씩 끊어서 출력(에포크라고 생각하면 됨)
        print("{}\t{}\t{}\t{}".format(i+1, w, output, loss))