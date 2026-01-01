import re
from PY_PKG import SU_RE_HANDLING as srh

######################################################################### r를 써야만 하는 이유
txt = "Abc and abc is good"
print(txt)
print(re.findall('abc',txt))


# 만약에 '\n' 이라고 하면 리턴, r'\n' 그냥 문자열
# todo 그런데 \s는 적용되지 않는다. \s 이스케이프 대상이 아니다.
# https://velog.io/@yoopark/r-prefix-in-regexp 탈출문자에 대해 정의한 곳 참조
ss = "Abc and ab\nd is good"
print(ss)


ss = r"Abc and ab\nd is good"
print(ss)


text = "Abc and ab\sd is good" # \s하나의 문자에 불과함.
print(text)


print(re.findall('ab\sd',text))        # \s를 스페이스로 인식
print(re.findall(r'ab\sd',text))       # \s를 스페이스로 인식
print(re.findall('ab\\sd',text))       # \s를 스페이스로 인식. todo : 파이선엔진만 \\->\로 자동변경
print(re.findall(r'ab\\sd',text))      # \s를 문자로 인식
print(re.findall('ab\\\\sd',text))     # \s를 문자로 인식
# https://velog.io/@kim-mg/Python-re%EC%A0%95%EA%B7%9C%EC%8B%9D-%EC%97%B0%EC%82%B0-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
# 참정리 잘 해놨다.


######################################################################### re의 옵션들
# re.DOTALL개행문자도 하나의 문자로 취급
print(re.findall(r'a..', 'abc a  a\na'))                # 점(.) 개행문자를 제외한 모든 문자와 대응. 공백도 포함됨
print(re.findall(r'a..', 'abc a  a\na', re.S))          # 개행문자도 점(.)으로 대응
print(re.findall(r'a..', 'abc a  a\na', re.DOTALL))
print(re.findall(r'(?s)a..','abc a  a\na'))          # 인라인 플래그를 써서 출력


# IGNORECASE 대소문자 구분없이 사용
print(re.findall(r'abc', 'abc AB cc ABC', re.IGNORECASE))
print(re.findall(r'abc', 'abc AB cc ABC', re.I))
print(re.findall(r'(?i)abc', 'abc AB cc ABC'))       # 인라인 플래그를 써서 출력


# re.MULTILINE 멀티라인에 적용. 단지 ^, $ 일때만 효과
text = """
ABc and abc is good.
abc and Abc is good.
"""
print(re.findall(r'^abc',text))                      # 일치결과 없음
print(re.findall(r'^abc',text, re.IGNORECASE))       # 일치결과 없음, 두번째 줄 ABc가 나오지 않음. 이것도 다음줄
print(re.findall(r'^abc',text, re.IGNORECASE | re.MULTILINE))       # 이것이 원하는던 결과
print(re.findall(r'(?im)^abc',text))                 # 인라인 플래그를 조합해서 | 와 같은 효과를 나타탬


# 인라인 플래그 테스트
print(re.findall('(?s)a..', 'abc a  a\na'))         # \n를 문자로 취급
print(re.findall('(?is)a..', 'ABc Adb  a\na'))      # \n를 모두 문자로 취급하고 대소문자도 가리지 않음


# 인라인 플래그를 써서 특정 부위만 적용 할 수 있음.         # todo 멀티라인 속성이 없어도 ^, $를 제외하고는 다 인식함, s옵션을 안줘도 상관없음
print(re.findall('(?im:abc) and abc is good',        # todo 인라인 플래그의 진정한 위력. 파이썬3.7 부터 중간에 두면 오류
'''
ABc and abc is good.
abc and Abc is good.                                 
'''))


# todo 이렇게 하면 해당되는 것 다 나옴. (?i:abc) 하고 차이가 있음
# todo 이렇게 하면 문장 전체, 위에 문장하고 차이가 있음
print(re.findall('(?i)abc and abc is good',
'''
ABc and abc is good.
abc and Abc is good.                                 
'''))


# 아래는 오류가 난다. 인라인 플래그는 앞에만 둬야 한다. 파이썬 버전 3.7부터..
# print(re.findall('a.. and (?i)abc is good',
# '''
# Abc and abc is good.
# abc and Abc is good.
# '''))


# re.VERBOSE 이것은 정규식을 알아보기 쉽게 하기 위해 사용한다. 예를들어
text = "ab123c and Abc is good"
m = re.compile('[a-z]+[0-9]+')
print(m.findall(text))


# 위에 식이 너무 복잡함(현재는 간단하지만...), 아래와 같이 하면 가독성이 뛰어남
text = "ab123c and Abc is good"
m = re.compile(r"""
    [a-z]+
    [0-9]+
    """,
re.VERBOSE)
print(m.findall(text))


######################################################################### ? + *
# ?, * 는 차이가 있다. 똑 같은게 아님. ? findall 찾으면 한문자씩 출력됨. * findall 찾으면 만족하는 문자열까지 출력
data = "ab1c12DD"


# ? 0개 또는 1개, 아닌것도 리스트에 ''로 표시됨
p = re.compile("[a-z]?", re.IGNORECASE)
print(p.findall(data))


# + 한개 이상, 아닌것은 리스트에 없음, 그러니까 대부분 이것만 사용해야 함.
p = re.compile("[a-z]+", re.IGNORECASE)
print(p.findall(data))


# 0개 이상, 문자열, 아닌것도 리스트에 표시됨
p = re.compile("[a-z]*", re.IGNORECASE)
print(p.findall(data))


