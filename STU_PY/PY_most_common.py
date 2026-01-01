# most_commont 함수는 등장 빈도수가 높은 상위 n개 단어만 저장, 거의 Counter 함수를 사용, 이게 딕셔너리지 형태지만 파이썬의 디셔너리와는 약간 차이
# 리스트에 담긴 튜플 형태로 리턴

from collections import Counter

# Counter 함수는 리스트에서 빈도수를 같이 포함한 딕셔너리를 리턴. 이때 정렬까지 함
# most_common는 단지 상위 몇개를 리턴 할 것인가. 튜플 형태로
li = ['aaa', 'ccc', 'bbb', 'bbb', 'bbb', 'aaa']
co = Counter(li)
print(co)
print(co.most_common(2))

# Counter 함수는 아래와 같이 이미 딕셔너리 형태인 것도 캐스팅해서 사용할 수 있음. 이때로 값을 보고 자동 정렬 함
li = {'bbb':5, 'ccc':2, 'aaa':3, 'ddd':4}
print(Counter(li).most_common(2))