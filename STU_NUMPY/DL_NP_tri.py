"""
삼각행렬을 만듬. 트랜스포머에서 마스크 만들때 사용 함
"""

import numpy as np

# 기본
print(np.tri(5))

# 결과를 보고
print(np.tri(N=5, M=5, k=0))
print(np.tri(N=5, M=5, k=1))
print(np.tri(N=5, M=5, k=-1))


a = np.arange(1, 26).reshape(5, 5)
print(a)

# 여기서 triu는 u는 under의미
print(np.triu(a))
print(np.triu(a, 0))
print(np.triu(a, 1))
print(np.triu(a, -1))

#########################################################
print("--------------------마스크에 사용")
print(np.tri(N=5, M=5, k=0))