# {n} 앞의 패턴이 n번 반복, 아닌것은 리스트에 없음
p = re.compile("[a-z]{2}", re.IGNORECASE)
print(p.findall(data))

########################################################################## match
# todo 첫번째 문자열에서 패턴이 일치하는 첫번째 문자열 리턴.
# 가능하면 search를 사용하자. group 함수를 쓰기도 search가 낫다.
data = "aab bbb ccc ddd aaa"
p = re.compile("[a]+", re.IGNORECASE)
print(p.match(data))  # 처음 aab 중 aa출력


# 아래는 값이 없다.
data = "ccb aab bbb ccc ddd aaa"
p = re.compile("[a]+", re.IGNORECASE)
print(p.match(data))  #


######################################################################### search
# todo 문자열 전체에서 패턴이 일치하는 첫번째 문자열 리턴.

data = "aab bbb ccc ddd aaa"
p = re.compile("[a]+", re.IGNORECASE)
print(p.search(data))  # 처음 aab 중 aa출력


# match와 다르게 아래는 값이 있다.
data = "ccb aab bbb ccc ddd aaa"
p = re.compile("[a]+", re.IGNORECASE)
print(p.search(data))  # aab 중 aa 출력


######################################################################### findall
# 문자열 전체에서 일치하는 것을 리스트형식으로 보여주는데 중요한것은 그룹단위이다. 그룹은 ()으로 정의된다.
# 만약에 그룹이 지정되지 않으면 상관없지만 그룹이 지정되면 그룹과 일치하는 것을 보여준다.
# todo findall에서 그룹이 없으면 기본을 출력하지만 그룹이 있으면 기본을 출력하지 않고 그룹만 출력한다.그룹이 필요없으면 (?:) 해주면 된다.
# 보여 주는 것만 그룹을 보여주지 조건은 전체가 만족되어야 한다.

data = "VVhgl TThgl"
p = re.compile("[V]+(hgl)", re.IGNORECASE)
print(p.findall(data))  # 이때는 hgl이 그룹으로 지정되어 있기 때문에 VVhgl이 아닌 hgl만 출력됨


# 아래는 왜 쓰는 거야!!
p = re.compile("[V]+(?:hgl)", re.IGNORECASE) # 그룹이 아닌 포함된 문구 전체를 출력력
print(p.findall(data))


# 아주 중요함 다음 문장을 6자씩 끊어서 결과보여주기. point(.) 6개 정의하면 됨
text = "Regular expressions are powerful!!! "
print(re.findall(r'......', text))


text = "abc adc aec afc"
p = re.compile('a(b|d)c')
print(p.findall(text))          # todo 이렇게 하면 그룹으로 지정된() b,d만 출력


p = re.compile('a(?:b|d)c')     # 이렇게 그룹을 해제하면 그룹의 역할을 하면서 abc adc 출력
print(p.findall(text))


p = re.compile('a[bd]c')       # 이렇게 해도 그룹이 아닌 형태로 출력 []안은 무조건 or의 개념이다
print(p.findall(text))


######################################################################### finditer
# 결과를 반복자로 넣겨줌. for문을 통해서 하나씩 꺼내야 함
data = "VVhgl1 TThgl2"
p = re.compile("(hgl1|hgl2)", re.IGNORECASE)
iter = p.finditer(data)
for item in iter:
    print(item.group())  


######################################################################### group
data = "VVhgl TThgl"

p = re.compile("[V]+hgl", re.IGNORECASE)
print(p.findall(data))  # 이때는 VVhgl 다출력 됨


# 우리가 출력하고자 하는 것은 결고 hgl 이다. 이때 쓰이는 것인 ()
# 아래의 예를 보면서 비교. 즉 findall()도 group의 개념을 이미 내포 했음, 즉 group 여러개 있으면 모두 표시. 예제를 보면서
# group(), group(0)은 매칭되는 전체 문자열을 보여주고, group(1), group(2) 딱 ()보여줌
p = re.compile("[V]+(hgl)", re.IGNORECASE)
print(p.findall(data))


################################### 25.03.02 추가
# "\g<1>" 이것은 하나의 그룹을 나타냄. re가 아닌 p임으로 인자는 2개이다.
# 컴파일해서 전체을 첫번째 문구로 교체한다는 의미이다. 즉 data에서 ===> [V]+(hgl)\s[T]+(hgl)를 \g<1>-aaa 교체한다는 것이다.
data = "VVhgl TThgg vvtt"
p = re.compile("[V]+(hgl)\s[T]+(hgg)", re.IGNORECASE)
print(p.findall(data))


print(p.sub("\g<0>-aaa", data)) # 그룹전체에 -aaa 추가
print(p.sub("\g<1>-aaa", data)) # data 중에서 그룹에 해당되는 문구를 "첫번째 그룹-aaa"교체
print(p.sub("\g<2>-aaa", data)) # data 중에서 그룹에 해당되는 문구를 "두번째 그룹-aaa"교체



print(p.sub("ssss", data))  # data 문장에서 그룹을 모두 ssss 문자로 바꾼다.

# todo re모듈에서 \1은 첫번째 그룹명을 말한다. p에서 \g<1> 동일하다.
# 즉 sub 해당단어를 없애고 대체하는데 \1의미는 없애지 말고 대체만 하라는 의미
sent = "I am? boy."
sent = re.sub(r"([?.!,¿])", r"=\1", sent)
print(sent)

###################################


m = p.match(data)
print(m.group())
print(m.group(0))
print(m.group(1))

