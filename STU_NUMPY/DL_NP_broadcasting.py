"""
broadcasting.png를 참고
브로드캐스팅 조건이 있구나. 일단 1차원 1차원은 안되는 것 같네
"""

import numpy as np

a = np.array([1, 2, 3])
print(a + 10)

b = np.arange(1, 10).reshape(3, 3)
print(b)
print(a + b)

b = np.arange(1, 4).reshape(3, 1)
print(b)
print(a + b)
