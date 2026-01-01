"""
현재 날짜에 리스트 값을 더하면 날짜가 증가
오늘부터 이전 3일, 이후 3일을 계산할 때 사용
"""

import numpy as np
import datetime


aa = np.array(datetime.date.today(), dtype=np.datetime64)
print(aa)

# 오늘부터 10일간. 우리 달력을 그래도 반영. 즉 9월 30일까지 있다면 다음날은 10일 01일
print(aa + np.arange(10))

print(aa - np.arange(10))

################################## 여기서 잠깐. 리스트, 배열의 차이는 요소마다 구분자 유무
alist = [1, 2, 3, 4, 5]
print(alist)

arr = np.arange(1, 10)
print(arr)
