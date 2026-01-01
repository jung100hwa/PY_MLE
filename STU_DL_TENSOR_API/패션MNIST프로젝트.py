"""
옷, 신발 등 이미지를 보고 어느 분류에 속하는질 알아내는 것
"""

import tensorflow as tf
from tensorflow.keras.datasets.fashion_mnist import load_data
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, LearningRateScheduler, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model, to_categorical
from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-white')

# 데이터로드
tf.random.set_seed(111)
(x_train_full, y_train_full), (x_test, y_test) = load_data()
x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full,
                                                  test_size=0.3,
                                                  random_state=111)

# 데이터확인
print(x_train_full.shape)
print(x_train.shape)
print(x_val.shape)
print(y_train_full.shape)
print(y_train.shape)
print(y_val.shape)

class_name = ['T-shirt/top',
'Trouser',
'Pullover',
'Dress',
'Coat',
'Sandal',
'Shirt',
'Sneaker',
'Bag',
'Ankle boot']

print(class_name[y_train[2]])

# 정규화
# x_train = (x_train.reshape(-1, 28, 28)) / 255. # Flattern 레이어를 사용해도 되는데 여기서 펼쳐 버림
# x_val = (x_val.reshape(-1, 28, 28)) / 255.
# x_test = (x_test.reshape(-1, 28, 28)) / 255.

x_train = x_train / 255 # Flattern 레이어를 사용해도 되는데 여기서 펼쳐 버림
x_val = x_val / 255
x_test = x_test / 255

# 라벨에 대해 원한 코딩
# todo loss='sparse_categorical_crossentropy' 일때는 원핫 코딩하면 안된다.
# y_train = to_categorical(y_train)
# y_val = to_categorical(y_val)
# y_test = to_categorical(y_test)


# 모델 만들기(함수형 API)
input = Input(shape=(28,28), name = 'input')
flatlayer = Flatten(input_shape=[28, 28], name='flatten')(input)
hidden1 = Dense(512, activation='relu', name='hidden1')(flatlayer)
hidden2 = Dense(256, activation='relu', name='hidden2')(hidden1)
hidden3 = Dense(128, activation='relu', name='hidden3')(hidden2)
hidden4 = Dense(64, activation='relu', name='hidden4')(hidden3)
hidden5 = Dense(32, activation='relu', name='hidden5')(hidden4)
output = Dense(10, activation='softmax', name='output')(hidden5)

model = Model(inputs=[input], outputs=output)
model.summary()

# 콜백함수 정의
check_point_md = ModelCheckpoint('keras_minist_model.keras', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)
check_point_st = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)

# 모델 컴파일
model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.01),
              metrics=['acc'])

# 학습
history = model.fit(x_train, y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val),
                    callbacks=[check_point_md,check_point_st])


# 평가
model.evaluate(x_test, y_test)


# 예측
pred_ys = model.predict(x_test)
aa = np.argmax(pred_ys[0])
print("인덱스 번화 {}, 이름은 {}".format(aa, class_name[aa]))
plt.imshow(x_test[0])
plt.show()

# 모델저장. sava 함수는 모델과 가중치를 한꺼번에 저장 함.
model.save("fashion_mnist_model.keras")

# 모델불러오기
loaded_model = models.load_model('fashion_mnist_model.keras')

# 불러온 모델로 테스트
pred_ys = loaded_model.predict(x_test)
aa = np.argmax(pred_ys[1])
print("인덱스 번화 {}, 이름은 {}".format(aa, class_name[aa]))

plt.imshow(x_test[1])
plt.show()

