# for문과 if문을 이용하여 원하는 자료만 뽑아내기

word_to_index = {'barber': 1, 'secret': 2, 'huge': 3, 'kept': 4, 'person': 5, 'word': 6, ' keeping': 7}
vocab_size = 5

words_frequency = [word for word,index in word_to_index.items() if index >= vocab_size]
print(words_frequency)