# 이진 탐색, 이미정렬된 순차열에서 어떠한 숫자를 찾거나 새로 삽입할 위치를 찾는다.
import bisect

alist = [1,3,4,4,6]

# 4를 삽입할려고 할때 삽입가능한 위치의 가장 왼쪽을 반환
# 인덱스를 반환한다. 숫자가 아닌
index = bisect.bisect_left(alist, 4)
print(index)

# bisect.bisect_right 동일
index = bisect.bisect(alist,4)
print(index)

# 리스트 a에 x를 삽입합니다. 리스트 a가 이미 정렬되어 있다고 가정합니다. 
# 만약 리스트 a 내에 x가 이미 존재하는 경우, x를 리스트 a 내에서 가장 오른쪽 위치 시킨다.
a = [1,2,4,6]
bisect.insort_right(a,3)
print(a)

# bisect.insort_right 동일
a = [1,2,3,4,6]
bisect.insort(a,3)
print(a)

aList = [33, 99, 77, 70, 89, 90, 100]

# 100점 이상 : A
# 80점 이상 : B
# 70점 이상 : C
# 60점 이상 : D
# 0~59점 : F

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수가 정렬되어 삽입될 수 있는 포지션을 반환
    print(pos) # 인덱스를 반영한다. 즉 각 단계의 사이값 순서(0,1,2,3,4)

    # 아래 코드는 머리가 좋은데 굳이 이렇게 하지는 말자. 구해놓고 평점을 구하면 되지. 이무슨..
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)