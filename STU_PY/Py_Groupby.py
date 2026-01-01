
# 특정항목을 중심으로 그룹핑 하기
# 이것은 판다스를 이용하는게 훨씬 나을 듯 함
import itertools
import operator

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]

# 리스트 일경우 itemgetter(1) 처럼 인덱스로 접근 가능
data = sorted(data, key=operator.itemgetter('blood'))
print(data)

# 반드시 먼저 소트를 해야 한다. 
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)

print(result)