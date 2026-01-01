"""
케라스에서 제공하는 mnis 손글씨 이미지를 실제 0~9(라벨) 학습
예측은 내가 쓴 손글씨 이미지를 실제 숫자로 매핑하면 오케이
"""
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras import models
from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.utils import plot_model, to_categorical

from sklearn.model_selection import train_test_split
import numpy as py

import matplotlib.pyplot as plt

# 마지막 성능보고서 출력을 위해
from sklearn.metrics import classification_report

# callback 함수 이용하기 위해
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, LearningRateScheduler, TensorBoard, ReduceLROnPlateau

import datetime


# print(plt.style.available)
plt.style.use('seaborn-v0_8-white')

tf.random.set_seed(111)

(x_train_full, y_train_full),(x_test, y_test) = load_data('mnist.npz')
x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full, test_size=0.3, random_state=111)

# x데이터 확인
print(len(x_train_full))
print(len(x_train))

print(x_train_full[:5])
plt.imshow(x_train_full[0])
plt.show()

# 라벨 확인
print(len(y_train_full))
print(len(x_train))
print(y_train_full[:5])


# x데이터에 대해 정규화(0~1)로 바꾸자
x_train = x_train / 250.
x_val = x_val / 250.
x_test = x_test / 250.

print(x_train[:5])

# 라벨에 대해 원한 코딩
print(y_train[0])

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

print(y_train[:5])


# 모델생성.
model = Sequential(
    [
        Input(shape=(28,28), name='input'),
        Flatten(input_shape=[28,28], name='flatten'), # 입력값을 다 펼친다.
        Dense(100, activation='relu', name='dense1'),
        Dense(64, activation='relu', name='dense2'),
        Dense(32, activation='relu', name='dense3'),
        Dense(10, activation='softmax', name='output')
        ]
)

model.summary()
plot_model(model, show_shapes=True)

# 훈련
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='sgd')

################### 콜백함수
# todo ModelCheckpoint는 중간에 손실(loss), 정확도(accuracy)가 가장 좋은 todo 가중치만 저장
# todo 활용은 중간에 어떠한 사유로 중단되었을 때 이 가중치를 불어와서 재학습시킨다
# todo model.load_weights("weights.h5")
# todo 처음부터 하지 않는다는 잇점이 있고 실제 아무일 없이 훈련이 완료되었을 때에는 당연히 최상의 가중치와 함께 모델도 저장됨
check_point_md = ModelCheckpoint('keras_minist_model.keras', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)

# todo EarlyStopping 손실(loss)가 에포크 5 동안 개선되지 않을 때 중단
check_point_st = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1)

# 보통 ModelCheckpoint, check_point_st 함께 사용하는 듯

# todo ReduceLROnPlateau 손실(loss)가 에포크 5동안 개선되지 않으면 학습률을 기존의 0.5로 재조정
# todo 그런데 얘는 단독으로 주로 많이 쓰이는 듯
# todo check_point_rr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, verbose=1)
# 그외에도 LearningRateScheduler: 에포크 어느 정도 됬을때 강제 변경

# todo 텐서보드 사용 많은 공부가 필요해 보임
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") # 여기에 반드시 시간을 줘야 할 듯 안주면 안되는듯.....
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1, write_graph=True, write_images=True)

history = model.fit(x_train, y_train, epochs=50, batch_size=128,
                    validation_data=(x_val,y_val), verbose=1, callbacks=[check_point_md, check_point_st,tensorboard_callback])

# 평가
model.evaluate(x_test,y_test)

# 예측
pred_ys = model.predict(x_test)
print(pred_ys[0]) # 첫번째 값으로 테스트
print(y_test[0])


arg_pred_max = np.argmax(pred_ys[0])
y_test_max = np.argmax(y_test[0])
print("예측값={}, 실제값={}".format(arg_pred_max, y_test_max))


# 전체 결과 확인(컨퓨전매트릭스로 평가)
print(classification_report(np.argmax(y_test, axis=-1),np.argmax(pred_ys,axis=-1)))


# 모델저장. sava 함수는 모델과 가중치를 한꺼번에 저장 함.
model.save("mnist_model.keras")

# 모델불러오기
loaded_model = models.load_model('mnist_model.keras')
loaded_model.summary()

# 불러온 모델로 테스트
pred_ys = loaded_model.predict(x_test)
print(pred_ys[0]) # 첫번째 값으로 테스트
print(y_test[0])

arg_pred_max = np.argmax(pred_ys[0])
y_test_max = np.argmax(y_test[0])
print("예측값={}, 실제값={}".format(arg_pred_max, y_test_max))