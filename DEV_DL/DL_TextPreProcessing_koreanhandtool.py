
# 이 모듈은 한국사람이 만든 것 같은데 엄청 시간 많이 걸림
# 그리고 내부적으로 텐서플러를 이용하는 것 같음
from pykospacing import spacing

from konlpy.tag import Okt

import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor

# 한국어를 위한 SOYNLP의 L tokenizer
from soynlp.tokenizer import LTokenizer
from soynlp.tokenizer import MaxScoreTokenizer

from soynlp.normalizer import *

from ckonlpy.tag import Twitter

# 한국어를 띄어쓰기 테스트
sent = '''김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 
철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를
 찾으러 속세로 내려온 인물이다.'''


# 테스트 하기 위해 띄어쓰기가 없는 문장으로 만들기
new_sent = sent.replace(" ", '')
print(new_sent)

# 띄어쓰기가 거의 일치 한다
kospacing_sent = spacing(new_sent)
print(kospacing_sent)

# 애는 신조어는 인식하지 못함
tokenizer = Okt()
print(tokenizer.morphs('에이비식스 이대휘 1월 최애돌 기부 요정'))

# soynlp 얘는 계속 등장하는 단어를 단어로 인식
# 아래는 한번만 다운로드 받고 무조건 주석 처리. 시간이 엄청 걸림
# urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")


corpus = DoublespaceLineCorpus("2016-10-20.txt")
print(len(corpus))

i = 0
for document in corpus:
  if len(document) > 0:
    print(document)
    i = i+1
  if i == 3:
    break

# 여기서 학습을 하면서 텍스트 파일에 단어들이 몇번 나오는지 테이블을 만드는 과정
word_extractor = WordExtractor()
word_extractor.train(corpus)
word_score_table = word_extractor.extract()


# 위에서 학습된 것을 기반으로 아래 단어를 토큰화 한다.
scores = {word:score.cohesion_forward for word, score in word_score_table.items()}
l_tokenizer = LTokenizer(scores=scores)
lst = l_tokenizer.tokenize("국제사회와 우리의 노력들로 범죄를 척결하자", flatten=False)
print(lst)

# 띄어쓰기가 안된 것들 토큰화
maxscore_tokenizer = MaxScoreTokenizer(scores=scores)
lst = maxscore_tokenizer.tokenize("국제사회와우리의노력들로범죄를척결하자")
print(lst)


# SOYNLP를 이용한 반복되는 문자 정제
# num_repeats 이것은 같은 것을 몇개까지 허용할 것인가
print(emoticon_normalize('앜ㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠ', num_repeats=3))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠ', num_repeats=2))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠ', num_repeats=2))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠㅠㅠ', num_repeats=2))
print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2))
print(repeat_normalize('와하하하하하하핫', num_repeats=2))
print(repeat_normalize('와하하하하핫', num_repeats=2))


# 형태소 분석기를 통하여 한글 토큰화. 형태소 분석기 일경우 신조어 등을 인식하지 못한다.
# 또한 사람이름 등 이것을 단어로 인식못하는데 아래는 단어 사전을 등록해서 "이것을 단어로 인식하고 분리하지 말라" 라고 등록하는 과정

# 아래는 은경이를 단어로 인식하지 못한다.
twitter = Twitter()
lst = twitter.morphs('은경이는 사무실로 갔습니다.')
print(lst)

# 은경이를 하나의 단어로 인식하도록 단어 사전에 등록해 주었다
twitter.add_dictionary('은경이', 'Noun')
lst = twitter.morphs('은경이는 사무실로 갔습니다.')
print(lst)