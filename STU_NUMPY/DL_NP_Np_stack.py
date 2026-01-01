"""
축을 하나 추가해서 연결한다. 사용할 일이 없을 것 같은데
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(10, 19).reshape(3, 3)
print(a)
print(b)

print(np.stack([a, b]))
