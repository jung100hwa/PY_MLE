"""
현재의 배열의 형태를 변경. 숫자가 없으면 0으로 채운다고 하는데 있는 숫자가지고
사이트 변경을 하는 것 같다.
"""

import numpy as np

aa = np.random.randint(0, 10, (2, 5))
print(aa)

print(np.resize(aa, (5, 2)))
print(np.resize(aa, (10, 10)))

aa = np.array([1, 2, 3, 4, 5])
print(aa)
print(np.resize(aa, (3, 3)))

print(np.arange(1, 10).reshape(3, 3))