##############################################  24.12.28 간단한 예제
data = '''
a-hgl is b-hgl is c-hgl is d-hgl is
ak-hgl bj-hgl ci-hgl dp-hgl
'''
# 아래는 포함된 단어가 리스트로 출력 된다.
p = re.compile(".{2}(?:hgl)", re.IGNORECASE | re.MULTILINE)
print(p.findall(data))


# todo 이렇게 해버리면 .+ 2개가 리스트로 출력된다. 마지막 hgl앞에 있는 모든 문자로 선택된다. 단 제일 뒤에 is는 출력이 되지 않는다.
p = re.compile(".+(?:hgl)", re.IGNORECASE | re.MULTILINE)
print(p.findall(data))


p = re.compile(".+(hgl)", re.IGNORECASE | re.MULTILINE)
print(p.findall(data))
##############################################


# findall의 동작을 보면 () 그룹만 보여준다. 뒤에 숫자가 있음에도 불구하고
data = "aa VVhgl1651kk TThgl"
p = re.compile(r'[V]+(hgl)+(\d{4})+([k]+)', re.IGNORECASE)
print(p.findall(data))  # 그룹에 해당되는 것을 다 보여준다


m = p.search(data)      # match를 쓰면 data에 첫번째 문자열만 검색함에 따라 아래 문장들이 오류가 발생한다.
print(m.group())        # group(), group(0)은 매칭되는 문자열 전체를 보여준다.
print(m.group(0))
print(m.group(1))       # 첫번째 그룹만 보여줌. 즉 'hgl'
print(m.group(2))       # 두번째 그룹만 보여줌 . 즉 '1651'
print(m.group(3))       # 세번째 그룹만 보여줌 . 즉 'kk'


# 이번에는 그룹이 (), () 이런 구조가 아니라 (()) 즉 가로 안에 가로가 있는 구조 형식
# 이럴때가 더 많을 것으로 판단됨. 밖깥쪽 ()group1, 안쪽 ()가 group2...이런식으로 된다.
p = re.compile(r'[V]+(h(g)l)', re.IGNORECASE)
print(p.findall(data))  # 그룹에 해당되는 것을 다 보여준다


m = p.search(data)
print(m.group())        # 전체를 보여준다. 즉 VVhgl
print(m.group(0))       # 전체를 보여준다. 즉 VVhgl
print(m.group(1))       # 전체를 보여준다. 즉 hgl
print(m.group(2))       # 전체를 보여준다. 즉 g


# 아래와 같이 그룹이 여러개 이고 각 그룹안에 그룹이 있을 때 앞에서 부터 순차적으로
# 가장 쉬운 방법은 findall로 찍어보면 앞에서부터 group(1), group(2)....
p = re.compile(r'[V]+(h(g)l)+(\d{4})+([k]+)', re.IGNORECASE)
print(p.findall(data))  # 그룹에 해당되는 것을 다 보여준다
m = p.search(data)
print(m.group())        # 전체를 보여준다.
print(m.group(0))       # 전체를 보여준다.
print(m.group(1))       # 전체를 보여준다. 즉 hgl
print(m.group(2))       # 전체를 보여준다. 즉 g
print(m.group(3))       # 전체를 보여준다. 즉 1651
print(m.group(4))       # 전체를 보여준다. 즉 kk


# 이름과 전화번호 예를 한번 보자, 다음은 그룹이 2개로 이루어져 있다.
p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search("park 010-1234-5678")


if m:
    print(m.group(1))       # 이름
    print(m.group(2))       # 전화번호만
else:
    print("매칭값 없음")


# 아래와 같이 그룹명을 줄 수 있는데 이렇게 하지 말자. 복잡해 진다.
p = re.compile(r"(?P<name>\w+)\s+\d+[-]\d+")
m = p.search("park2 010-1234-5678")
print(m.group("name"))


######################################################################### ^ 시작문자열
# 시작문자열 의미, []안에 있으면 not을 의미
print(re.search('^Life','Life is to short'))
print(re.search('^Life','Lifes is to short'))


# 아래는 찾지 못한다.
print(re.search('^Life','My Life is to short'))


# 멀티라인 옵션을 사용한다. 옵션을 연결할때는 | 이것을 사용한다.
p = re.compile('^Life',re.MULTILINE | re.IGNORECASE)
data = """python one
life is too short python two
you need one
Life three Lifes is too short"""

print(re.findall(p,data))


rstr = p.findall('My \nLife is too short')
print(rstr)

data = """python one
life is too short
python two
you need python
python three"""

# python으로 시작하고(^) 화이트스페이스가(\s) 있고 뒤에 하나 이상의 문자{\w)가 와야 함
# 그룹이 없기 때문에 전체 해당 문자열을 출력한다.
p = re.compile(r'^python\s\w+', re.MULTILINE)
print(p.findall(data))


# []안에 있을 때에는 not에 의미 이다. 하나의 문자 다음에 a b c 문자가 포함되지 않은 것
p = re.compile('.[^abc]')
data = 'python one'

rstr = p.findall(data)
print(rstr)


######################################################################### $ 끝문자열
strdata = "life is too short"
if re.search('short$', strdata):
    print("exist")
else:
    print("not exist")

# 멀티라인에서
data = """python one
life is too short python two
you need one
python three"""

# print(data)

# 멀티라인 옵션이 있어야 함. 만약에 data = "python one" 이러면 멀티라인 속성이 없어도 됨
if re.search("one$",data, re.MULTILINE):
    print("exist")
else:
    print("not exist")


