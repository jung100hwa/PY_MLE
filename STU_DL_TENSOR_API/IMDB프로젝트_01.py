"""
케라스에서 제공하는 영화 평가 데이터를 불러와서 학습
"""

from tensorflow.keras.datasets import imdb
import numpy as np


(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print(len(train_data))
print(train_data[:5])

def vectorize_seq(seqs, dim=10000):
    results = np.zeros((len(seqs), dim))
    for i, seq in enumerate(seqs):
        results[i, seq] = 1
    return results

x_train = vectorize_seq(train_data)
x_test = vectorize_seq((test_data))
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, LearningRateScheduler, TensorBoard, ReduceLROnPlateau

############################################################################## 이렇게 하니 오버피팅 발생
model = Sequential(
    [
        Dense(16, activation='relu', input_shape=(10000,), name='inputs'),
        Dense(16, activation='relu', name='hidden'),
        Dense(1, activation='sigmoid', name = 'outputs')
        ]
)

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
model.summary()

check_point_md = ModelCheckpoint('keras_minist_model.keras', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)
check_point_st = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)


# mode_hit = model.fit(x_train, y_train, epochs=20, batch_size=512, validation_split=0.2,callbacks=[check_point_md, check_point_st])
mode_hit = model.fit(x_train, y_train, epochs=20, batch_size=512, validation_split=0.2)

print("=============================> evaluate")
model.evaluate(x_test,y_test)

import matplotlib.pyplot as plt
print(plt.style.available)

plt.style.use('seaborn-v0_8-white')
epochs = range(1,21) # 이렇게 레인지를 맞출려면 콤백함수를 주면 안된다. 콜백함수를 줄려면 plot() 함수에서 첫번째 인자를 주지 말자
model_val_loss = mode_hit.history['val_loss']

plt.plot(epochs, model_val_loss, 'r+')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()


########################################################################## 여기서부터 오버피팅 해결방안
"""
    1.먼저 모델의 크기를 줄인다.
    모델의 크기를 줄인다는 것은 아웃품 텐서의 개수를 줄인다.
    그래프 모양을 보면 알지만 에포크가 증가함에 따라 loss 값이 줄어든다.
"""

model_s = Sequential(
    [
        Dense(7, activation='relu', input_shape=(10000,), name='inputs2'),
        Dense(7, activation='relu', name='hidden2'),
        Dense(1, activation='sigmoid', name = 'outputs2')
        ]
)

model_s.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
model_s.summary()

check_point_md = ModelCheckpoint('keras_minist_model.keras', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)
check_point_st = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)


# mode_hit = model.fit(x_train, y_train, epochs=20, batch_size=512, validation_split=0.2,callbacks=[check_point_md, check_point_st])
mode_hit_s = model_s.fit(x_train, y_train, epochs=20, batch_size=512, validation_split=0.2)

print("=============================> evaluate")
model_s.evaluate(x_test,y_test)

plt.style.use('seaborn-v0_8-white')
epochs_s = range(1,21) # 이렇게 레인지를 맞출려면 콤백함수를 주면 안된다. 콜백함수를 줄려면 plot() 함수에서 첫번째 인자를 주지 말자
model_val_loss_s = mode_hit_s.history['val_loss']

plt.plot(epochs, model_val_loss, 'r+')      # 저위에서 오버피팅 발생한것
plt.plot(epochs_s, model_val_loss_s, 'bo')

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()


######################################################## 비교를 위해서 학습시 loss를 보자

plt.style.use('seaborn-v0_8-white')
epochs_s = range(1,21) # 이렇게 레인지를 맞출려면 콤백함수를 주면 안된다. 콜백함수를 줄려면 plot() 함수에서 첫번째 인자를 주지 말자
model_train_loss = mode_hit.history['loss']
model_train_s_loss = mode_hit_s.history['loss']

plt.plot(epochs, model_train_loss, 'g--')      # 저위에서 오버피팅 발생한것
plt.plot(epochs_s, model_train_s_loss, 'bo')

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()


"""
여기까지 결론
1. 학습시 loss는 제대로 줄어드는데 검증시 loss를 보면 에포크가 증가할 수록 어느 시점에서 다시 증가
2. 이말은 오퍼피팅이 발생했다는 증거 임
3. 오퍼피팅 해결을 위해 1) 규모 축소 2) 옵티마이저 선택 3) 가중치 초기화 4) dropout(가장 효과적) 5) 배치정규화 6) L1, L2 규제화 등 여러가지 방법을 사용해야 함
4. 규모 축소라 함은 레이어의 출력 텐서를 줄이는 것
"""






