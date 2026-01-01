
# 반복가능한 자료를 필터링 하는 함수
# 즉 반복가능한 객체에서 원하는 자료만 가져오기. 이런 함수를 암기할 필요는 없음.
# 사용자 함수로 쉽게 구현됨

# 이렇게 함수로 구현할 수도 있다.
def positive(aList):
    result = []
    for num in aList:
        if num > 0:
            result.append(num)
    return result

print(positive([1, -3, 4]))

# 위의 내용을 filter함수를 이용해서 간단하게 작성. 양수만 리턴
def positive_filter(x):
    return x > 0

print(list(filter(positive_filter, [1, -3, 4])))

# 람다 함수를 이용해서 더 간단하게 작성
# 가독성에 문제가 있기 때문에 가능하면 람다 함수는 쓰지 말자
print(list(filter(lambda x : x > 0, [1, -3, 4])))