# 훈련용 데이터와 검증용 데이터를 나누는 함수

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import platform
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

x = np.array(range(1,101))
y = np.array(range(1,101))

# train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
# <입력값>
# arrays : list, numpy, arrays 등
# test_size : 테스트 데이터셋의 비율(float)이나 갯수(int) (default = 0.25)
# train_size : 학습 데이터셋의 비율(float)이나 갯수(int) (default = test_size의 나머지)
# random_state : 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값 (int나 RandomState로 입력), 즉 몇번을 섞을 것인가
# shuffle : 셔플여부설정 (default = True)
# stratify : 지정한 Data의 비율을 유지한다. 예를 들어, Label Set인 Y가 25%의 0과 75%의 1로 이루어진 Binary Set일 때, stratify=Y로 설정하면 나누어진 데이터셋들도 0과 1을 각각 25%, 75%로 유지한 채 분할된다.

# <출력값>
# X_train, X_test, Y_train, Y_test : arrays에 데이터와 레이블을 둘 다 넣었을 경우의 반환이며, 데이터와 레이블의 순서쌍은 유지된다.
# X_train, X_test : arrays에 레이블 없이 데이터만 넣었을 경우의 반환


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=66, test_size=0.4)
# 아래의 결과를 보면 알겠지만 데이터(x)와 레이블(y)는 항상 쌍을 유지한다. 이게 중요하다.
print("=" * 50)
print(x_train)
print(y_train)

print("=" * 50)
print(x_test)
print(y_test)


