'''
군집 클러스터링 기법 중 k_means 기법
몇개의 클러스터로 나누고 각 클러스트 중심까지 거리가 가장 가까운 클러스터로 포함시킨다.
클러스터 개수가 많으면 분석효과가 떨어진다.
비지도 학습으로 예측결과를 지정할 필요가 없다.
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
[Step 1] 데이터 준비
'''

# Wholesale customers 데이터셋 가져오기 (출처: UCI ML Repository)
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
00292/Wholesale%20customers%20data.csv'

df = pd.read_csv(uci_path, header=0)  # header 컬럼명으로 사용할 row number


'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())   
print('\n')

# 데이터 자료형 확인
print(df.info())  
print('\n')

# 데이터 통계 요약정보 확인
print(df.describe())
print('\n')


'''
[Step 3] 데이터 전처리
'''

# 분석에 사용할 속성을 선택, 지지도 학습으로 예측변수는 필요 없다.
print('\n 분석에 사용할 데이터 선택')
X = df.iloc[:, :]
print(type(X))          # 데이터프레임
print(X[:5])
print('\n')

# # 테스트
# aDic = {'a':[1,2,3], 'b':[11,22,33], 'c':[111,222,333], 'd':[1111,2222,3333]}
# df = pd.DataFrame(aDic)
# ndf = df.iloc[1:3,1:3 ]
# print(ndf)

# # 이렇게 조건을 주어 검색한다. 짱
# mask1 = (df['a'] == 1) | (df['d'] == 3333)
# ndf = df[~mask1]
# print(ndf)

# 설명 변수 데이터를 정규화
# 정규화 한다는 것은 모든 값을 0~1 사이값으로 평준화 한다는 것
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)
print(type(X))          # 넘파이 배열
print(X[:5])
print('\n')



'''
[Step 4] k-means 군집 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 cluster 군집 모형 가져오기
from sklearn import cluster

# 모형 객체 생성, 이런 모듈을 만드는 사람이 진짜 실력자네.
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

# 모형 학습
kmeans.fit(X)   

# 예측 (군집), labels_ 변수에 클러스터 방번호가 출력된다.
# 실행할 때마다 값이 달라질 수 있다.
cluster_label = kmeans.labels_   
print(cluster_label)
print('\n')

# 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())
print('\n')


# 그래프로 표현 - 시각화
# 8개의 변수를 모두 그릴 수 없으니 2개의 변수를 선택해서 그래프로 그린다.
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', 
        colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', 
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

# 큰 값으로 구성된 클러스터(0, 4)를 제외 - 값이 몰려 있는 구간을 자세하게 분석
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]

ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', 
        colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', 
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

