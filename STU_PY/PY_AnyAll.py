str = "one two three"
keywords = ["one", "two", "four"]

# 아래와 같은 표현은 정말 가독성이 떨어지는데. 일단 뒤에서부터 해석. 즉 for 문의 결과인 keyword가 str에 하나라도 있으면 참을 리턴
# 즉 앞에 keyword in str 문장을 매번 실행하는 것. 이런 코드는 아니다.
print(any(keyword in str for keyword in keywords))

if any(keyword in str for keyword in keywords):
    print("포함")
else:
    print("미포함")

a = [1,2,3,4,5]
result = all(a)
print(result)

# 0은 false로 인식
b = [1,2,3,4,0]
result = all(b)
print(result)

print('\n =====any2')
aList = [0, '']
print(any(aList))