"""
특별한 숫자 등의 포함여부를 확일 할 때 많이 사용
"""

import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)


print(a == 5)


if np.any(a == 5):
    print("ok")
else:
    print("no")
