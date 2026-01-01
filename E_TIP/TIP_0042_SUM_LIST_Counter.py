
# 만약에 리스트안에 리스트가 있을 때 안에 리스트를 없애고 그냥 하나의 리스트로 만들고 싶을 때
# 리스트안의 항목들 개수를 알고 싶을 때
# 그리고 빈도수가 많은 상위 5개를 출력하고 싶을 때

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