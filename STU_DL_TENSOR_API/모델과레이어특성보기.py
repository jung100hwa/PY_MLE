import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.utils import plot_model

#################################################################### 1
inputs = Input(shape=(4,4))

x = Flatten(input_shape=(4,4))(inputs)
x = Dense(3,activation='relu')(x)
x = Dense(2, activation='relu')(x)
x = Dense(1, activation='softmax')(x)

model = Model(inputs=inputs, outputs=x)
model.summary()

# 모델에 있는 레이어 목록
print(model.layers)

# 모델 2번째 레이어 이름
print(model.layers[2].name)

# 모델 1번째 레이어의 가중치, 바이어스 ==> 값이 없다.
# weights, biases = model.layers[1].get_weights()

# 모델 2번째 레이어의 가중치, 바이어스
weights1, biases1 = model.layers[2].get_weights()
print(weights1)
print(weights1.shape)

# 모델 3번째 레이어의 가중치, 바이어스
weights2, biases2 = model.layers[3].get_weights()
print(weights2)
print(weights2.shape)



#################################################################### 2
inputs = Input(shape=(4,4))

# x = Flatten(input_shape=(28,28,1))(inputs)
x = Dense(3,activation='relu')(inputs)
x = Dense(2, activation='relu')(x)
x = Dense(1, activation='softmax')(x)

model = Model(inputs=inputs, outputs=x)
model.summary()

# 모델에 있는 레이어 목록
print(model.layers)

# 모델 2번째 레이어 이름
print(model.layers[1].name)

# 모델 1번째 레이어의 가중치, 바이어스 ==> 값이 없다.
# weights, biases = model.layers[1].get_weights()

# 모델 1번째 레이어의 가중치, 바이어스 todo 1번째가 되어 야 한다. 하나의 레이어가 사라졌기 때문에
weights3, biases3 = model.layers[1].get_weights()
print(weights3)
print(weights3.shape)

# 모델 2번째 레이어의 가중치, 바이어스
weights4, biases4 = model.layers[2].get_weights()
print(weights4)
print(weights4.shape)


################################### 비교
print("########################################")
print(weights1)
print(weights1.shape)
print()

print(weights2)
print(weights2.shape)
print()

print(weights3)
print(weights3.shape)
print()

print(weights4)
print(weights4.shape)


