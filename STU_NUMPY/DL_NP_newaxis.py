import numpy as np

arr = np.arange(4)
print(arr.shape)

# 로우 벡터로 차원을 하나 늘림
row_vec = arr[np.newaxis, :]
print(row_vec.shape)

# 컬럼 벡터로 차원을 하나 늘림
col_vec = arr[:, np.newaxis]
print(col_vec.shape)


# 넘파이 브로드캐스팅을 위해
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3])

x1_new = x1[:, np.newaxis]
print(x1_new.shape)
print(x1_new)
print(x2)
print(x1_new + x2)
