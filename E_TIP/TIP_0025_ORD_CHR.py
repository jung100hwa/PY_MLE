"""
ord chr 함수를 이용해서 한글과 영문만 선택하는 예제
"""
import re

strL = ['a','b','A','B','C','가','나','허','ㄱ','ㅣ','ㄴ', '@', '_']
for itme in strL:
    print(itme)

# 첫번째 방법은 함수를 이용
# 영문은 대문자 65~90 소문자 97~122. 중간에 91~96까지는 특수문자
result = [x for x in strL if 64 < ord(x) < 91 or 96 < ord(x) < 123]
print(result)

# 두번재 방법 sub 이용
print("#" * 50)
result = " ".join(strL)
result = re.sub('[^A-Za-z0-9]', ' ', result)
result = result.split()
print(result)


# 한글
# 한글 44032-55203
print(ord('가'))
print(ord('힣'))
print(ord('ㄱ'))
print(ord('ㅎ'))
print(ord('ㅏ'))
print(ord('ㅣ'))

# 아래는 완전한 한글 문장
result = [x for x in strL if 44031 < ord(x) < 55202]
print(result)

# 아래는 받침까지
result = [x for x in strL if 44031 < ord(x) < 55202 or 12592 < ord(x) < 12644 ]
print(result)

print("#" * 50)


# 이번에는 re.sub활용(정규식)
result = " ".join(strL)
result = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣]', ' ', result)
result = result.split()
print(result)


# sub, replace
strL = "파이썬은 버전에 따라 참 다르다!!! abc def"
result = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣]','',strL)
print(result)