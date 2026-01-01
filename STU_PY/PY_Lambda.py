# 람다는 가독성이 문제가 될 수 있음

from functools import reduce

print("=" * 70)

def hap(x, y):
    return x + y

print(hap(2, 3))


# 바로 표현 할 수도 있고
print("=" * 70)
print((lambda x, y: x * y)(2, 3))


# 변수로 받아서 할 수도 있고
print("=" * 70)
def lam(x, y):
    return x + y

print(lam(5, 6))

# map 함수에 적용하기, todo map(함수, 변수) 형태
print("=" * 70)
mapList = map(lambda x: x ** 2, range(1, 5))
lstList = list(mapList)  # 리스트 형식으로 변환
print(lstList)


# map 함수에 적용하기, map(함수, 변수) 형태
# map 인자 중 사용자 함수 인자가 2개이면 인자수만큼 넣어줘야 한다.
print("=" * 70)
mapList = map(hap, range(1, 5), range(1,5))  # hap 인자가 2개 이기 때문에 다음에 range를 2번 함
lstList = list(mapList)
print(lstList)


# reduce 함수 적용하기, 누적집계, 리스트가 아닌 단일값
# 먼저 0과 1을 더하고, 그 결과에 2를 더하고, 거기다가 3을 더하고, 또 4를 더한 값을 돌려줍니다. 한 마디로 전부 다 더하라는 겁니다
print("=" * 70)
print('\n reduce')
redList = reduce(lambda x, y: x + y, range(0, 5)) # 이 시그니처가 하나의 공식, 항상 2개의 인자를 요구하고 앞에 x는 누적된 값이 쌓이기 됨.
print(redList)


# 아래와 같은 경우는 안된다. 이때는 for문을 써야 한다. 아니면 map 함수를 써야 한다.
# print("=" * 70)
# print(list((lambda x : x + 10)(range(10))))


# # filter 함수 적용하기(5보다 작은 값 걸러내기)
# map과 동일하다고 생가하면 편할 것 같음. 단일값이 아님
print("=" * 70)
print('\n filter')
filterList = filter(lambda x: x < 5, range(1, 10))
filterList = list(filterList)
print(filterList)


# filter를 map 함수를 이용해서 동일하게 구현
# 람다함수에서 if는 반드시 else가 있어야 한다는 것
listv = list(map( lambda x: x if x < 5 else None, range(0,10)))
print(listv)
listv = [val for val in listv if val]
print(listv)

# 23.09.01 테스트 추가
listtest = [i for i in range(0,100)]
print(listtest)


# 함수를 리스트 형식을 해서 사용도 가능
print("=" * 70)
myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList[0](2, 3))
print(myList[1](2, 3))