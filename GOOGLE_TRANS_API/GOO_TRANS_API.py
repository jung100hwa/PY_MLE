import googletrans
from googletrans import Translator

# 주의!!
# 최신 버전으로 설치시 이상한 group 에러가 발생하면 아래와 같이 함
# pip uninstall googletrans
# pip install googletrans==3.1.0a0

# 이렇게 해도 잘 안되네.!!! 다른 대안

tr = Translator()
strV = tr.translate("안녕하세요", src='ko', dest='en')
print(strV)

# src 옵션을 하지 않아도 자동으로 인식 함
strV = tr.translate("안녕하세요", dest='en')
print(strV)

# 영어번역문만 출력
print(strV.text)

# 일본어 출력
strV = tr.translate("안녕하세요", dest='ja')
print(strV.text)
print(strV.pronunciation)

# 지원가능한 나라 출력
print(googletrans.LANGCODES)

# 언어 자동 감지
strV = tr.detect("이 언어는 한국어입니까?")
print(strV)
print(strV.lang)