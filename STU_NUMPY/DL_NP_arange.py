"""
배열을 생성. 아마도 가장 많이 사용할 듯
"""

import numpy as np

# 간격까지 설정
print(np.arange(0, 10, 2))

# 보통은 아래와 같이 reshape
print(np.arange(1, 10).reshape(3, 3))
