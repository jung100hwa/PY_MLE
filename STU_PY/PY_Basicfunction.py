# abs
print('\n =====abs')
print(abs(-3))

# eval 식을 실행하는 함수. 중요한건 식이 문자열이라는 것
print('\n eval 함수를 실행')
print(eval('max([1,2,3,4])'))
print(eval('abs(-1)'))


# hex 16진수 리턴
print('\n hex 16진수 출력')
print(hex(3))

# oct 8진수 표기
print('\n hex 8진수 출력')
print(oct(34))

# id 고유의 주소값을 리턴
# 아래는 모두 같은 값을 가짐
# c언어의 주소와 유사
print('\n id 고유의 값을 리턴')
a = 10
b = a
print(id(10))
print(id(a))
print(id(b))


# input
print('\n input')
print('please char insert : ', end='')
a = input()
print(a)


# int
print('\n int')
print(int(3.4))

# 이진수를 십진수로
print('\n int 이진수를 십진수로')
print(int('11',2))

# 16진수를 십진수로
print('\n int 16진수를 십진수로')
print(int('A',16))


#isinstance 클래스 객체인지 아닌지 판단
print('\n class 객체인지 확인')
class Person:pass

a = Person()
b = 3
print(isinstance(a, Person))
print(isinstance(b, Person))


# max 최대값 리턴
print('\n max')
print(max([1,2,3,4]))

# pos 제곱근
print('\n pow')
print(pow(2,3))

# range
print('\n range')
print(list(range(10)))
print(list(range(0,10)))
print(list(range(0,10,2)))

for i in range(0,10):
    print(i)








