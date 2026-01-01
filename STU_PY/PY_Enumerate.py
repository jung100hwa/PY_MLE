# 단지 앞에 번호만 붙여준다.
word = [('barber', 8), ('secret', 6), ('huge', 5), ('kept', 4), ('person', 3)]

for item, word in enumerate(word):
    print(item, word)

vocab=[('barber', 8), ('secret', 6), ('huge', 5), ('kept', 4), ('person', 3)]
print(vocab)

# enumerate 자동으로 인덱스르 만든다.
for index, word in enumerate(vocab):
    print(index, word[0])


# 이런문장의 형태가 자주 등장하네...가독성이 떨어지는데
word_to_index = {word[0] : index + 1 for index, word in enumerate(vocab)}
print(word_to_index)

for index, item in enumerate(['body', 'foo', 'bar']):
    print(index, item)


############################################# 251218. 이런 건 정말 대단하다.
# 리스트의 끝을 알아내는 방법인데 정말..
alist = ['a','b','c','d']
for i, v in enumerate(alist):
    if i == len(alist) -1:
        print("rast value")
    else:
        print(v)