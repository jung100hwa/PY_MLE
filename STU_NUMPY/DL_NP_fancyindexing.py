"""
a[인덱스 배열]. 즉 boolindexing은 참과 거짓으로 찼음
이 함수는 참고 거짓이 아닌 인덱스로 값을 찾음
"""

import numpy as np


# 팬시 인덱싱
aa = np.arange(1, 10)
print(aa)

ind = np.array([1, 3])
print(ind)
print(aa[ind])

aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(aa)

row = np.array([1, 2])
col = np.array([1, 2])

"""
항상 기억해야 함. 넘파이는 로우와 컬럼이 쌍으로...
row=(1,2), col=(1,2) 이라고 하면 (1,1) (2,2) 값을 찾는다.
row=(2), col=(1,2) 이라고 하면 (2,1) (2,2) 값을 찾는다.
"""
print(aa[row, col])
print(aa[2, col])
