"""
벡터의 크기를 구하는 함수
즉 기본이 배열 제곱의 루트
"""

import numpy as np
# import numpy.linalg as LA
from numpy.linalg import norm

a = np.array([1, 3, 5, 7])

# todo 기본이 제곱의 루트이다. 이걸 보통 L2 norm
print(norm(a))

# 1승의 루트, L1 norm
print(norm(a,1))

# 여기서부터는 단순 루트 개념이 아니다. 나도 잘 모르겠다. 공식에 의해서 나온다.
print(norm(a,3))
print(norm(a,4))

# todo 벡터 정규화에 쓰인다. 결국 정규화라는 것은 1을 넘지 않도록 기존 값을 비율데로 감소
a = np.array([1, 3, 5, 7])
print(a/norm(a))