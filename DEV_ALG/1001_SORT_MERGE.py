
def mergeSort(listdata):

    if len(listdata) < 2:
        return listdata

    mid = len(listdata) // 2
    left = mergeSort(listdata[:mid])
    right = mergeSort(listdata[mid:])

    res = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    # 양쪽에 나머지 값들을 추가해준다. append하면 안됨. 리스트 자체를 하나의 인자로 추가 함
    res += left[l:]
    res += right[r:]

    return res;

listdata = [7,6,5,8,3,5,9,1]
res = mergeSort(listdata)
print(res)
