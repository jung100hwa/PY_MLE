import re

############################################### 이메일 검증 01
# 아래 예제는 이메일 리스트에서 검증하기 위함함
email = ['example@example.com', 'aaa example@example.com', '#abc@emample.com']

p = re.compile('^[0-9a-zA-Z가-힣_.%+-]+@[a-zA-Z.-]+[.][a-zA-Z]{2,}$')

for item in email:
    print(p.findall(item))
    

############################################### 이메일 검증 02
# 하나의 글에서 이메일 뽑아내서 검증
email ="""I mail example@example.com  abc
you mail ==example@example.com bbc
she mail #abc@emample.com ccc
he is 123@naver.com ddd
"""
# (1) 아래과 같이 일단 후보군을 뽑아내고
# todo 후방검색에서 고정길이를 써야 한다. 즉 \s+ 이렇게 하면 안된다.
# p = re.compile(r'(?<=\s)[a-zA-Z0-9가-힣=-_+&^%$#@!~]+@[a-zA-Z.-]+[.][a-zA-Z]+',re.MULTILINE | re.DOTALL)
p = re.compile(r'(?:[a-zA-Z0-9가-힣=-_+&^%$#@!~]+@[a-zA-Z.-]+[.][a-zA-Z]+)',re.MULTILINE | re.DOTALL)

emailList = p.findall(email)
print(emailList)

# (2) 뽑아낸 후보군에서 메일 양식에 맞게 다시 정규화한다.
# 바로 (2)을 실행하면 ==example@example.com --> example@example.com으로 의도치 않은 메일주소로 인식할 가능성이 있다.
p = re.compile('^[0-9a-zA-Z가-힣_.%+-]+@[a-zA-Z.-]+[.][a-zA-Z]{2,3}$')
reList = []
reList = [val for val in emailList if len(p.findall(val))>0]
print(reList)

############################################### 이메일 검증 03
# 위에 방식보다 그룹으로 해버리면 어떨까? 왠만하면 이 방법으로 하자
# 도대체 02방식으로 왜 사용한거야. 좀더 정확도를 높힘. 2번은 많은 사례를 해결할 수 있음
email ="""I mail example@example.com
you mail ==example@example.com
she mail #abc@emample.com
he is 123@naver.com
"""

p = re.compile(r'([0-9a-zA-Z가-힣_.%+-]+@[a-zA-Z.-]+[.][a-zA-Z]{2,3})', re.IGNORECASE | re.DOTALL | re.M)
reList = p.findall(email)
print(reList)


############################################### url 검증 01
# http://가 없는 경우도 고려해야 한다. 이때는 두번 돌리는게 낫다.
url = ['http://www.example.com','https://www.example.com', 'http://www.example.comab123', 'www.example.com']
p = re.compile(r'^(?:http:|https:)[/]{2}[w]{3}.[0-9a-zA-Z가-힣]+.[a-zA-Z]{2,3}$', re.IGNORECASE | re.MULTILINE)
reList=[]
reList=[val for val in url if len(p.findall(val))>0]

reList2 = []
p = re.compile(r'^[w]{3}.[0-9a-zA-Z가-힣]+.[a-zA-Z]{2,3}$', re.IGNORECASE | re.MULTILINE)
reList2 = [val for val in url if len(p.findall(val))>0]

reList =reList + reList2

for item in reList:
    print(item)


############################################### 전화번호 검증 01
# 아래는 일반 전화 검증
phone = ['123-456-7890','a123-123-3456','010-2222-12345']
p = re.compile(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$')
reList = [val for val in phone if len(p.findall(val))>0]

for item in reList:
    print(item)

############################################### 전화번호 검증 02
# 국내 핸드폰 검증을 해보자
phone = ['010-4564-7890','a123-123-3456','010-2222-12345']
p = re.compile(r'^010-[0-9]{4}-[0-9]{4}$')
reList = [val for val in phone if len(p.findall(val))>0]

for item in reList:
    print(item)
    
############################################### 전화번호 검증 03
# 여러문장에 포함되어 있을 때. 역시 그룹을 이용하면 전화번호만 뽑아낼수 있다.
phone ="""I phone 010-2322-1234
you phone1010-2345-4567
she phone 010-2323-12345
"""
p = re.compile(r'(010-[0-9]{4}-[0-9]{4})', re.IGNORECASE | re.DOTALL | re.MULTILINE)
reList = p.findall(phone)
for item in reList:
    print(item)
    
############################################### 전화번호 검증 04
# 전화번호 검증 03에서 010-2323-12345를 걸러내지 못할 수 있다.
# 1234가 아닐 수 있으므로 이런건 삭제한다. 그래서 04방법을 사용한다.
# todo: 이때는 ^ $활용해야 한다.
# 이메일에서 했듯이 2단계 걸쳐서 해보자
phone ="""I phone 010-2322-1234
you phone1010-2345-4567 ddd
she phone 010-2323-12345 abc
"""
# 1단계 후보를 따 뽑아낸다.
p = re.compile(r'(?:010-[0-9]{4}-[0-9]+)', re.IGNORECASE | re.DOTALL | re.MULTILINE)
phoneList = p.findall(phone)
print(phoneList)

reList = []
p = re.compile(r'(^010-[0-9]{4}-[0-9]{4}$)')  # todo: 리스트이니까 ^, $을 적극 활용해야 한다.
reList = [val for val in phoneList if len(p.findall(val))>0]
print(reList)

############################################### 특수문자 검증 01
# _ 언더바는 \W에 포함되지 않는다. 언더바는 특별한 문자이다.
var = 'he$$$llo@%'
p = re.compile(r'[\W_]+')
reList = p.findall(var)
print(reList)

# 특수문자를 없앤다.
ch = re.sub(r'[\W_]+','',var)
print(ch)

############################################### 비밀번호 검증 01
# 대문자, 소문자, 숫자, 특수문자 포함해서 8자 이상
# todo 여기서 핵심 ?=.*[0-9] 의 의미를 알아야 한다. 이것은 처음뿐만 아니라 어느 위치든 0-9문자를 최소한 하나는 포함되어야 한다는 의미이다
# 당연 이해안가지. .*은 0이상의 문자. 즉 abc2, aabad2, abdcdsfe2....이렇게 하다보면 한단어에 숫자가 포함되어 있는지를 알수가 있다.
# 뒤에 [A-Za-z\d@$!%*?&] 는 앞에 참인 것중에 표시하니까 참인 단어만 조사해서 표시하겠지지
# (?=조건)(?=조건)(?=조건)이렇경우 세조건을 모두 만족시키는 단어 이어야 한다.
var = '11he$$$llo33AA@%~~~~'
p = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
reList = p.findall(var)
print(reList)

############################################### 숫자만 있는지 검증 01
# todo 정말 이코드 대박이다. 어떻게 이런 생각을 다 하지
var = ['1234','12ab34','abcd']
p = re.compile(r'^\d+$')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)

