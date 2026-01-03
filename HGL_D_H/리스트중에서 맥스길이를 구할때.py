"""
리스트값중에서 특별한 값을 구할 때

1. 아래 예제는 max
2. 각 리스트마다 길이
2. 이러한 형태를 방법에 응용할 수 있다.
"""

alist = ["abc", "dfadfasdf", "kkkkkk", "dadfas"]

# max len 구하기
max_len = max(len(str) for str in alist)
print(max_len)

# 각 길이를 구해서 리스트로 담기
bList = [len(str) for str in alist]
print(bList)