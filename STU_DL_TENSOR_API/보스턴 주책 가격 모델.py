"""
대표적인 회귀모델.
단점은 데이터개수가 너무 적음(600개). 피처의 단위가 다름(범죄율:0-1 사이의 값, 방의 개수: 3-9사이의 값 등)
1000달러 기준 즉 레이블이 25.이면 실제 25000 달러
# todo 정답은 주택 가격의 중간가격
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model
from tensorflow.keras.datasets.boston_housing import load_data

from sklearn.model_selection import train_test_split

plt.style.use('seaborn-v0_8-white')

# 난수 발생시 동일한 난수 발생시키기 위한 함수
tf.random.set_seed(111)

(x_train_full, y_train_full), (x_test, y_test) = load_data(path='boston_housing_npz', test_split=0.2, seed=111)

print("학습 데이터: {}\t 레이블: {}".format(x_train_full.shape, y_train_full.shape))
print("테스트 데이터: {}\t 레이블: {}".format(x_test.shape, y_test.shape))

print(x_train_full[0])
print(y_train_full[0])

# 데이터 전터리 (표준화)
mean = np.mean(x_train_full, axis=0)
std = np.std(x_train_full, axis=0)

# 각각의 피처의 값의 범위가 다르니 편차 / 표준편차로 나누어줘서 값의 범위를 일정하게 맞춰준다.
# 수학이라서 그런값다 해야 할 것
x_train_processed = (x_train_full - mean) / std
x_test = (x_test - mean) / std
print(x_train_processed[0])

# 검증데이터 확보
x_train, x_val, y_train, y_val = train_test_split(x_train_processed,y_train_full, test_size=0.3)

print("학습 데이터: {}\t 레이블: {}".format(x_train_full.shape, y_train_full.shape))
print("학습 데이터: {}\t 레이블: {}".format(x_train.shape, y_train.shape))
print("검증 데이터: {}\t 레이블: {}".format(x_val.shape, y_val.shape))
print("테스트 데이터: {}\t 레이블: {}".format(x_test.shape, y_test.shape))

# 모델생성. 데이터가 적으면 오버피팅 발생. 이때는 너무 깊게 하지 말것
model = Sequential(
    [
        Dense(100, activation='relu', input_shape=(13,), name='dense1'),
        Dense(64, activation='relu', name='dense2'),
        Dense(32, activation='relu', name='dense3'),
        Dense(1, name='outpout')
    ]
)

model.summary()

# 컴파일
model.compile(loss='mse', optimizer=Adam(learning_rate=0.01),
              metrics=['mae'])

# 학습
history = model.fit(x_train, y_train, epochs=300,
                    validation_data=(x_val,y_val))

# 평가
model.evaluate(x_test, y_test)

# 히스토리 값을 조회(그래프 등으로)
print(history.history.keys())
his = history.history

loss = his['loss']
val_loss = his['val_loss']
mae = his['mae']
val_mae = his['val_mae']

epochs = range(1, len(loss)+1)

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(epochs, loss, color = 'blue', label='train_loss')
ax1.plot(epochs, val_loss, color = 'red', label='val_loss')
ax1.set_title('Train and Validation loss')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Loss')
ax1.grid()
ax1.legend()

ax2 = fig.add_subplot(1,2,2)
ax2.plot(epochs, mae, color = 'blue', label='train_mae')
ax2.plot(epochs, val_mae, color = 'red', label='val_mae')
ax2.set_title('Train and Validation mae')
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Mae')
ax2.grid()
ax2.legend()

plt.show()

