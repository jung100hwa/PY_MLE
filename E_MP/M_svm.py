# 머신러닌 분류기법 중 SVM 기법을 활용
#  두 개체군을 분리하는 최적의 경계선을 찾는 기법

import pandas as pd
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn as sns

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn import preprocessing
from sklearn import metrics
from sklearn import svm

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

print('\n\nnan 삭제후 정보 보기')
rdf['embarked'].fillna(most_freq, inplace=True)
print(rdf.info())


#  *************************************************   test

print("---테스트--")
d_ir = {'a':[1,2,3,np.nan], 'b':[11,22,3,4],'c':[111,111,33,np.nan]}
ndf = pd.DataFrame(d_ir);
print(ndf)

print(ndf['a'].unique())
print(ndf['a'].value_counts())

# 유일값의 상대적 비율
print(ndf['c'].value_counts(normalize=True))

# 유일값 정렬, 값에 대한 개수를 정렬 시킨다.
print(ndf['c'].value_counts(sort=True, ascending=True))

# na값을 포함시키지 않는다.
print(ndf['c'].value_counts(sort=True, ascending=False, dropna=True))
# NaN값도 유일값에 포함시킨다.
print(ndf['c'].value_counts(dropna=False))

s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6,7])
print(s1)
print(s2)

# 상하로 결합
print('상하결합')
ndf = pd.concat([s1,s2], axis=0)
print(ndf)

# 인덱스 중복 없이
print('기존인덱스를 무시하고 새로 부여')
ndf = pd.concat([s1,s2], axis=0, ignore_index=True)
print(ndf)

# 열추가
print('열추가')
ndf = pd.concat([s1,s2], axis=1)
print(ndf)

# 열추가 좌우에 인덱스값이 동일한 것만
print('인덱스값이 동일한 열만 추가')
ndf = pd.concat([s1,s2], axis=1, join='inner')
print(ndf)

print('\n================')
df1 = pd.DataFrame(np.arange(1,5).reshape(2,2), columns=['a','b'])
df2 = pd.DataFrame(np.arange(6,10).reshape(2,2), columns=['a','b'])
print(df1)
print(df2)

print('\n================')
ndf = pd.concat([df1,df2], axis=0, ignore_index=True)
print(ndf)

print('\n================')
ndf = pd.concat([df1,df2], axis=1)
print(ndf)

#  *************************************************   test

# 분석에 활용할 열(속성) 선택
print('=' * 100)
print('\n\n  분석을 위한 컬럼 선택')
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head(5))

# 원핫인코딩 - 범주형을 컬럼으로 만들어 숫자형으로 변환
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)
onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

# 원핫인코딩 대상 컬럼 삭제
ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head(5))

# 독립변수와, 구하고자하는 종속변수 정의
# survived 값은 이미 생존자, 사상자의 값이 들어 있음. 이것과 비교
x = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]
y = ndf['survived']

# 독립변수(설명변수)를 정규화
x = preprocessing.StandardScaler().fit(x).transform(x)

# train data와 test data를 7:3으로 구분
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=10)
print('train data : ', x_train.shape)
print('test data : ', x_test.shape)

# 2단계 모형 학습 및 검증
# 모형객체 생성, 여기서는 여러 커널 중 rbf를 사용한다. 다른 커널의 용도와 정확도는 별도 공부
svm_model = svm.SVC(kernel='rbf')

# 학습
svm_model.fit(x_train, y_train)

# test data를 가지고 예측값 추출
y_hat = svm_model.predict(x_test)

# 비교
print('=' * 100)
print('\n\n만들어진 모형의 값과 실제값을 비교하여 모형의 성능 검증')
print(y_hat[0:10])
print(y_test.values[0:10])

# 지표계산(실측치와 예측치)
svm_metrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_metrix)


svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
