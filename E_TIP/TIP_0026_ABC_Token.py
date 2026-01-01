from nltk.tokenize import RegexpTokenizer
import nltk

# 아래와 같은 여러 문자가 섞여 있는 문장이 있을 때 영어단어만 뽑아낼려고 한다면
# 중요한 것은 aaa_bbb, ccc#ddd를 aaa bbb ccc ddd로 추출해야 한다.
strL = "abc aaa_bbb ccc#ddd 허길양 123 @@zzz"

# 1단계) 특수문자를 포함한 영문만 추출. 여기서 한글만 제외
# 여기서 중요한게 영문은 대문자 65~90 소문자 97~122. 중간에 91~96까지는 특수문자 라고 해서 특수문자를 제외하면
# 한줄에 다 붙어나온다. 즉 아래와 같이 하면 안된다.
# strL = "".join(i for i in strL if  64 < ord(i) < 91 or 96 < ord(i) < 123)

# strL = "".join(i for i in strL if  ord(i)<128)
# print(strL)

################################################## 2단계만 해도도는데 불용어 제거가 있어서 그런가
# 2단계) 영문단위로 토큰화한다
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
strL = tokenizer.tokenize(strL)
print(strL)

# 3단계-옵션) 단어를 종합한다.
strL = " ".join(strL)
print(strL)