# 어떠한 요소를 지정된 함수로 한꺼번에 처리한다.
# 예를 들면 리스트의 float 요소를 한꺼번에 int, str로 변환한다.

aList = [1.2, 2.2, 3.4]

# 실수를 문자열로 변환
aList2 = list(map(str,aList))
print(aList2)

# 실수를 정수로 변환
aList3 = list(map(int, aList))
print(aList3)

# map안에는 반복가능한 모든 객체를 넣을 수 있다. range로 숫자를 만들어서 넣어 보자
aList4 = list(map(str, range(10)))
print(aList4)

aList=list(map(int, range(10)))
print(aList)

# input 함수를 이용할 경우 문자열로 받아 지는데 이것을 숮자로 변경해보자
# 아래는 입력을 받아야 하기 때문에 잠시 주석 처리
# aList5 = list(map(int, input().split()))
# print(aList5)


# 람다함수와 같이 쓰기
# 아래에서는 lambda x: x ** 2 이것이 변환 함수라고 볼수 있다.
mapList = map(lambda x: x ** 2, range(1, 5))
lstList = list(mapList)  # 리스트 형식으로 변환
print(lstList)

# 아래에서는 3의 배수만 문자열로 바꾸어 보다
# 람다 표현식에 if를 사용하면 만드시 else가 있어야 함. !!!중요
aList = list(range(1,11))
print(aList)
aList2 = list(map(lambda x:str(x) if x % 3 == 0 else x, aList))
print(aList2)


# 반드시 람다에서는 if를 사용하면 else가 있어야 함
# 그리고 항상 얘기하지만 람다 등 이렇게 복잡하게 하면 나중에 디버깅에 문제가 생긴다.
alist = list(i for i in range(0,10))
alist = list(map(lambda x : str(x) + " 3의 배수" if x % 3 == 0 else x, alist))
print(alist)


alist = [['a','b','c'], ['aa','bb'], ['aaa']]
print(len(alist)) # 개수
print(list(map(len, alist))) # map을 쓰면 각 요소계산
print(sum(map(len, alist)) / len(alist))