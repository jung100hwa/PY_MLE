# 머신러닌 분류기법 중 KNN 알고리즘 사용

import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


import PY_PKG.SU_ALLMO_Init_MO as SI
SI.SU_MO_VarInit(SI.G_SU_INIT_LIST,'PANDAS',1)

############################################## 1단계 데이터 준비
print('=' * 100)
print('\n\n데이터 조회')
df = sns.load_dataset('titanic')
print(df.head())


# ############################################## 2단계 데이터 탐색
print('=' * 100)
print('\n\n데이터 탐색')
print(df.info())

# NaN이 많고 중복 컬럼 제거
print('=' * 100)
print('\n\n널값이 너무 많고 중복 컬럼 제거')
rdf = df.drop(['deck', 'embark_town'], axis=1)
colList = rdf.columns.tolist()
print(type(colList))
print(colList)
print(rdf.columns.values)

# age열에 NaN가 있는 모든 행삭제
print('=' * 100)
print('\n\nage 컬럼의 유일값 조회')
print(rdf['age'].unique())


print('=' * 100)
print('\n\nage컬럼 널인값  행제거')
rdf.dropna(subset=['age'], how='any', axis=0, inplace=True)
print(len(rdf))     # 제거하고 남은 행의 수

# embarked열의 NaN의 값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
print('=' * 100)
print('\n\n승선도시 널값을 가장 많이 방문하는 것으로 치환')
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)

#  print(rdf['embarked'].value_counts(dropna=True))

 # 이걸로도 확인 가능
print(rdf.describe(include='all'))

# 가장 많은 "S" NaN를 교체한다.
print('\n\n 교체전 다음 정보 보기')
print(rdf['embarked'].unique())

rdf['embarked'].fillna(most_freq, inplace=True)
print('\n\n 교체후 다음 정보 보기')
print(rdf['embarked'].unique())



###############################################  3단계 변수로 사용할 후보 선택
print('=' * 100)
print('\n\n변수로 사용할 컬럼만 선택')
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())


# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
print('=' * 100)
print('\n\n원핫 인코딩')

print('\n\n성별의 유일값 조사')
print(rdf['sex'].unique())

 
onehot_sex = pd.get_dummies(ndf['sex'])
print(type(onehot_sex))
ndf = pd.concat([ndf, onehot_sex], axis=1)    # 데이터프레임에 생성된 컬럼을 붙인다.

# onehot 코딩을 하면 sex의 유일한 값이 컬럼으로 만들어진다.
print(ndf.columns.values)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

print('=' * 100)
print('\n\n원핫 인코딩 이후 원컬럼 sex, embarked 삭제 후 데이터프레임')
ndf.drop(['sex', 'embarked'], axis=1, inplace=True) # 원핫코딩으로 유일값만큼 컬럼이 생성되었으므로 삭제
print(ndf)


###############################################  4단계 훈련/검증 데이터 분할
# 예측변수 - survivied, 나머지는 설명변수
x = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]
y = ndf['survived']

# 설명변수들 정규화, 정규화는 모든 컬럼의 데이터값을 0 - 1 사이즈로 정의. 그래서 모든 값을 숫자형태로 함
print('=' * 100)
print('\n\n 정규화 수행 : 정규화는 0-1로 모슨 값을 맞춤')
x = preprocessing.StandardScaler().fit(x).transform(x)
print(type(x))
print(x)

# train data와 test data 7:3으로 분리
print('=' * 100)
print('\n\n훈련데이터와 검증데이터로 분리')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)
print('train data : ', x_train.shape)
print('test data : ', x_test.shape)


################################################  5단계 모형 학습 및 검증
# 모형객체 생성 이웃의 수는 5개
knn = KNeighborsClassifier(n_neighbors=5)

# train 데이터를 가지고 학습
knn.fit(x_train, y_train)

# test data를 가지고 y_hat를 예측
y_hat = knn.predict(x_test)

# # 모형에 의해 새로운 결과값과 기존 결과값을 비교한다.
print('=' * 100)
print('\n\n검증데이터의 예측값과 실제데이터 검증')
print(y_hat[0:10])              # 넘파이 배열
print(y_test.values[0:10])      # 시리즈

# 모형의 성능 평가
print('=' * 100)
print('\n\nconclusion matrix로 모형의 성능평가')
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)   # tp, fp, fn, tn 값을 출력, confusion matrix 참고

# 모형의 성능의 지표 계산
knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)       # f1-score가 예측능력 평가치