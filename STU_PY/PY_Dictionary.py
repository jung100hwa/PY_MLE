
print('\n dictionary 조회')
d = {1:'a', 2:'b', 3:['a','b','c']}
print(d)

# 조회(인덱스가 아니라 키로 찾는다)
print('\n인덱스가 아니라 키로 조회')
print(d[2])
# print(d[0]) # 이것은 값이 존재하지 않는다. 인덱스가 아니라 키값임을 잊어서는 안된다.!!!!

# 추가
print('\n특정값 추가')
d[4] = 'abc'
print(d)

# 키값을 통한 값 얻기
print('\n키에 해당하는 값 for')
for item in d.keys():
    print(d[item])

# 그냥 값만 불러오기
print('\n값만 불러오기')
for item in d.values():
    print(item)

print(len(d.values()))

# 키와 값 같이 얻기
print('\n키와 값을 같이 불러오기')
for key, val in d.items():
    print("key = %s, value = %s" %(key, val))

# 키가 존재하는 조사(value는 이렇게 못한다)
print('\n키가 존재하는지 조사')
if 2 in d:
    print('ok')
else:
    print('no')
    

#  value값에 해당하는 리스트가 아닌 반복객체. 즉 리스트 함수를 사용할 수없다.
#  사용하기 위해서는 리스트로 치환해야 한다.
print('\n 리스트로 치환')
d = {1:'one', 2:'two', 3:'three'}
g = d.keys()
print(g)


#  리스트로 변경하기
g = list(g)
g.append(100)
print(g[3])
print(g)


# get 함수를 사용하여 값을 얻기. 해당 키에 해당하는 값이 없을 경우 디톨트 값을 리턴할 수 있게 한다.
# get의 두번째 인자가 없으면 출력하는 디폴트값
d = {1:'one', 2:'two', 3:''}
print(d.get(4,'no'))
print(d.get(2,'N/A'))