from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

# 표제어를 추출
print("\n ===============>표제어 추출")
n=WordNetLemmatizer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
listValue = [n.lemmatize(item) for item in words]
print(listValue)

print("\n ===============>어간 추출(Porter 알고리즘)")
s = PorterStemmer()
text="This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
words=word_tokenize(text)
print(words)

listValue = [s.stem(item) for item in words]
print('\n')
print(listValue)

print("\n ===============>어간 추출(랭커스터 스태머 알고리즘)")
l=LancasterStemmer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
listValue = [l.stem(w) for w in words]
print(listValue)

