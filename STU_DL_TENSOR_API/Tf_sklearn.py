"""
1. 라벨을 정수인코딩
"""

############################################## 1.라벨을 정수인코딩
import os
os.chdir(r"c:\projects\PY_MLE")

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('train.csv')
print(train.columns)
print(train['Sex'][:5])


# 정수인코딩
le = LabelEncoder()
result = le.fit_transform(train['Sex'])
print(result)


# 변환된 라벨과 정수 매핑정보 확인
print(le.classes_)

##############다른 예
print("------------------------")
x_test = np.array(['pc','mobile','tablet'])

encoder = LabelEncoder()
encoder.fit(x_test)

x_test_encoded = encoder.transform(x_test)
print(x_test_encoded)

print(encoder.classes_)