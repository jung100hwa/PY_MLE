"""
배치정규화는 에포크의 배치가 아니다. input data를 평균, 분산 등을 이용해서 일정하게 만드는 것이다.
예를 들면 모든 수를 (0~1) 사이로 만든다.
todo 중요한 것은 Dense와 Activation 사이에 넣어 준다.
"""
from tensorflow.keras.layers import Dense, BatchNormalization, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model

model = Sequential()
model.add(Dense(32, input_shape=(28*28,), kernel_initializer='he_normal'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.summary()

plot_model(model,show_shapes=True)
