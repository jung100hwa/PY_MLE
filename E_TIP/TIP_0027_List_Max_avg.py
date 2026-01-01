"""
리스트 안의 항목수, 평균을 구한다.
"""

strList = [['aaa', 'bbb'],['ccc', 'ddd'],['aaa', 'bbb','ccc']]

# 각 항목수 중 가장 큰값
print(max(len(x) for x in strList))

# 항목수 평균
print(sum(map(len, strList)) / len(strList))