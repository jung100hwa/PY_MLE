import itertools

# 정말 다양하게 써 먹을 수 있을 것 같음
# 수학적 연산. 확률 등

# 월별 누적수를 출력
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))
print(result)


print('=' * 50)
# 월별 누적하여 최대수를 표시, 예를들면 1월 1, 2월 2, 3월 1이면 3월은 2월값 2...

monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income, max))
print(result)


# 가능한 조합 모두 뽑아내기
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))


# 순서를 고려하지 않고 중복된 것은 제거하고 뽑아내기
arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))



# 랜덤과 유사하게 구간에서 몇개의 조합 뽑아내기
# 역시나 복권 해보기, random 보다 이게 낫네
# 아래는 랜덤이 아니고 그냥 경우의 수를 뽑아낸것으로 보면 됨.

print('=' * 50)

it = itertools.combinations(range(1, 46), 6)
# 이렇게 출력 무한루프. ctrl + c로 정지
# print(list(it))

iIndex = 0 # 지속적 반복을 막기 위해
for item in it:
    iIndex = iIndex + 1
   
    print(str(iIndex) + '===>', end='') 
    print(item)

    if iIndex == 10:
        break


print('=' * 50)

# 만약에 범위 중에 있는 숫자 중복이 가능하다고 보면
it = itertools.combinations_with_replacement(range(1, 46), 6)
iIndex = 0 # 지속적 반복을 막기 위해
for item in it:
    iIndex = iIndex + 1

    print(str(iIndex) + '===>', end='')
    print(item)

    if iIndex == 10:
        break
    
    

import time

# ctrl+c로 중지 가능
def gen():
    for i in itertools.count(1):
        time.sleep(1)
        yield (i, [1] * i)
        

for item in gen():
    print(item)