######################################################################### [] 안의 문자
# [] 중괄호 안의 문자와 일치 여부. []안에 있으면 무조건 문자 그자체이다.
# todo [] 안의 문자는 각각 OR의 성격

text = "How do you do"
print(re.findall('[oyu]', text))
print(re.findall('[dH].', text)) # findall은 그룹단위인데 여기서는 그룹()이 없기 때문에
print(re.findall('[dH].+',text))


# 점(.)은 []밖에서는 하나의 문자를 의미 하고 [.] 안에서는 점(.)자체이다.
# acb는 매칭되지 않는다. []안에 있기 때문에 점(.) 자체를 의미하고 acb는 점(.)이 없다.
p = re.compile('a[.]b')
m = p.match('acb')
if m:
    print(m.group())
else:
    print("no matching")


# 아래는 매칭된다. 점(.)이 있기 때문이다.
m = p.match('a.b')
if m:
    print(m.group())
else:
    print("no matching")

# 이것은 oy, oo,ow,wy,wo,ww,yy,yo,yw가 있는 것을 의미 함
# 이렇게 코딩하면 안된다. 예를 위한 문장
print(re.findall('[owy][yow]',text)) 


# re.IGNORECASE는 대소문자 관계없이
p = re.compile('[a-z]', re.IGNORECASE)
m = p.match('1bc def')  # match 첫번째만 비교하고 있으면 첫번째만 리턴, 없으면 None
if m:
    print(m.group())
else:
    print("no matching")


# 아래는 매칭된다.
p = re.compile('[a-z]',re.IGNORECASE)
m = p.match('abc ddd') # a, b, c, d, d,d 다 매칭되지만 첫번째만 비교하고 값을 리턴한다.
if m:
    print(m.group())
else:
    print("no matching")


# 한글 매칭
text = "I Love 허 길 양"
reList = re.findall("[가-힣]", text) # 하나의 문자씩 출력한다.
print(reList)

######################################################################### 점(.)
# 하나의 문자를 의미.
# [] 안에서는 점(.) 자체를 의미 한다.

# 하나의 문자를 의미
p = re.compile('a.b')
m = p.match('abb')
print(m.group())


# 다음 옵션이 없으면 줄바꿈 문자는 하나의 문자로 인식하지 못한다. 결국 아래는 None를 출력한다.
p = re.compile('a.b')
m = p.match('a\nb')
print(m)


# 아래와 같이 re.DOTALL를 주면 줄바꿈 문자를 하나의 문자로 인식한다.
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
print(m.group()) # 출력시 a (엔터) b 로 출력, 그냥 b만 출력되는게 아님


p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)


p = re.compile('(?s)a.b')
m = p.match('a\nb')
print(m)


# []안에서는 점(.)자체를 의미. 아래는 점이 없기 때문에 값이 없다.
p = re.compile('[.]')
m = p.match('abb')
print(m)


# 아래보면 sub 함수인데 만약에 영문한글숫자 _ - \n은 제외하고 나머지는 없애고 싶다면
# todo []안에서 - 문자 주의해서 사용해야 함. 가능하면 - 이문자는 맨 나중에 쓰자. - 다음에 \n 문자가 오면 컴파일러가 인식을 못함
# todo 일반적으로 -는 범위를 의미함. 그래서 가장 뒤에 쓰는 것이 맞음
text_org = "I love 123 you \n you are ### monster-real real_real"
print(text_org)


cond = r'[^a-zA-Z0-9가-힣\n_-]'
text = re.sub(cond,'', text_org)
print(text)


cond = r'[^a-zA-Z0-9가-힣-_\n]'
text = re.sub(cond,'', text_org)
print(text)


cond = r'[^a-zA-Z0-9가-힣\n]'
text = re.sub(cond,'', text_org)
print(text)

cond = r'[^a-zA-Z0-9가-힣_-df]'
text = re.sub(cond,'', text_org)
print(text)

# 오류가 발생한다. 
# cond = r'[^a-zA-Z0-9가-힣_-\n]'
# text = re.sub(cond,'', text)
# print(text)


######################################################################### 전방후방탐색
# todo 전체가 왼쪽에서 오른쪽으로 탐색하는 것은 공통이다.
# 전방긍정형탐지 : 패턴과 일치하면 패턴전까지 왼쪽 위치
# 전방부정형 탐지 : 패턴과 일치하지 않으면 패턴전까지 왼쪽 위치 
# 후방긍정형탐지 : 패턴과 일치하면 패턴전까지 오른쪽 위치
# 후방부정형 탐지 : 패턴과 일치하지 않으면 패턴전까지 오른쪽 위치
# 전후방 탐색에서 ()는 그룹이 없는 기본이다. 즉 findall에서 그룹이 없으면 기본을 출력하지만 그룹이 있으면 기본을 출력하지 않고 그룹만 출력한다.
# todo 후방탐색은 무조건 고정길이어야 한다. 아주 중요
# https://m.blog.naver.com/PostView.naver?blogId=hankrah&logNo=222203805292&categoryNo=65&proxyReferer=

################################################## 전방긍정형 탐색
print("\n==========>일반적인 탐색")
p = re.compile('.+:')
m = p.search('http://www.google.com')
print(m.group())


print("\n==========>일반적인 탐색(그룹화)")
p = re.compile('.+(:)')
m = p.search('http://www.google.com')
print(m.group())
print(m.group(0))
print(m.group(1))   # :만 출력


# findall 그룹이 있으면 모든 그룹을 리스트 형식으로 반환한다. search 후에 group() 또는 group(0)하고는 다르다.
print(p.findall('http://www.google.com'))


