from konlpy.tag import Okt
okt = Okt()

# 원하는 단어만 1, 나머지는 0처리
def onthotencording(word, word2index):
	one_hot = [0] * len(word2index)
	index = word2index[word]
	one_hot[index] = 1
	return one_hot


token=okt.morphs("나는 자연어 처리를 배운다")  
print(token)

# 정수 인코딩
word2index = {}
i = 1
for item in token:
	if item not in word2index.keys(): # 중복방지
		word2index[item] = i
		i = i + 1

print(word2index)

word2index = onthotencording('자연어',word2index)
print(word2index)