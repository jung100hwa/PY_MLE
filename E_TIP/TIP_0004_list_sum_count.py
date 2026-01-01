"""
리스트의 내용을 하나로 썸하는 예제
"""

from collections import Counter

alist = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person '], ['knew', 'secret'],
 ['secret', 'kept', 'huge', 'secret'], ['huge', ' secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'],
 ['barber','kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', ' barber', 'crazy'],
 ['barber', 'went', 'huge', 'mountain']]

alist = sum(alist,[])
print(alist)

vocab = Counter(alist)
print(vocab)

print("상위 5개 출력")
alist = vocab.most_common(5)
print(alist)


print("순서에 상관없이 단어 비교")
str1 = "bake"
str2 = "kabe"

print(Counter(str1) == Counter(str2))

str1 = "홍길동"
str2 = "길동홍"
print(Counter(str1) == Counter(str2))
