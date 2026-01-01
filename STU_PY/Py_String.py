import re

# 문자열 안에 작은 따음표가 있으면 ""로 묶기
str = "python's is very perl"
print(str)

# 문자열 안에 큰 따음표가 있으면 ''로 묶기
str = 'python is "very" perl'
print(str)

# '\으로 뒤에 나오는 문자를 그냥 문자로 인식
str = 'python is \"very\" perl\' language'
print(str)

# 문자열 곱셈
str1 = 'hgl'
str2 = str1 * 5
print(str2)

print('=' * 50)

print('문자열 대체')
str = "I Love My Life"
p = re.compile('My|Life')
str1 = p.sub('YourMind',str)
print(str1)

print('\n문자열 분리')
str1 = re.split('\s',str)
print(str1)

print('=' * 50)

# 98%를 표현할려면 %d 뒤에 %% 2개적어야 함 !!규칙
str = 'Error is %d%%' % 98
print(str)

print('=' * 50)
str = 'My Life is love'
print(str.count('i'))
print(len(str))
print(str.find('L'))

# 아래와 같은 코드는 가독성이 떨어져 굉장히 좋지 않다
print(str[:str.find('L')])

# join이라는 함수
str = '.'
str1 = 'abcd'
str1 = str.join(str1)
print(str1)

# 문자열 분리
str = 'abcde'
alist = list(str)
print(alist)

# 대소문자
print(str1.upper())
print(str1.lower())

# 공백지우기
str = ' hgl '
print(str.lstrip())
print(str.rstrip())
print(str.strip())

# 문자열 바꾸기, re.sub이 나을 것 같다. 여러개를 지정할 수 있으니까
str = 'abb'
print(str.replace('b','a'))

# 문자열 나누기, re.split 이것은 한번 규칙을 정해놓으면 계속해서 쓸 수 있다
str = 'a.b.c.d'
print(str.split('.'))

# %말고 좀더 고급스럽게 치환
str = "I Love {0} and I Love {1}"
str1 = str.format('MyLife','Mydaughter')
print(str1)








