"""
불리언 인덱싱이라고 하는데 기존 배열에서 특정값을 선택시 사용
정말 많이 사용할 것 같으니 철저하게 알고 있어야 함
"""

import numpy as np

aa = np.arange(1, 5)
print(aa)


# 2의 배수만 선택
bb = aa % 2 == 0
print(bb)
print(aa[bb])


# 2차원도 가능하다. 2차원 자체를 계산한다. 즉 [1,2,3]은 0인덱스, [4,5,6]은 1인덱스...덩어리를 하나의 인덱스 번호로 인식
# bb = [F,T,F,T] 이기 때문에 , 1, 2 인덱스가 선택됨. 아래 사이트에 print(aa[bb,:3]) 이 부분은 조금 잘못된듯 하다.
# https://butterflytothesea.tistory.com/38

aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(aa[bb])
print(aa[bb, :3])
print(aa[bb, :2])


# 특정조건에 맞는 배열만 추려내서 집계함수를 이용한다.
# 판다스의 마스크 역활
a = np.arange(1, 10).reshape(3, 3)
print(a)
b = a > 5
print(b)

print(np.sum(a[b]))
print(np.mean(a[b]))
print(np.median(a[b]))  # 짝수일때는 중간에 2개의 값 평균
