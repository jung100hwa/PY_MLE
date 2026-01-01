alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n\n일반적인 for')
for item in alist:
    print(item)

print('\n\n뒤에서부터 출력')
for item in alist[::-1]:
    print(item)


# 아래를 컴프리헨션이라고 함.
print('\n\n리스트 안에 for 내포')
alist2 = [x * 3 for x in alist]
print(alist2)

print('\n\n리스트 안에 for, if 내포')
alist2 = [x*10 for x in alist if x % 2 == 0]
print(alist2)