# 전방긍정형탐색
print('\n===========>http:에서 : 만 제외하고 http만 출력')
# todo 그룹명을 제외하고 출력 ?=
p = re.compile(".+(?=:)")
m = p.search("http://www.google.com")


print(m.group())   # http만 출력
print(m.group(0))  # http만 출력
# print(m.group(1))  # 그룹이 없다. 이렇게 하면 오류가 발생한다.
print(p.findall("http://www.google.com"))


################################################## 여기서 ?=문자(열)
# 문자열 전체와 매칭되어야 함

p = re.compile(".+(?=wwa)") # w가 아니라 wwa전체와 매칭. 그리고 항상 (?=) 이렇게 사용한다. 가로가 있어야 한다.
print(p.findall("http://www.wwa.google.com"))

##################################################

#todo 그룹명을 포함한 전체 출력 ?:
# ?: 일반적으로 캡처하지 않는다 라고 표현한다. ** 원노트 정의 참고
# 그룹화하지 않는다 라는 말과 동일한 것 같은데 어렵게 써놨네...
p = re.compile(".+(?::)")
print(p.findall("http://www.google.com"))


################################################## 25.04.18
hhh='kokokoko'
p=re.compile("(ko)+")
print(p.findall(hhh))

p=re.compile("(?:ko)+")
print(p.findall(hhh))

##################################################


# 전방긍정형탐색 실패 사례, foo다음에 소문자가 와야 하는데 숫자가 옴
print(re.search('foo(?=[a-z])', 'foo123'))


# 여기서 소비한다는 어려운 말이 나온다. 즉 경계를 찾되 소비하지 않고 나둔다.
# 뒤에 패턴에서 시작점을 이 소비하지 않은 경계부터 시작한다.
# 아래는 foo 다음에 b를 소비자하지 않고 점(.)문자시 시작점으로 한다.
m = re.search('foo(?=[a-z])(.)', 'foobar')
# m = re.search('foo(?=[a-z])', 'foobar')
print(m.group())            # foob 여기서 b가 출력되는 것은 group()은 전체를 다 표시하기 때문. 즉 b는 뒤에 그룹때문에 나온다.
print(m.group(0))
print(m.group(1))           # 그룹을 출력한다. 여기서 그룹은 (.)이 된다.
# print(m.group(2))         # ?=을 하는 순간 이것은 이미 그룹이 아니다. 그리고 마지막 문자를 소비하지 않는다.

p = re.compile('foo(?=[a-z])(.)')
print(p.findall('foobar'))


p = re.compile(r'foo(?:[a-z])(.)')
print(p.findall('foobar'))  # a만 출력, ?: 이미 그룹해제의 기능
m = p.search('foobar')

print(m)
print(m.group())            # 마찬가지 fooba를 출력 ?: 은 마지막 문자
print(m.group(0))
print(m.group(1))


# 전방탐색이 아니 일반적인 것을 보면
m = re.search('foo([a-z])(.)', 'foobar')
# m = re.search('foo([a-z])', 'foobar')

print(m.group())                    # 일치문자열 다표시
print(m.group(0))                   # 일치문자열 다표시
print(m.group(1))                   # 첫번째 그룹만 'b' 표시
print(m.group(2))                   # 두번째 그룹만 표시 'a'
# print(m.group('ch'))                # 두번째 그룹만 표시 'a'

# 이럴때는 ()으로 묶인게 전부다 그룹으로 됨
p = re.compile('foo([a-z])(.)')
print(re.findall(p, 'foobar'))      # 그룹만 표시


p = re.compile('foo[a-z]')
print(p.findall("foobar"))

print(re.search('foo([a-z])(.)', 'foobar'))

################################################## 전방부정형 탐색
# ?!<패턴> 패턴과 일치 않아야 된다. 일치하지 않으면 패턴의 왼쪽값을 출력
# 그렇게 많이 쓰지는 않을 것 같다.

# foobar가 긍정형 패턴과 일치 하니 왼쪽값 foo를 출력
print(re.search('foo(?=[a-z])', 'foobar'))
p = re.compile(r'foo(?=[a-z])')
print(p.findall('foobar'))


# 전방부정형. foo다음에 문자가 오지 말아야 하는데 b가 있으니 값이 없다.
print(re.search('foo(?![a-z])','foobar'))


# foo다음에 숫자가 오니까 foo를 출력. 이때 숫자1은 소비하지 않는다.
# 즉 시작점을 위해 남겨둔다. 단지 출력만 하지 않을 뿐이다.
print(re.search('foo(?![a-z])','foo123'))


# 부정형 전방탐색(특정 파일 확장자 제외)
# todo .*$ 이게 붙는 이유는 만약에 bat, exe가 아니면 .이후의 확장자를 보여주라는 의미 원래는 아니면 전방부정형 앞만 보여주기 때문에. $는 없어도 되는 듯
print("\n==========>부정형 탐색")
p = re.compile(r"(.*[.](?!bat$|exe$).*$)")
# p = re.compile(r"(.*[.](?!bat$|exe$))")
m = p.search("aaa.bat")
print(m)

m = p.search("aaa.bbbbat")
print(m)

m = p.search("aaa.batsss")
print(m)

m = p.search("bbb.exe")
print(m)

m = p.search("bbb.exe  exe")
print(m)


m = p.search("ccc.xlsx")
print(m)


