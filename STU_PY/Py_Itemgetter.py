from operator import itemgetter

# 예를 들어 가운데 숫로 정렬하고 싶을 때
# 기존 sorted 매개변수에 operator.itemgetter 이것을 인자로 준다
# heapq는 무조건 첫번째 인자만 가능. 이것은 선택이 가능
# 굳이 이런것은 쓸일이 없을 듯 한데
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
    ("sally", 17, 'A')
]

print(students)

result = sorted(students, key=itemgetter(1)) # 처음이면 itemgetter(0)
print(result)

result = sorted(students, key=itemgetter(0)) # 처음이면 itemgetter(0)
print(result)