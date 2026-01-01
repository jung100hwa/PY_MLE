# 어느 문장에서 단어의 카운트 수를 구하는 것

from collections import Counter
import re
data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

p = re.findall(r'\w+',data)
print(p)
count = Counter(p)
print(count)  # 딕셔너리 형태로 정렬되어 출력

# 빈도수가 가장 높은 한개의 단어
print(count.most_common(1))

# 빈도수가 가장 높은 2개의 단어
print(count.most_common(2))

# =====================================================
alist = ['A','B','B','C','D','D','D']
count = Counter(alist)
print(count)

# update 해서 다시 출력. alist + alist2 해서 빈도수를 구한다.
# 기존에 A와 추가된 A까지 해서 A가 빈도수가 가장 많게 나온다.
alist2=['A','A','A']
count.update(alist2)
print(count)

# subtrack는 update 반대개념 
count.subtract(alist2)
print(count)


########################################################25.09.27
# 직접 함수를 만들어 사용----------1
def count_letters(word):
    counter = {}
    for letter in word:
        if letter not in counter.keys():
            counter[letter] = 0
        counter[letter] += 1
    return counter
print(count_letters('banana'))


def count_letters2(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter,0)
        counter[letter] += 1
    return counter
print(count_letters2('banana'))


def count_letters3(word):
    counter = {}
    for letter in word:
        counter[letter] = counter.get(letter,0) +1
    return counter
print(count_letters3('banana'))


# collection defaultdict 활용----------2
from collections import defaultdict
def count_letters4(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter
print(count_letters4('banana'))

# collection Counter 활용----------3
p = re.findall(r'\w','banana')
print(p)
count = Counter(p)
print(count)


########################################################25.09.27
# 단어길이에 따라 분류
def group_words(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper

group_words(["banana", "banana", "strawberry", "mango", "pineapple", "watermelon", "blueberry", "kiwi", "grapefruit"])

# 만약에 중복을 제거하고 싶으면
def group_words2(words):
    grouper = defaultdict(set)  # 이 부분만 바뀌면 되지요
    for word in words:
        length = len(word)
        grouper[length].add(word) # add 바꾸고
    return grouper

group_words2(["banana", "banana", "strawberry", "mango", "pineapple", "watermelon", "blueberry", "kiwi", "grapefruit"])
