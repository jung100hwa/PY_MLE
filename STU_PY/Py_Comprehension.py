# 리스트 안에 표현식 for, if 사용이 가능 함. 그러네 이것을 잘 이용하면 될 듯
print("=" * 70)
a = [i for i in range(1,10)]
print(a)

print("=" * 70)
b = list(i for i in range(10,20))
print(b)

print("=" * 70)
c = list(i**2 for i in range(30,40))
print(c)

# if를 사용하기
print("=" * 70)
d = [i for i in range(1,10) if i % 2 == 0]
print(d)

# for문안에 for문 사용(구구단)
print("=" * 70)
i = 1
e = list(i*j for i in range(2,10) for j in range(1,10))
for item in e:
    if i == 10:
        print('\n')
        i = 1
    print(item, end=' ')
    i = i + 1

# map 함수 넣기
print('\n')
print("=" * 70)
f = [1.2, 2.2, 3.3, 4.4]
f = list(map(int,f))
print(f)

print("=" * 70)
g = list(map(str,range(10)))
print(g)

# map 함수 넣기, map(함수, 반복가능한 자료형)
print('\n')
print("=" * 70)
f = [1.2, 2.2, 3.3, 4.4]
f = list(map(int,f)) # f를 정수화 한다.
print(f)

print("=" * 70)
g = list(map(str,range(10)))
print(g)

# 다음은 딕셔너리에 적용해 보자
# 아래는 값에다가 인덱스 즉 로우번호를 같이 출력한다.
print("=" * 70)
word = [('barber', 8), ('secret', 6), ('huge', 5), ('kept', 4), ('person', 3)]

for item, word in enumerate(word):
    print(item, word)

print("=" * 70)
vocab=[('barber', 8), ('secret', 6), ('huge', 5), ('kept', 4), ('person', 3)]
print(vocab)

# 키 밸류이니까 리스트보다 앞에 키값 지정이 하나 더 있을 뿐이다.
# 아래는 키값이 높은 순으로 출력
print("=" * 70)
word_to_index = {word[0] : index + 1 for index, word in enumerate(vocab)}
print(word_to_index)