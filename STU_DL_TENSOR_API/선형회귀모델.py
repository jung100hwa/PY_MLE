import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-white')

learning_rate = 0.01
training_steps = 1000

x = np.random.randn(50)
y = 2*x + np.random.randn(50)

w = tf.Variable(np.random.randn(), name='weight')
b = tf.Variable(np.random.randn(), name='bias')

# 선형함수 정의
def line_regression(x):
    return w*x+b

# 손실함수
def mean_square(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred-y_true))

optimizer = tf.keras.optimizers.SGD(learning_rate)

# 이 함수를 잘 파악해야 한다. 자동으로 tape해당 변수들이 저장된다. for 등 구문이 필요없다.
def run_optimization():
    with tf.GradientTape() as tape:
        pred = line_regression(x)
        loss = mean_square(pred, y)

        # 이 부분이 기울기와 바이어스를 개선해서 반영하는 부분이다.
        gradients = tape.gradient(loss, [w,b])
        optimizer.apply_gradients(zip(gradients, [w,b]))


for step in range(1, training_steps + 1):
    run_optimization()

    if step % 50 == 0:
        pred = line_regression(x)
        loss = mean_square(pred, y)
        print("step:{:4d}\t loss:{:.4f}\t w:{:.4f}\t b:{:.4f}".format(step, loss, w.numpy(), b.numpy()))
