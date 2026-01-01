"""
두개의 행렬을 합치는 용도. 사용할 일이 거의 없을 듯
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)

print(a)
print(b)

print(np.append(a, b))
print(np.append(a, b, axis=0))
print(np.append(a, b, axis=1))
