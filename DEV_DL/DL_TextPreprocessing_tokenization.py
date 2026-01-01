# 1_01. 토큰화
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import kss
from konlpy.tag import Okt
from konlpy.tag import Kkma 

print("\n========>단어토큰화")
# nltk 함수를 사용
print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# keras 토큰 함수를 사용(이게 가장 낫지 않을까 생각)
print(text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


# 문장토큰화를 한문장으로 작성해야 될 것 같음 아니면 \n이 출력됨
print("\n========>문장토큰화")
text="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."
print(sent_tokenize(text))

# 점이 여러개 있어도 정확히 문장으로 구분해 냄
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))

# 한국어 문장 토큰화
print("\n========>한국어 문장토큰화")
text='딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?'
print(kss.split_sentences(text))

# 품사태킹
print("\n========>품사태깅")
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))

x=word_tokenize(text)
print(pos_tag(x))

# 한국어 품사태킹(정확히는 품사태킹), 상대적으로 느림
print("\n========>한국어 품사태깅")
okt = Okt()
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print("\n========>한국어 품사태킹(명사만 추출)")
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

# 다른 모듈을 이용한 형태소  분리
print("\n========>한국어 품사태킹 다른 모듈을 이용한")
kkma=Kkma()  
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 
print(kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))  