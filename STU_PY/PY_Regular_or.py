import re

# |은 or의 의미 있고 양쪽을 붙여써야 함. 핵심은 양쪽을 꼭 붙여써야 함.
# todo 여기서 중요한 것은 "문자열1"|"문자열2" 이럴 때 각 문자열 전체와 매칭이 되어야 함
# 각 문자열의 각각의 문자가 아님

text = "Monday Tuesday Friday"
print(re.findall('(Mon|Tues|Fri)day', text))


print('\n==============> |은 or의 의미')
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

################################################## 테스트
# 테스트
p = re.compile('aa|bb')
m = p.match('aabb ccaa')
print(m)

# 테스트
p = re.compile('aa|bb')
m = p.search('aabb ccaa')
print(m)

# 테스트
p = re.compile('aa|bb')
m = p.findall('aabb ccaa')
print(m)
