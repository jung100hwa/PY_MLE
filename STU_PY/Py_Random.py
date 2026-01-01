import random

print(random.random())

print(random.randint(1,10))

print(random.randint(1,55))


#  리스트 중에서 무작위로 하나를 선택하는 함수
def random_choice(data):
    re = random.choice(data)
    return re

# 하나를 선택해서 pop
data = list(range(0,10))
print(data)

data.pop(random_choice(data))
print(data)

# 리스트를 무작위로 섞기
# 리턴값이 있는게 아니라 그 자체를 바꾼다.
data = list(range(0,20))
random.shuffle(data)
print(data)