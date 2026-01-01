"""
부울린인덱싱 등은 다른 파일 참조
"""

import numpy as np

# 1차원일때
a = np.arange(1, 10)
print(a)
print(np.sum(a))
print(np.sum(a > 5))  # todo 5보다 큰 수의 개수 출력

print()

# 2차원일때
a = np.arange(1, 10).reshape(3, 3)
print(a)

print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

# 개수를 의미 a > 5
print(np.sum(a > 5))
print(np.sum(a > 5, axis=0))
print(np.sum(a > 5, axis=1))

# a > 5 요소들의 합계
b = a > 5
print(b)

print(sum(a[b]))
print()

# 누적 함수
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(np.cumsum(a))

a = np.arange(1, 10).reshape(3, 3)
print(np.cumsum(a, axis=0))
print(np.cumsum(a, axis=1))
