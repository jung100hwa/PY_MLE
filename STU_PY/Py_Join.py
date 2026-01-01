"""
'구분자'.join(리스트)
join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수입니다.
출처: https://blockdmask.tistory.com/468
"""

aList = [1,2,3,4,5,6,7,8,9,10]
result = ''.join(map(str, aList))
print(result)

# 아래는 에러. 문자열
# aList = [1,2,3,4,5,6,7,8,9,10]
# result = ''.join(aList)
# print(result)

aList = ['a','b','c','d','e']
result = ''.join(aList)
print(result)

aList = [1,2,3,4,5,6,7,8,9,10]
result = '_'.join(map(str, aList))
print(result)

aList = [1,2,3,4,5,6,7,8,9,10]
result = '.\n'.join(map(str, aList))
print(result)