############################################### 소문자만 있는지 검증 01
var = ['1234','12ab34','abcd', 'abCD']
p = re.compile(r'^[a-z]+$')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)


############################################### 모든 html 테그 제거 01
# 아래의 의미는 <>안에 <>> 이것을 제외한 모든 문자를 구하고
# 이것으로 sub 한다.
var = '<p>Hello</p>'
p = re.compile(r'(<([^>]+)>)')
reList = p.findall(var)

print(reList) # 일단 한번 찍어보기 [('<p>', 'p'), ('</p>', '/p')] 

print(p.sub('',var)) # 앞에 키값만 사용하나 부네. 'p'도 있는데 얘는 대체가 안된것으로 봐서


############################################### 이메일에서 도메인만 추출 01
# 아래는 '' 마지막에 널이 추출되는데 이것은 내부 그룹 ([_-]?[0-9a-zA-Z]+)* 이것에 대한 값이 없기 때문이다.
var = 'example@example.com'
p = re.compile(r'@([0-9a-zA-Z]+([_-]?[0-9a-zA-Z]+)*[.][a-z]{2,3}$)')
print(p.findall(var))

# 이렇게 하면 된다.
var = ['example@example_kk.com']
p = re.compile(r'@([0-9a-zA-Z]+([_-]?[0-9a-zA-Z]+)*[.][a-z]{2,3}$)')

reList = [item for item in var if len(p.findall(item))>0]
print(reList)

############################################### 이메일에서 도메인만 추출 02
# 정확한 이메일에서 도메인만 추출할 때 아래와 같이 간단하게 할 수 있다.
var = 'example@example.com'
p = re.compile(r'@(.+)')
print(p.findall(var))

############################################### 이메일에서 추출 03
# todo -문자 뒤에 특수문자가 오면 컴파일러가 인식을 못함. 이문자는 가능하면 맨 나중에 쓰자.
# 도메인에 점이 올 수 없다는 가정함
var = ['example@example.com','example@example.com.aaa','example@example.com.aaaaaaa','**@exampl.com']
p = re.compile(r'[0-9a-zA-Z]+([._-]?[0-9a-zA-Z]+)*@[0-9a-zA-Z]+([_-]?[0-9a-zA-Z]+)*[.][a-z]{2,3}$')

reList = [item for item in var if len(p.findall(item))>0]
print(reList)


############################################### 주석을 제거해보자 01
# *? 라는 탐욕적 표현이 사용 됨. 즉 /* 다음에 첫번째로 나오는 */까지 선택하라는 의미이다.
var = '/* this is a comment */ var x = 10'
p = re.compile(r'\/\*[\s\S]*?\*\/')
var = p.sub('',var)
print(var)

############################################### 숫자만 추출 01
var = 'Hello123'
p = re.compile(r'[0-9]+')
# p = re.compile(r'([0-9])+')   # todo 이렇게 그룹을 하면 하나의 숫자만 나온다.
# p = re.compile(r'(?:[0-9])+') # 그룹을 할려면 이렇게 해서 123이 다 나오도록 해야 한다.
print(p.findall(var))

############################################### 신용카드 형식 검사 01
var = ['1234-5678-9012-3456','1234-5678-901-3456','1234-5678-9012-34a6']
p = re.compile(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)

############################################### 날짜 01
# 쉬운줄 알았는데 그렇지 않음, 특히 ^, $을 잘 활용해야 함.
var = ['12/31/2023','12/31/20234','12/313/2023']
p = re.compile(r'(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/[0-9]{4}$')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)

############################################### 유효한IP 검증 01
# 머리좋은 사람 많구나.
# 카드 넘버드 번호검색은 이렇게 자리수로 끊어야 한다.
var = ['192.168.0.1','192.168.0.900','192.168.0..1']

# 이것은 255.을 앞에 3개로 검색
p = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

# 애는 .255를 뒤에 3개로 검색
# p = re.compile(r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}')
reList = [item for item in var if len(p.findall(item))>0]
print(reList)