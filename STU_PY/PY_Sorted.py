# sort는 리스트만 적용, 실제 값을 정렬시킴
# sorted는 모든 이터레이터, 실제 값을 정렬시키지 않고 리턴값
print('=' * 100)
print('\n\n리스트 정렬 리턴')
stList = sorted([5, 2, 4, 3, 6])
print(stList)

# 람다함수와 함께 딕셔너리-마찬가지로 인덱스만 소팅
print('=' * 70)
print('\n\n람다함수와 함께 딕셔너리')
stList = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
stList = sorted(stList, key=lambda x: x[0])
print(stList)

# 내림차순
print('\n\n람다함수와 함께 딕셔너리 내림차순')
stList = sorted(stList, key=lambda x: -x[0])
print(stList)

# 첫번재는 오름차순, 두번째 인수로 내림차순
# 이 부분이 중요!!!!!!!!!!!!!!!!!!!!!!!
print('\n\n람다함수와 함께 딕셔너리 키는 오름차순, 값은 내림차순')
stList = sorted(stList, key=lambda x: (x[0], -x[1]))
print(stList)

students = [
    ('홍길동', 3.9, 2016303),
    ('김철수', 3.0, 2016302),
    ('최자영', 4.3, 2016301),
]

# 성적순으로 정렬
print('\n\n성적순으로 정렬, 숫자만 가능한 듯')
print(sorted(students, key=lambda x: -x[1]))

# keys()로 정렬하면 키값만 표시,이것이 디폴트
print('\n\n딕셔너리 키만 표시')
stList = {3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}
stList = sorted(stList.keys())
print(stList)

# 위에와 같은 결과값
stList = sorted(stList)
print(stList)


# 키와 밸루가 같이 출력된다. 디폴트가 인덱스로 정렬
print('\n\n딕셔너리 키와 값을 같이 출력_집합으로 출력')
stList = {3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}
stList = sorted(stList.items())
print(stList)

#============>디폴트가 키만
stTest ={1:'a', 2:'b'}
print(sorted(stTest))

# 오름차순
stList = {3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}
stList = sorted(stList.items(), key=lambda x: x[0])
print(stList)

# 내림차순
stList = {3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}
stList = sorted(stList.items(), key=lambda x: -x[0])
print(stList)

# 내림차순 2번재
stList = {3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}
stList = sorted(stList.items(), key=lambda x: x[0], reverse=True)
print(stList)

# 딕셔너리에서 첫번째 오름차순, 두번째는 내림차순는 의미없다. 어차피
# 딕셔너리 자체의 키값은 유일해야 한다. 중복된 것은 출력되지 않는다. 그러네


# 학점을 기준으로 내림차순, 이름은 오름차순
students = [
    (3.9, '홍길동', 2016303),
    (3.9, '홍하연', 2016301),
    (3.0, '김철수', 2016302),
    (4.3, '최자영', 2016307),
    (4.3, '최민지', 2016306)
]

listResult = sorted(students, key=lambda x: (-x[0], x[1]))
print(listResult)

# 만약에 학점을 기준으로 내림차순, 이름도 내림차순 일때 아래와 같이 하면 오류남
# 문자는 -x[n] 안됨. 굉장히 중요함.
# students = sorted(students, key=lambda x: (-x[0], -x[1]))

# 이때는 분리하는 수밖에 없는 듯 함
list_sorted = sorted(students, key=lambda x: x[1], reverse=True)
list_sorted = sorted(list_sorted, key=lambda x: (-x[0]))
print(list_sorted)