################################################## 후방탐색(지원하지 않는 언어도 많다)
data1 = 'ABC01: $23.45'
print(re.search(r'\$[0-9.]+', data1)) # 여기서 23인데 [0-9]으로 가능할려면 [0-9.]+ 즉 숫자 또는 점이 하나이상이기 때문에 가능 함. 헷깔리지 말길


# 만약에 달러가 필요없다면 어떻게 해야 할까
# 아래와 같이 하면 안된다. 가격만 나오는게 아니기 때문이다. ABC01에서 01이 나온다.
print(re.search(r'[0-9.]+', data1))


# 후방탐색을 이용. 마찬가지로 패턴은 소비는 하지 않고 이후부터 출력
print(re.search(r'(?<=\$)[0-9.]+', data1))


p = re.compile(r'(?<=\$)[0-9.]+')
print(p.findall(data1))


# TODO 아래예는 아주 중요하다. 후방탐색도 역시 왼쪽에서 오른쪽으로 탐색을 하되 패턴의 오른쪽을 출력한다.
# 아래에에서 23.24가 20.01보다 먼저 추가되는 것을 확인할 수 있다.
data1 = 'ABC01: $23.45 $20.01'
p = re.compile(r'(?<=\$)[0-9.]+')
print(p.findall(data1))


# 전방탐색과 후방탐색을 같이 사용해 보자
data1="""
<head>
<title>Ben Forta's Homepage</title>
</head>
"""

# 후방긍정형으로 한번 걸러내면 Ben Forta's Homepage</title></head>
# 전방긍정형으로 다시 걸려내면 Ben Forta's Homepage
p = re.compile(r'(?<=<[tT][iI][tT][lL][eE]>).+(?=<\/[tT][iI][tT][lL][eE]>)')
print(p.findall(data1))

# 좀더 간단하게
p = re.compile(r'(?<=<[tT][iI][tT][lL][eE]>).+(?=<\/[TITLE]+>)', re.IGNORECASE)
print(p.findall(data1))


# 아래는 허용되지 않는다. 
# todo : 후방탐색은 무조건 고정길이 여야 한다. .* 또는 .+ 이런것은 허용되지 않느다.
# 예제에서 뒤부분은 긍정형 탐색이다. 한참처다보고 다른다은 것을 암..ㅎㅎㅎ
# p = re.compile(r'(?<=<[TITLE]+>).+(?=<\/[TITLE]+>)', re.IGNORECASE)
# print(p.findall(data1))



# 아래도 찾지 못한다. 먼저 < 다음에 t밖에 없는데 그다음이 > 가 아니기 때문에 이것도 한참 봤네
p = re.compile(r'(?<=<[TITLE]>).+(?=<\/[TITLE]+>)', re.IGNORECASE)
print(p.findall(data1))

###################################################################### 241228_예제 추가

 # 원래는 [I Love you, Love you] 이러게 나와야 하는데
 # todo 전후방탐색을 제외하고는 모두 소비한다. 
sss = "I Love you"
p = re.compile(r'[IL].+')
print(p.findall(sss))

###################################################################### 

# 아래는 참 중요한 샘플이다.
# 먼저 이런 경우는 원하는 자료가 나온다.
data2= """AAA BBB</title>"""
p = re.compile(r'(AAA.*(?=<\/[tT][iI][tT][lL][eE]>))', re.IGNORECASE)
print(p.findall(data2))


# * 일경우 ['AAA BB',''] 이렇게 반드시 널이 하나 따라 나온다. 당연하다.
data2= """AAA BBB</title>"""
p = re.compile(r'(.*(?=<\/[tT][iI][tT][lL][eE]>))', re.IGNORECASE) # 앞에 아무것도 없어도 되는 경우는
print(p.findall(data2))


# TODO ['AAA BB'] 이렇게 만 나오게 할려면 .*가 아닌 .+이렇게 해야 한다
data2= """AAA BBB</title>"""
p = re.compile(r'(.+(?=<\/[tT][iI][tT][lL][eE]>))', re.IGNORECASE) # 앞에 아무것도 없어도 되는 경우는
print(p.findall(data2))



###################################################################### 후방부정탐색
# 아래의 예제에서는 $이 아니고 다음에 바로 숫자가 오는 것을 출력

# 먼저 아래에서 $30에서 30만 찾는 후방긍정탐색을 하면 아래와 같다.
data1 = 'I paid $30 for 100 apples'
p = re.compile(r'(?<=\$)(\d+)')
print(p.findall(data1))

# 이번에는 $30에서 30이 아니라 100만 찾기. 후방부정형탐색, 3은 출력되지 않음. 왜냐하면 소비되지 않았지만 전후방탐색시 출력은 안하기 때문
p = re.compile(r'(?<!\$)(\d+)')  #이렇게 하면 $30에서 0도 출력됨
print(p.findall(data1))


# $30에 0이 나오지 않기 위해
p = re.compile(r'(?<!\$)(\d{2,})')
print(p.findall(data1))


# 또는 아래와 같이
# \b는 단어와 단어의 경계를 의미한다. 어렵게 얘기 할 것 없고 한 구절로 만 패턴을 만족하는 것
# 여기서 100은 단독으로 쓰였지만 $30에 0은 단독으로 쓰이지 않았다. 이렇게 하면 쉬울걸
p = re.compile(r'(\b(?<!\$)\d+\b)')
print(p.findall(data1))

######################################################################### \b \B
# Boundary 경계를 의미. 원노트에 정의된 항목을 참고
# 한글이 이제는 되네....

text = "Explore results with the Tools below"
print(re.findall(r'\b.', text))

