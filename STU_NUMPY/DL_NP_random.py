"""
보통 rand~ 로 시작하는 함수는 0~1 사이의 값
rand(), random() 함수는 동일하나 넣어주는 형태가 다르다.
"""

import numpy as np
import matplotlib.pyplot as plt

# 0-1사이의 하나의 값
print(np.random.rand())
print(np.random.rand(10))
print(np.random.rand(2, 2))


print(np.random.random((1, 3)))
print(np.random.random((3, 3)))
print(np.random.randint(1, 10, (3, 3)))


# 정규분포
aa = np.random.normal(0, 1, (30, 30))
print(aa)


plt.hist(aa, bins=30, density=True)
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("==============균등분활")
print(np.random.rand(5))
print(np.random.rand(5, 5))


aa = np.random.uniform(0, 1, 100)
print(aa)
plt.hist(aa, bins=100, density=True)
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
