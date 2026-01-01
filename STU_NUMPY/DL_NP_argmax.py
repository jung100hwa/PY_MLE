"""
축정보에 따라 가장 큰값을 가진 인덱스. 큰값이 아니다. 인덱스
"""

import numpy as np

# 0, 5 사이에 10개 숫자를 만든다.
result = np.linspace(0, 5, 10).tolist()
print(result)

result1 = np.argmax(result, axis=0)
print(result1)

# 축을 이용한 인덱스 값 돌려받기
# https://jimmy-ai.tistory.com/72 아주 잘되어 있음


print()
result = np.arange(1, 10)
np.random.shuffle(result)

result = result.reshape(3, 3)
print(result)
print()

result1 = np.argmax(result, axis=0)
print(result1)
print()


result2 = np.argmax(result, axis=1)
print(result2)
print()
