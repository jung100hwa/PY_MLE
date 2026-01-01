"""
리스트 안에서 특정 조건에 맞는 항목들 전체 삭제
여기서는 길이가 2이하인 문자열을 전체 삭제해보자
"""

import numpy as np

strList = ['aaaa', 'bb', 'cdddd', 'dd', 'eee', 'ff', 'ff']
result = [index for index, value in enumerate(strList) if len(value) <= 2]
print(result)

# 만약에 오류 날때는 리스트를 object 타입 변경
# strList = np.array(strList, dtype=object)

strList = np.delete(strList, result, axis=0)
print(strList)