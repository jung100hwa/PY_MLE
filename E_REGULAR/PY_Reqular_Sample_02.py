# 여기는 주로 문제 위주로 작성
import re
##################################################################################
# 문제 : colour, Color, color 등 모든 버전의 color에 일치되는 정규식을 작성하라.
# 즉 아래에 제시하는 모든 단어는 color로 본다는 것이다.
var = ['colour', 'Color', 'color']

p = re.compile(r'\bcolou?r\b', re.IGNORECASE)  # 경계는 영어일때만 가능 함
reList = [item for item in var if len(p.findall(item))>0]
print(reList)


##################################################################################
# 문제 : cat에는 일치되지 않고, cat을 포함하면서 그보다 긴 단어, staccato, cats, tomcat 등에 일치되는 정규식을 작성하라.
var = ['cat', 'staccato', 'cats', 'tomcat']

# 이렇게 되면 안되는데 어떤 사이트에는 이렇게 있네. 이런경우는 가운데 포함된 경우만
# var = 'cat staccato cats tomcat'
# p = re.compile(r'\Bcat\B')
# print(p.findall(var))

# 이렇게 해야 되지 않나
p = re.compile(r'(.*cat.+)|(.+cat.*)|(.+cat.+)')

reList = [item for item in var if len(p.findall(item))>0]
print(reList)


##################################################################################
# 문제 : 이번에는 특정 단어를 제외시켜 보자. reg를 제외한 모든 단어에 일치되도록 하는 정규식을 작성하라.
# 즉 정확한 reg만 있는것을 제외하고 나머지 선택
var = 'reg stacrego regs tomreg'
p = re.compile(r'\b(?!reg\b)\w+')  # re.compile(r'\b(?!reg)\b\w+') 이렇게 \b ( ) 밖으로 나오면 안됨. todo \w은 소비하지 않은 문자를 출력하닌가
print(p.findall(var))


var = ['reg', 'stacrego', 'regs', 'tomreg']
p = re.compile(r'(.*reg.+)|(.+reg.*)|(.+reg.+)')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)

##################################################################################
# 문제 : 이번엔 특정 단어뿐 아니라 그 단어를 포함하는 단어도 제외시켜 보자. reg뿐만 아니라 regex, register, dreg 등은 모두 제외되어야 한다.
var = 'reg stacrego regs tomreg tomre'

# 이럴경우는 무조건 시작단어가 reg만 아니면 첫번째 조건은 통과한다.
p = re.compile(r'\b(?!reg)\w+\b')   
# p = re.compile(r'\b(?!reg\b)\w+')
print(p.findall(var))


# 아래와 가로가 중복할 때는 바깥쪽 가로가 단어하나를 의미하고 안쪽 가로의 조건을 하나의 단어에서 찾는다.
# 이게 우리가 원하는 답이다.
p = re.compile(r'\b(?:(?!reg)\w)+\b')
# p = re.compile(r'\b((?!reg)\w)+\b')
print(p.findall(var))

# 여기서 reg가 나오는 것은 "reg"를 소비하지 않고 다음조건의 시작점의 대상이기 때문. [a-z]+ 대상이기 때문
var = 'regaaa stacrego regs tomreg tomre reg'
p = re.compile(r'\b(?=reg)[a-z]+\b')
print(p.findall(var))

# 아래의 의미를 잘알아야 한다.
var = 'reregaa reg reba rereg ----'

 # todo (?:.....\w)+ 이 자체는 ....이 부분을 단어단위로 그룹이 아닌 일반 검색처럼 만든다.
 # 문자열 전체로 비교하지 않고 단어하나하나 비교한다. 
 # 그룹이 중첩일때 바깥쪽 그룹이 False이면 안쪽은 평가하지 않는다.
 # 그러니까 reg가 어느 위치에 있든 상관이 없는 것이다.
p = re.compile(r'\b(?:(?!reg)\w)+\b') 
print(p.findall(var))