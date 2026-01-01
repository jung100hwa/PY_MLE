"""
다음값과의 차이
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)

print(np.diff(a))
print(np.diff(a, axis=0))
print(np.diff(a, axis=1))
