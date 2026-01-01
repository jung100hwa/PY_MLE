# 리스트의 내용을 하나로 썸하는 예제

lis = [["aa","bb"],["cc","dd"]]

# []을 붙여줘야 한다.
lis2 = sum(lis,[])

print(lis2)


# 다른 방법 +
print("#" * 50)
print(lis[0] + lis[1])
