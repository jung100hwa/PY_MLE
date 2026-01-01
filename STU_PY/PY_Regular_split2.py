import  re

# split는 문장을 주어진 기호로 분리하는 것
# 아래와 같은 문장이 있다고 하면 "공백"으로 분리한다고 하면
text = """100 John PROF
101 James   STUD
102 Mac  STUD"""

# 여기서 '\s+' 핵심, 공백을 " "표시하면 안된다. 공백이 2개 이상 있을 수 있으며 탭도 있을수 있다.
result = re.split('\s+', text)
print(result)