from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np

text = """A barber is a person. a barber is good person. a barber is huge person. 
he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. 
His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."""

# 문장토큰화
text = sent_tokenize(text)

# 단어토큰화를 수행하면서 불용어 제거
# 정제와 단어 토큰화

vocab = {}
sentences = []
stop_words = set(stopwords.words('english'))

for item in text:
    sentence = word_tokenize(item)
    result = []

    for item2 in sentence:
        item2 = item2.lower()

        if item2 not in stop_words:
            if len(item2) > 2:  # 단어길이가 2이하인 것은 버린다.
                result.append(item2)

                if item2 not in vocab:
                    vocab[item2] = 0
                vocab[item2] += 1
    sentences.append(result)

print(sentences)
print(vocab)

vocab_sorted = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
print(vocab_sorted)

# 많이 언급된 것 부터 1,2,3..부여한다.
word_to_index = {}
i = 1
for item in vocab_sorted:
    if item[1] > 1:  # 언급된 횟수가 1이상인 것으로 한다.
        word_to_index[item[0]] = i
        i = i + 1

print(word_to_index)

# 일반적으로 특정 순위 안에 것만 사용 함
wort_to_del = [w for w, c in word_to_index.items() if c > 5]
for w in wort_to_del:
    del word_to_index[w]

print(word_to_index)

# 토큰화된 단어들에 정수로 인코딩
# 숫자가 매기지지 않은 것은 여기서는 6으로 통일
word_to_index['OOV'] = len(word_to_index) + 1

encoded = []
for s in sentences:
    temp = []
    for w in s:
        try:
            temp.append(word_to_index[w])
        except KeyError:
            temp.append(word_to_index['OOV'])
    encoded.append(temp)
print(encoded)

# 패팅 : 가장 긴 자리수로 맞춘다.
max_len = max(len(w) for w in encoded)
for item in encoded:
    while len(item) < max_len:
        item.append(0)

padded_np = np.array(encoded)
print(padded_np)
