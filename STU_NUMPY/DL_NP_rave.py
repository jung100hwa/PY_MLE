"""_summary_
그냥 1차원화 또는 평평하게 만든다.
"""

import numpy as np

ori = np.arange(1,10).reshape(3,3)
print(ori)

# C스타일
ar = np.ravel(ori,order='C')
print(ar)

# F스타일(컬럼 방향)
ar = np.ravel(ori,order='F')
print(ar)

# 3차원 배열을 평평하게 만들기
ori3 = np.arange(1,13).reshape(2,3,2)
print(ori3)

ar = np.ravel(ori3, order='C')
print(ar)

ar = np.ravel(ori3, order='F')
print(ar)