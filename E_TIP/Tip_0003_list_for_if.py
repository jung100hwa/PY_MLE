"""
리스트 안의 for if 활용하기
"""

alist = [item for item in range(0, 10)]
print(alist)

# for 안의 for
alist = [i * j for i in range(0, 5) for j in range(0, 10)]
print(alist)

# for if문
alist = [i for i in range(1, 11) if i % 2 == 0]
print(alist)

# if문 for => for문이 먼저 실행됨, if else는 for문 앞에 위치
alist = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(10)]
print(alist)

# if else는 for문 앞쪽에 위치
# alist = [i**2 for i in range(10) if i%2 ==0 else i**3]
