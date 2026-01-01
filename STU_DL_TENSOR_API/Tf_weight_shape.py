import tensorflow as tf
from tensorflow.keras import Sequential,Model
from tensorflow.keras import Input
from tensorflow.keras.layers import Dense, Concatenate
from tensorflow.keras.utils import plot_model


input_layer = Input(shape=(8,8), name="input_01")
hidden1 = Dense(4, activation='relu', name="dense_01")(input_layer)
hidden2 = Dense(2, activation='relu', name="dense_02")(hidden1)
concat = Concatenate()([input_layer, hidden2])
output = Dense(1, name="dense_03")(concat) #유닛1개

model = Model(inputs=[input_layer], outputs=[output])
aaa = model([input_layer])
model.summary()

# 같은 폴더에 이미지로 저장된다.
plot_model(model)


# weight 값을 조사할 수 있다. 초기 weight 값으로 보면 된다.
weight, bias = model.get_layer('dense_02').get_weights()
print(weight)
print(weight.shape) # weight의 형태이다. summary(28,5). 여기서 28은 입력값 출력값이다. 출력 형태가 나오기 위한  weight의 shape
print(bias)


weight, bias = model.get_layer('dense_01').get_weights()
print(weight)
print(weight.shape) # weight의 형태이다. summary(28,5).
print(bias)
