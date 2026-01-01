import numpy as np
import pandas as pd
from tabulate import tabulate


# 파일을 읽어서 숫자 형태로 전환
fList = pd.read_csv('./E_FILE/quest.csv')
# fList = EBP.switch(fList)
print(fList)

# 넘파이로 계산을 편하게 하기 위해 배열로 만듬
quest = np.array(fList)
print(quest)
print(type(quest))

# 5점 척도로 5점 이상인 것은 5점으로 세팅
quest = quest.astype('int32')
quest[quest >= 5] = 5

print(quest)


# # 파일로 저장
# EBP.writercsv(G_AptSample + 'quest2.csv', quest)
print("배열의 특정값만 출력")
print(quest)
print(quest[0, 0], quest[1, 1], quest[4, 3])
print(quest[2:, 3:])

# 배열의 크기 알아보기
print("배열의 크기 : ", end='')
print(quest.shape)

print("배열의 타입 : ", end='')
print(quest.dtype)

quest = quest.astype('int32')
print("바뀐 배열의 타입 : ", end='')
print(quest.dtype)

# 처음 2개행을 0으로 초기화된 배열 생성
plist = np.zeros((2, 10))
print(plist)

# 나머지 3개행을 1으로 초기화
plist = np.ones((3, 10))
print(plist)

# 연속된 정수를 생성하는데 1차원 배열만 가능한듯, 가로도 하나이다는 것
print("\n===============>배열생성")
plist = np.arange(3, 10)
print(plist)

# 모든 원소가 5인 2*3행렬
plist = np.full((2,3),5)
print(plist)

# 단위행렬
plist = np.eye(5)
print(plist)

# 피봇
plist = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(plist)
plist = np.transpose(plist)
print(plist)

# 인덱싱과 슬라이싱)
print("===========인덱싱과 슬라이싱==========")
plist = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # 리스트안에 리스트
print(plist)
print(plist[:3]) # 이것은 똑 같이 나온다. 왜냐하면 리스트안의 리스트가 하나의 원소이기 때문. 0에서부터 2까지 출력. 실제적으로 0행하고 1행밖에 없다.

plist = np.arange(10)  # 리스트안에 하나의 숫자가 리스트라고 생각하면됨
print(plist)
print(plist[:3])
print(plist[-3:])

plist = np.array([[1, 2, 3, 4, 5], [11, 22, 33, 44, 55], [111, 222, 333, 444, 555]])  # 리스트안에 리스트
print(plist)
print(plist[1, 2])
print(plist[:, 2])  # 모든 행의 세번째 요소를 출력
print(plist[1:, 2])
print(plist[:1, 2])

# 조건에 맞는 값을 한번에 바꿀수 있다
# 리스트에서는 아래와 같이 계산이 불가능. 이게 리스트와 배열의 차이
plist[plist > 5] = 0
print(plist)


# 일반적으로 넘파이를 데이터프레임으로 변환하는 방법
plist = np.random.randint(10, 15, (5,3))
df = pd.DataFrame(plist)
print(df)