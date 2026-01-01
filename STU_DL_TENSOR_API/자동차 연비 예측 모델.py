import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.chdir(r"c:\projects\PY_MLE\STU_DL_TENSOR_API")

import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import Model
from tensorflow.keras.utils import get_file, plot_model
from tensorflow.keras.callbacks import EarlyStopping

plt.style.use('seaborn-v0_8-white')
sns.set_theme(style='white')

# 데이터 가져오기
df = pd.read_csv('auto-mpg.csv', na_values='?', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head())
col_list = df.columns.tolist()
df = df[col_list[:-1]]

# na값을 삭제
df.dropna(inplace=True)
print(df.isna().sum())

# 범주형 원핫코딩
origin = df.pop('origin')
df['us'] = (origin == 1) * 1.
df['eu'] = (origin == 2) * 1.
df['kr'] = (origin == 3) * 1.
print(df.head())

train_dataset = df.sample(frac=0.8, random_state=0)
test_dataset = df.drop(index=train_dataset.index)

# 데이터 확인. mpg를 빼넨 이유는 이것이 정답 즉 라벨이기 때문이다.
train_stats = train_dataset.describe()
train_stats.pop('mpg')
train_stats = train_stats.transpose()
print(train_stats)

# 데이터특성과 라벨 분리
train_label = train_dataset.pop('mpg')
test_label = test_dataset.pop('mpg')

# 데이터정규화
# todo 이코드 참 유용. 전부 단위가 다르다보니 범위 격차가 심함
def nomalization(x):
    return (x - train_stats['mean']) / train_stats['std']

nor_train_data = nomalization(train_dataset)
nor_test_data = nomalization(test_dataset)

print(nor_train_data.head())
print(train_dataset.keys())
print(train_dataset.columns)

# 모델 정의
def build_model():
    inputs = Input(shape=(len(train_dataset.keys())), name='inputs')
    hidden1 = Dense(64, activation='relu', name='hidden1')(inputs)
    hidden2 = Dense(64, activation='relu', name='hidden2')(hidden1)
    outputs = Dense(1, name='ouputs')(hidden2)

    model = Model(inputs=[inputs], outputs=outputs)
    model.compile(loss='mse', optimizer=RMSprop(0.001), metrics=['mae','mse'])

    return model

model = build_model()
model.summary()

# 학습
check_point_st = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1)
history = model.fit(nor_train_data,train_label, epochs=1000, validation_split=0.2,
                    callbacks=[check_point_st])

def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    plt.figure(figsize=(12, 6))
    plt.subplot(1,2,1)
    plt.xlabel('Epoch')
    plt.ylabel('MPG Mean Absolute Error')
    plt.plot(hist['epoch'], hist['mae'], label='Train mae')
    plt.plot(hist['epoch'], hist['val_mae'], label='Train mae')
    plt.ylim([0,5])
    plt.legend()
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.xlabel('Epoch')
    plt.ylabel('MPG Mean Absolute Error')
    plt.plot(hist['epoch'], hist['mse'], label='Train mse')
    plt.plot(hist['epoch'], hist['val_mse'], label='Train mse')
    plt.ylim([0, 20])
    plt.legend()
    plt.grid()
    plt.show()

plot_history(history)

# 모델 평가. 실제 mae만큼 오차가 실제값과 있다는 의미
loss, mae, mse = model.evaluate(nor_test_data, test_label)
print(loss)
print(mae)
print(mse)

# 모델 예측
test_pred = model.predict(nor_test_data).flatten()

plt.scatter(test_label,test_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.axis('square')
plt.grid()
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.xlim()[1]])
plt.plot([-100,100], [-100,100])
plt.show()
