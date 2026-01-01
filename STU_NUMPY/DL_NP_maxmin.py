"""
maximum 함수는 여러 array에서 각 위치에서 최대 값을 가져오는 함수
"""

import numpy as np

print("==============max")
a = np.arange(1, 10)
print(np.max(a))

a = np.arange(1, 10).reshape(3, 3)
print(a)
print(np.max(a))
print(np.max(a, axis=0))
print(np.max(a, axis=1))

print("==============maxnum")
a = np.array([1, 3, 5])
b = np.array([6, 4, 2])
print(a)
print(b)
print()
print(np.maximum(a, b))
