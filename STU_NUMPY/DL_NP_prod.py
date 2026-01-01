import numpy as np

a = np.arange(1, 5).reshape(2, 2)
print(a)

print(np.prod(a))
print(np.prod(a, axis=0))
print(np.prod(a, axis=1))

# 누적 곱
print(np.cumprod(a))
print(np.cumprod(a, axis=0))
print(np.cumprod(a, axis=1))
