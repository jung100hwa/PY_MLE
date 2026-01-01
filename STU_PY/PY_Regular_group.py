import re

# ()로 묶어주면 순서에 따라.1,2,3...그룹인덱스가 먹여 진다
# 복잡한 정규식에 사용하면 유용

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")
print('\n그룹으로 산출해서 인덱스로 추출하기')
print(m.group(1))
print(m.group(2))


# 그룹명을 이름으로 줄 수 있다 이 방법은 가급적 사용하지 말자. 너무 복잡해진다.
# 이렇게 할 이유가 없다. 인덱스로 하면되지 이름까지...
p = re.compile(r"(?P<name>\w+)\s+\d+[-]\d+")
m = p.search("park2 010-1234-5678")
print(m.group("name"))