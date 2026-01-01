from copy import deepcopy
import numpy as np

print("=" * 50)
print("깊은 복사와 얕은 복사")

# 단순복사(참조의 의미)
aList = [1,2,3,['a','b','c']]
aList2 = aList
aList2[0]= 100
print(aList2)
print(aList)


# 얕은 복사
aList = [1,2,3,['a','b','c']]
aList2 = aList[:]
aList2[0]= 100
print(aList2)
print(aList)


aList = [1,2,3,['a','b','c']]
aList2 = aList.copy()
aList2[0]= 100
print(aList2)
print(aList)


aList = [1,2,3,['a','b','c']]
for item in aList:
    # 안에 타입을 검사할 때는 str()
    if str(type(item)) == "<class 'list'>":
        for itemD in item:
            print(itemD)
    else:
        print(item)


print("=" * 50)
print("리스트 연산")
aList = [1,2,3]
bList = [4,5,6]
print(aList + bList)
print(aList * 5)   # 5번 반복이다는 의미이다. 각 요소에 5를 곱하는게 아님


print("=" * 50)
print("특정값 바꾸기")
aList = [1,2,3]
aList[2] = 4
print(aList)


print("슬리이스 상태로 값바꾸기")
aList = [1,2,3]
aList[1:2] = ['a','b','c'] #1번
print(aList)


# 슬라이스와 차이 구별. 이것은 인덱스에 해당하는 자리에 리스트 자체를 넣는다.
print("특정인덱스에 리스트 넣기")   #슬라이스 형태일 때하고 완전 다름
aList = [1,2,4]
aList[1] = ['a','b','c'] # todo 1번 수정과 전혀 다른 값
print(aList)


print("=" * 50)
print("뒤에 값 추가")
aList = [1, 2, 3]
print(aList)


print("뒤에 리스트를 추가")
aList.append([5,6]) # 하나의 요소에 리스트를 추가
print(aList)

aList.append(11)

print(aList)

####################################################### 250926
aList2 = []
str1="aaa"
str2="bbb"
str3="ccc"
str4="ddd"
aList = [str1, str2]
aList2.append(aList)
aList = [str3, str4]
aList2.append(aList)
print(aList2)



print("=" * 50)
print("리스트 정렬-리스트 자체 정렬")
aList = [1,3,2]
aList.sort() # 값자체가 정렬됨
print(aList)


print("리스트 정렬-리스트 원본은 정렬되지 않음,정렬된 리턴값")
aList = [1,3,2]
bList = sorted(aList) # 원본값을 변함이 없음
print(aList)
print(bList)


print("=" * 50)
print("역으로 정렬")
aList = [1,2,3]
aList.reverse()  # 내림차순이 아닌 그냥 역으로 정렬
print(aList)


print("=" * 50)
print("끼워넣기")
aList = [1,2,3]
aList.insert(2,[4,5])
print(aList)


print("=" * 50)
print("리스트 원소 삭제")
aList = [1,2,3,4,53,4]
aList.remove(4) # 처음나오는 4를 삭제, 인덱스가 아님!!!
print(aList)


# 리스트안에 comprehension을 잘 보자. for 문을 리스트 안에 넣어서 리스트로 리턴하게 만드네.
print("리스트에 특정 숫자를 모두 삭제해보자")
aList =[1, 2, 1, 3, 4, 5, 2, 3, 3, 4, 5, 5, 3, 2, 2, 2, 100]
aList2 = [x for x in aList if x != 2]
print(aList2)


print("=" * 50)
print("마지막 요소를 리턴하고 삭제")
aList = [1,2,3]
i = aList.pop() # 마지막 요소를 리턴하고 리스트에서 삭제
print(i)
print(aList)


print("지정한 인덱스를 삭제")
aList = [1,2,3]
i = aList.pop(2) # 해당 인덱스에 해당하는 값 삭제
print(i)
print(aList)


print("=" * 50)
print("특정 값이 몇번 들어있느지 개수 구하기")
aList = list(range(0,10))
print(aList)
print(aList.count(1)) # 1이 몇번 들어있는지 카운드
print(len(aList))     # 전체 요소 수

#########################################sum 함수를 이용한 리스트 안의 리스트를 전체 하나의 리스트로
strList = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'],
           ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'],
           ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber','kept', 'secret'],
           ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'],
           ['barber', 'went', 'huge', 'mountain']]

strList2 = sum(strList, [])
print(strList2)

# extend는 통째로 리스트를 추가
resultList = ['aaa','bbb']
resultList.extend(strList)
print(resultList)

# 이렇게 튜플 형태를 리스트에 추가
numbers = [1, 2, 3]
numbers.extend((4, 5))  # 튜플을 사용
print(numbers)

numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)


alist =[[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(alist)
print(arr)
print(arr[0:1])


aList = [1,2,3]
aa = alist.count(4)
print(aa)