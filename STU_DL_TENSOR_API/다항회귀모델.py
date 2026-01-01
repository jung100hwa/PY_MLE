import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam

epochs = 2000
learn_rate = 0.001 # 이게 가장 좋은 수치라네...인터넷에서

# 2차함수의 상수
a = tf.Variable(np.random.randn())
b = tf.Variable(np.random.randn())
c = tf.Variable(np.random.randn())

print(a.numpy())
print(b.numpy())
print(c.numpy())

# feature, label
x = np.random.randn(50)
y = x**2 + x*np.random.randn(50)

print(x)
print(y)

# 그래프의 초기 상태
line_x = np.arange(min(x),max(x), 0.001)
line_y = a*line_x**2 + b*line_x + c

# 이건 그냥 보여주기식. 왜 하는지 모르겠음
x_ = np.arange(-4, 4, 0.001)
y_ = a*x_**2 + b*x_ + c


plt.scatter(x, y, label = 'x data')
plt.plot(x_, y_, 'g--', label='origin line')
plt.plot(line_x, line_y, 'r--', label='after train')
plt.xlim(-4.0, 4.0)
plt.legend()
plt.grid()
plt.show()

# 손실함수 정의
def compute_loss():
    pred_y = a*(np.array(x)**2) + b*np.array(x) + c
    loss = tf.reduce_mean((y-pred_y)**2)
    return loss

optimizer = Adam(learning_rate=learn_rate)

for epoch in range(1, epochs + 1):
    optimizer.minimize(compute_loss, var_list=[a, b, c])

    if epoch % 100 == 0 :
        print("epoch:{}]]t a:{}\t b:{}\t c:{}\t".format(epoch, a.numpy(), b.numpy(), c.numpy()))


# a, b, c가 갱신되었으니 이 변수는 재정의 후 차트 그리기
line_x = np.arange(min(x),max(x), 0.001)
line_y = a*line_x**2 + b*line_x + c

plt.scatter(x, y, label = 'x data')
plt.plot(x_, y_, 'g--', label='origin line')
plt.plot(line_x, line_y, 'r--', label='before train')
plt.xlim(-4.0, 4.0)
plt.legend()
plt.grid()
plt.show()
