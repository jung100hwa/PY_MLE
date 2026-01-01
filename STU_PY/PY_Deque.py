# 리스트와 비슷한데 속도가 빠르다
from collections import deque

aList = [1,2,3,4,5]
qDeque = deque(aList)
print(qDeque)

print('=' * 50)
for item in qDeque:
    print(item)

print('=' * 50)
qDeque.appendleft(0)
qDeque.append(6)
print(qDeque)

print('=' * 50)
qDeque.pop()
print(qDeque)
qDeque.popleft()
print(qDeque)