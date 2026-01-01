import tensorflow as tf
import matplotlib.pylab as plt
import numpy as np

"""
1. 그래디언트는 한점에서 기울기을 구함
2. tape 기록해서 역전파 할 때 사용하는 것 같음 특히 경사하강법에서 사용한다고 하는데
"""


t = np.arange(0, 5, 0.01)
plt.plot(t, (t-1)*(t-4))
plt.grid()
plt.show()

x= tf.Variable(2.5)

with tf.GradientTape() as tape: # tape을 여러번 사용할려면 persitent=True
    y = (x-1)*(x-4)

# y 형태의 그래프의 x지점에서 기울기. 즉 미분값
result = tape.gradient(y, x)
print(result)
print(result.numpy())



##############  아래 내용은 잘 모르겟음. 아래 사이트 참고
"""
공부할 필요가 있음
"""
# https://www.youtube.com/watch?v=qw8J5SMfCKA
t = tf.Variable(2.0)
with tf.GradientTape(persistent=True) as tape: # persitent=True tape을 아래에도 여러번 사용할 경우
    x = 2*t
    y = x**2

result = tape.gradient(y, x)
print(result.numpy())