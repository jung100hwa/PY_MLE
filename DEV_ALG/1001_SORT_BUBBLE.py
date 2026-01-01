# 버블정렬

li = [3,5,2,7,10,9,8,1,4,6]

for item in li:
    print(item, end='')
    
for i in range(0,10):
    for j in range(0,9-i):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            
print('\n')         
for item in li:
    print(item, end='')