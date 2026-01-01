# 선택 정렬 구현
li = [3,5,2,7,10,9,8,1,4,6]

index_a = 0
index_b = 0
index_min = 0
temp = 0

# 일단 한번 출력
for item in li:
    print(item, end='')

for index_a in range(0,len(li)):
    minv = 9999  # 일단 임의 최대값

    for index_b in range(index_a, len(li)):
        # 가장 적은 값을 담는다.
        if minv > li[index_b]:
            minv = li[index_b]
            index_min = index_b

    # 스와핑
    temp = li[index_min]
    li[index_min] = li[index_a]
    li[index_a] = temp

# 제대로 선택정렬이 되었는지 확인
print('\n제대로 되었는지 확인')
for item in li:
    print(item, end='')