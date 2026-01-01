import numpy as np

# 제곱과 제곱근
a = np.array([1,2,4])
print(a)
print(np.square(a))
print(np.sqrt(a))

# 지수와 로그
print("지수")
print(np.exp(a))   # e^x e자연상수
print(np.exp2(a))  # 2^x
print(np.power(a,2))


print("로그")
print(np.log(a))
print(np.log2(a))
print(np.log10(a))

# 삼각함수
print("삼각함수")
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
