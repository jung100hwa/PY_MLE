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
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.datasets.boston_housing import load_data

from sklearn.model_selection import train_test_split

from sklearn.model_selection import KFold

plt.style.use('seaborn-v0_8-white')

# 난수 발생시 동일한 난수 발생시키기 위한 함수
tf.random.set_seed(111)

(x_train_full, y_train_full), (x_test, y_test) = load_data(path='boston_housing_npz', test_split=0.2, seed=111)

# 데이터 전터리 (표준화)
mean = np.mean(x_train_full, axis=0)
std = np.std(x_train_full, axis=0)

# 각각의 피처의 값의 범위가 다르니 편차 / 표준편차로 나누어줘서 값의 범위를 일정하게 맞춰준다.
# 수학이라서 그런값다 해야 할 것
x_train_processed = (x_train_full - mean) / std
x_test = (x_test - mean) / std

k = 3
kfold = KFold(n_splits=k, random_state=111, shuffle=True)

def build_model():
    inputs = Input(shape=(13,), name='input')
    hidden1 = Dense(100, activation='relu', name='dense1')(inputs)
    hidden2 = Dense(64, activation='relu', name='dense2')(hidden1)
    hidden3 = Dense(32, activation='relu', name='dense3')(hidden2)
    output = Dense(1, name='outpout')(hidden3)

    model = Model(inputs=[inputs], outputs=output)
    model.compile(loss='mse', optimizer='adam',
                  metrics=['mae'])

    return model


mae_list = []

for train_idx, val_idx in kfold.split(x_train_processed):
    x_train_fold, x_val_fold = x_train_processed[train_idx], x_train_processed[val_idx]
    # x_train_fold, x_val_fold = x_train_full[train_idx], x_train_full[val_idx]
    y_train_fold, y_val_fold = y_train_full[train_idx], y_train_full[val_idx]

    model = build_model()
    model.fit(x_train_fold, y_train_fold, epochs=300, validation_data=(x_val_fold,y_val_fold))
    _, test_mae = model.evaluate(x_test, y_test)
    mae_list.append(test_mae)

# 정확도가 가장 좋은 모델을 그냥 써도 된다.
print(mae_list) 

# 아래는 어떻게 평균 정확도의 평균을 구해봤다. 그렇니까 대충 자료를 어떻게 돌리든 정확도는 저 정도 나온다라는 의미
print(np.mean(mae_list))


