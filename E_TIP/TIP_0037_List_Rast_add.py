# 리스트 안에 리스트가 있는 경우 마지막 리스트에 어떠한 값들을 추가하는 방법

n = 10

result = []
for i in range(n):
    result.append([])
    
    for j in range(n):
        result[-1].append(str(i)+'-'+str(j)) # 정말 똑똑한 사람들 많네
print(result)


# 지금까지는 이렇게 했겠지. 성능의 문제가 없으면 이것도 괜찮지
result = []
for i in range(n):
    imsi = []
    for j in range(n):
        imsi.append(str(i)+'-'+str(j))
    result.append(imsi)
    
print(result)