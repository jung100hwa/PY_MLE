# 삽입정렬

li = [3,5,2,7,10,9,8,1,4,6]

# 일단 한번 찍어보고
for item in li:
    print(item, end='')
    
# 정렬
for i in range(0,len(li)-1):
    j = i
    while(li[j]>li[j+1]):
        temp = li[j]
        li[j] = li[j+1]
        li[j+1] = temp
        if j>0:
            j = j-1
      
# 결과 출력      
print('\n')
for item in li:
    print(item, end='')