print(re.findall(r'\b.\b', text)) # 다 공백만 나온다.

# todo 제일앞에 _, 숫자, 문자이면 경계가 있는 것으로 본다.
# 제일뒤에 경계가 있는 것으로 본다.
# '_'문자를 제외하고는 문자와 특수문자사이에는 무조건 경계가 있는 것으로 본다.
# "_" 문자 취급하고 나머지 특수문자는 비문자 취급. # todo 항상 "_" 문자 주의
tList = ['foo', 'foo.', '(foo)', 'bar foo baz', 'foo_', 'foobar','foo3','_foo','123foo']
for item in tList:
    print(item + " ===> ", end="")
    print(re.findall(r'\b.', item))

# 아래는 'foo_', 'foobar','foo3' 둘은 일치하지 않음
for item in tList:
    result = re.search(r'\bfoo\b', item)
    if result:
        print(item + " ==> " + result.group())


# todo 아래는 모두 선택된다. 여기도 쉽게 얘기하면 어절별 검색.
p = re.compile(r'\b[a-zA-Z]+\b')
m = p.findall('no class as all')
print(m)


# 한글을 테스트 해보자. 한글도 되는듯 한데...
p = re.compile(r'\b[가-힣]+\b')
m = p.findall('언제부터 한글이 되는지 모르겠지만 현재는 된다')
print(m)


# 아하!! 안에 포함된 것만 /B 문자와 문자, 비문자와 비문자이기 때문에
p = re.compile(r'\Bclass\B')
m = p.search('noclassed at all')
print(m)


# 양쪽에 문자난 숫자로 되어 있는 연속된 문자열을 출력
# class -> las, all->l 이렇게 출력된다.
p = re.compile(r'\B[a-zA-Z]+\B')
m = p.findall('no class as all')
print(m)


# 원래 예는 특정 문자열이 어절마다 처음에 있는지 없는지를 판단하기 위한 것
# 아래는 예를 들어도 다 값이 같아서 헷갈릴수 있음
text = "yaya yayaya  ya"
p =re.compile(r'\bya')      # 앞에 'ya'만 선택
print(p.findall(text))


p =re.compile(r'ya\b')      # 뒤에 'ya'만 선택
print(p.findall(text))

######################################################################### |은 or의 의미
# todo 양쪽을 붙여써야 함. 핵심은 양쪽을 꼭 붙여써야 함.
# todo 여기서 중요한 것은 "문자열1"|"문자열2" 이럴 때 각 문자열 전체와 매칭이 되어야 함
# 각 문자열의 각각의 문자가 아님

text = "Monday Tuesday Friday"
print(re.findall('(Mon|Tues|Fri)day', text)) # findall group단위로 출력한다. 그룹이 지정되어 있으면


print('\n==============> |은 or의 의미')
p = re.compile('Crow|Servo')
m = p.match('CrowHello')            # 첫번째 문자열과 매칭
print(m)


p = re.compile('Crow|Hello')
m = p.search(('CrowHello'))         # 전체 문자열 중에 매칭되는 첫번째 문자열 리턴
print(m)


# 테스트
p = re.compile('aa|bb')
m = p.match('aabb ccaa')
print(m)


# 테스트
p = re.compile('aa|bb')
m = p.search('aabb ccaa')
print(m)


p = re.compile('aa|bb')             # 천체 문자열 중에 매칭되는 전체 문자열. 그룹이면 그룹에 해당되는 것만 리턴
m = p.findall('aabb ccaa')
print(m)


######################################################################### split
# todo re.split 첫번째 인자가 패턴이라는 것이다. 아주중요
print('\n===============>화이트스페이스로 분리하기')
text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

text = re.split(r'\s+', text)
print(text)


print('\n===============>숫자로 분리하기')
text = """100 John    PROF
101 James   STUD
102 Mac   STUD 200"""
text = re.split('\d+', text)
print(text)


# 이게 좀 더 확실하다. 하나의 문장이 있을 때 숫자중심으로 분리. 위에는 \n 문자까지 출력됨
# 처음 나오는 숫자로 분리하면 앞에 빈 공백이 하나 생긴다.
text = "100 hgl 200 jung 300 min"
text = re.split(r'\d+', text)
print(text)

# 앞에 100이 없으니 공백이 없다.
text = "hgl 200 jung 300 min"
text = re.split(r'\d+', text)
print(text)


print('\n===============>문자열 특정 키워드로 분리하기')
text = "사과 딸기 수박 메론 바나나"
text = re.split(' ', text)                      # 공백으로 분리 #TODO 파이참에서만 공백인데 _ 으로 표시됨
print(text)


# 여기는 화이트문자를 하나의 스페이스로 변경하는 것
text = "사과 딸기 수박 메론               바나나"
p = re.compile(r'\s+')
ret_list = p.findall(text)
print(ret_list)

for item in ret_list:
    text = text.replace(item,' ')
print(text)

text = "사과 딸기 수박 메론               바나나"
text = re.sub(r'\s+',' ', text)
print(text)

# 공통 모듈을 이용해서 한번 테스트. todo 부분실행으로는 공통모듈을 인식하지 못하네. 일단 주석처리, 그렇치 안으면 import re를 인식하지 못함
# text = "사과 딸기 수박 메론               포토"
# text = srh.SU_RE_WS_SUB01(text, ' ')
# if text:
#     print(text)
#
# text = "사과 딸기 수박 메론               포토"
# text = srh.SU_RE_WS_SPLIT01(text)
# if text:
#     print(text)

