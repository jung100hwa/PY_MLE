import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10).reshape(3, 3)
print()
print(a)
print(b)


print(np.dot(a, b))  # 차원이 같을 때는 행렬곱
print(np.matmul(a, b))  # matmul을 권고

print()

# 차원이 다를 경우는 내적(단순 같은 원소끼리 곱)
a = np.array([[1, 3], [2, 4]])
b = np.array([2, 5])

print(a)
print(b)
print(np.dot(a, b))
