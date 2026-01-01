"""
참조, 얕은복사, 깊은복사 개념
mutable : list,set, dictionary만 해당
immutable : int, tuple 이것은 무조건 copy, 즉 얕은 복사의 개념
"""

import copy

# 먼저 참조의 의미. 같은 메모리를 바라본다.
a = [1,2,3]
b = a
b[0] = 100
print(a,b)

# 얕은복사, 별도 메모리에 생성함으로 영향을 주지 않는다.
a = [1,2,3]
b = a.copy()
b[0] = 100
print(a,b)

# 깊은 복사, 1차원일때는 얕은 복사랑 똑 같음
a = [1,2,3]
b = copy.deepcopy(a)
b[0] = 100
print(a,b)

# 문제는 리스트가 2차원일때. 얕은 복사는 리스트 안의 리스트를 참조 한다는 것
print("#" * 50)
a = [[1,2],[3,4]]
b = a.copy()
b[0][0] = 100 # 원래 1차원일때 이렇게 하면 a는 값이 변경이 없어야 한다. 그런데 2차원일때는 내부 리스트를 참조만 한다.
print(a,b)

# 2차원리스트를 깊은 복사를 해보자
print("#" * 50)
a = [[1,2],[3,4]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a,b)
