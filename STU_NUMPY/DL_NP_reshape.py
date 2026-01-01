"""
형태를 변형, -1를 적으면 알아서 차원츨 결정
"""

import numpy as np

aa = np.arange(0, 20)
print(aa)

print(aa.reshape(4, 5))
print(aa.reshape(2, 2, 5))
print(aa.reshape(4, -1))
print(aa.reshape(5, -1))
print(aa.reshape(2, 5, -1))
