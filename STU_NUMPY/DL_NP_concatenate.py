"""
2개의 행렬을 합치는 함수. append 함수를 더 많이 사용할 것 같은데
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print(a)
print(b)

print(np.concatenate([a, b]))
print(np.concatenate([a, b], axis=1))

# append 하고 똑 같음
print(np.append(a, b))
print(np.append(a, b, axis=0))
print(np.append(a, b, axis=1))
