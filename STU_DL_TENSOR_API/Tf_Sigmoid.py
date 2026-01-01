"""
시그모이드 함수는 계단함수의 단점(0.5보다 크냐작냐만 따짐. 0과 1로 표시)을 보완한 s자형으로 결과에 차이를 상세하게 둔다
그리고 역전파 수행시 경사하강법을 사용하는데 경사하강법은 기본적으로 미분가능해야 한다. 계단함수는 한점에서 기울기를 구할 수 없음
시그모이드 함수는 한점에서 미분 가능하다.

# todo 단점으로 처음과 끝에서 계단함수와 마찬가지로 기울기가 사라진다.
"""

"""
프로세스
1.활성화 함수(시그모이드) 만들고
2.뉴런을 활성화함수에 넣어서 결과값 출력
"""

import numpy as np
import tensorflow as tf


# 시그모이드 함수 정의
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 뉴런을 만들고 활성화함수(시그모이드 통과)
def Neuron(x,w,bias=0):
    z = w*x+bias
    return sigmoid(z)

x = tf.random.normal((1,2), 0, 1)
w = tf.random.normal((1,2), 0, 1)

print(x)
print(w)
print(Neuron(x,w))

