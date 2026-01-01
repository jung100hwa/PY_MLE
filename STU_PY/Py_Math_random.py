import random

aList = []

# 6개의 무작위 숫자
while len(aList) < 6:
    num = random.randint(1,45)
    aList.append(num)
print(aList)

# 리스트 숫자를 무작위로 섞어 싶을 때
print('=' * 50)
aList = [1, 2, 3, 4, 5, 6]
random.shuffle(aList)
print(aList)