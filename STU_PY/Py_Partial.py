from functools import partial

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add',1,2,3,4,5))
print(add_mul('mul',1,2,3,4,5))

print('=' * 50)

# add(1,2,3,4,5), mul(1,2,3,4,5)를 기존 함수를 이용해서 만든다고 할때
# 아래와 같이 하는게 일반적
# def add(*args):
#     return add_mul('add', *args)

# def mul(*args):
#     return add_mul('mul', *args)

# print(add(1,2,3,4,5))
# print(mul(1,2,3,4,5))

print('=' * 50)
# 아래와 같이 좀더 우아한 방법으로. 참 전혀 의미 없는...ㅋㅋㅋ
add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5))
print(mul(1,2,3,4,5))