# text = """사과1
# 딸기1
# 수박1
# 메론1
# 바나나1"""
# text = srh.SU_RE_WS_SPLIT01(text)
# if text:
#     print(text)


# 특수문자로 분리
text = "사과+딸기+수박+메론+++++포도"
str = r'\++'  # 이것의 의미는 +가 2개 있는 것이 아니라 앞에 +가 1개이상이라는 의미
text = re.sub(str,'-',text)
print(text)


# sub 메소드의 참조를 이용하여 이름과 전화번호의 순서를 바꿈
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
print(p.sub(r'\g<phone> \g<name>', "park3 010-1234-5678"))


# # 특수문자를 전역함수로 테스트, todo 부분실행으로는 공통모듈을 인식하지 못하네.
# text = "사과+딸기+수박+메론+++++포토"
# text = srh.SU_RE_SP_SUB02(r'\++','+',text)
# print(text)
#
# print("=============>전역함수를 이용한 특수문자 분리")
# text = "사과+딸기+수박+메론+++++포토"
# text = srh.SU_RE_WS_SPLIT02(r'\++',text)
# print(text)

# text = "100 hgl 200 jung 300 min"
# text = srh.SU_RE_WS_SPLIT02(r'\d+',text)
# print(text)

# 이런경우 처음과 끝에 공백을 제외하고 중간 리스트 항목에 공백이 없게 할려면(처음과 끝은 안되는 듯)
# text = "100 hgl 200 jung 300 min 500"
# text = srh.SU_RE_WS_SPLIT02(r'\d+\s+|\s+\d+\s+|\s+\d+', text)
# print(text)

######################################################################### %s
# %s는 화이트 스페이스를 의미 하는데 이미 앞에서 읽어 버리면(소진해버리면) 뒤에는 적용이 안된다
# 아래는 as가 선택이 되지 않은 것은 이미 class에서 공백을 소진해 버렸기 때문이다.
p = re.compile(r'\s+[a-zA-Z]+\s+')
m = p.findall("no class as all")
print(m)

m = p.findall("no class as all ") # 이렇게 되면 all도 출력 todo 즉 소진됬다는 건 조건에 맞을 때만 해당됨. 무조건 읽는다고 소진된건 아님
print(m)

# 아래와 같이 하면 둘다 가능함. 일단 공백을 하나 더 넣고 + 를 없애는 것이다.
p = re.compile(r'\s[a-zA-Z]+\s')
m = p.findall("no class  as all") # as 앞에 공백이 2개 임
print(m)

# 아래에서 all이 출력되는 이유는 앞에 공백이 있지만 at에서 이미 읽었기 때문에 all은 앞에 공백이 적용되지 않는다.
# 헛갈리수 있으니 하나의 단어씩 적용해 보면 답이 나온다. noclasstwo가 나오는 이유는 t->w일때 다음 o가 공백이 아니기 때문
# 이후에 o-> 공백이기때문에 o까지만 읽는다.
# todo 중요한 것은 아래와 같이 3파트로 구성되어 있으면 3파트로 검사를 한다. 예를들면
# noclass라면 맨처음 n공백이아니라면 o가 문자인지 그리고 그 다음 c가 공백이 아니인지 이런식으로 계속 조건을 만족할 때까지 소진한다.
# 이래서 at 나오지 않는 이유다. 3파트로 구성이 되어 있었으며 나왔을 것이다.

p = re.compile(r'\S[a-zA-Z]+\S')
m = p.findall('noclasstwo at all')
print(m)

m = p.findall(("noclasstwo abt all"))
print(m)

# 테스트
text = srh.SU_RE_TURNCHANGE_SUB03("her 010-1111-2222")
print(text)


# '\s'는 공백문자, '\S'는 공백문자가 아닌 것
# 아래에서 class만 출력됨. 뒤에 as는 출력되지 않음. 왜냐하면 앞뒤 공백을 이미 class에서 사용했기 때문 !!!아주 중요
p = re.compile('\s[a-zA-Z]+\s')
m = p.findall('no class as all')
print(m)

# 아래는 class, as 가 출력 됨. as 공백을 하나 더 넣었기 때문 !!!아주중요
p = re.compile('\s[a-zA-Z]+\s')
m = p.findall('no class  as all')
print(m)

######################################################################### %w
# \w 문자와 숫자를 의미 함
# todo "_"를 포함한다. 아주 중요!!
text = "A1 B2 c3 d_4 e:5 ffGG77--__-- "
print(re.findall(r'\w', text))

# \w는 "_"를 포함한다.
text = "a_b-c"
print(re.findall(r'\w', text))

# \W는 정반대의 의미, 즉 문자, 숫자, _ 이 아닌 것
text = "AS _34:AS11.23  @#$ %12^* ++++"
print(re.findall(r'\W', text))


######################################################################### ?
# *?, +?, ??, {m,n}. 탐욕스럽다는 표현으로 하는데
# 책 "점프투파이썬 326p에 잘 나와 있음

# 아래에서 <...> 이것을 삭제하고 싶을 때
text = "<hp:tttta>수행기관 로고</hp:ttttta> <hp:ttttaaa>"

# +?에서 ?은 .+가 한문자 이상이기 때문에 > 문자가 제일 마지막 >로 잡히지 말고 첫번째 나온것으로 하라는 의미
p = re.compile(r'<hp:.+?>|</hp:.+?>')
print(p.findall(text)) # 출력해보면 "수행기관 로고"를 제외한 나머지가 출력된다.
print(p.sub('',text))