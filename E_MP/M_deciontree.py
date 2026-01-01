# 머신러닌 분류기법 중 decision tree

import pandas as pd
import numpy as np
import seaborn as sns

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn import svm
from sklearn import tree

# ###################################################################### 1단계 데이터 준비
# 웹에서 다운로드
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

# 열이름을 지정
df.columns = ['id','clump','cell_size','cell_shape', 'adhesion','epithlial',
              'bare_nuclei','chromatin','normal_nucleoli', 'mitoses', 'class']
print('=' * 100)
print('\n\n 샘플데이터 출력')
print(df.head())

# ###################################################################### 2단계 데이터 탐색
# 데이터의 자료형 확인
print('\n\n 데이터 타입 출력')
print(df.info())

# 통계정보 출력
print('\n\n 데이터 통계정보')
print(df.describe())

# 문자열을 가지 컬럼을 숫자형으로 변환
print('\n\n 숫자형이 아닌 컬럼의 유일값 출력')
print(df['bare_nuclei'].unique())

print('\n\n 널값으로 바꾸고 널인행 삭제 후 데이터 타입 변경')
df['bare_nuclei'].replace('?',np.nan, inplace=True)
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)
df['bare_nuclei'] = df['bare_nuclei'].astype('int') 
print(df.info())

# ####################################################################### 3단계 데이터셋 구분
x=df[['clump','cell_size','cell_shape', 'adhesion','epithlial',
      'bare_nuclei','chromatin','normal_nucleoli', 'mitoses']]  #설명 변수 X
y=df['class']                                                   #예측 변수 Y


# 설명 변수 데이터를 정규화
print('=' * 100)
print('\n\n 데이터 표준화 후 데이터 값 출력(정규화와 표준화 개념은 정리 노트 참고)')
x = preprocessing.StandardScaler().fit(x).transform(x)
x1 = pd.DataFrame(x)
print(x1)

# train data 와 test data로 구분(7:3 비율)
print('=' * 100)
print('\n\n 훈련용 데이터와 검증용 데이터 분리')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print('train data 개수: ', x_train.shape)
print('test data 개수: ', x_test.shape)


# ################################################################### [Step 4] Decision Tree 분류 모형 - sklearn 사용
# 모형 객체 생성 (criterion='entropy' 적용)
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5) # 5단계까지만

# train data를 가지고 모형 학습
tree_model.fit(x_train, y_train)   

# test data를 가지고 y_hat을 예측 (분류) 
y_hat = tree_model.predict(x_test)      # 2: benign(양성), 4: malignant(악성)

print('=' * 100)
print('\n\n 검증용 데이터 예측값과 실제값을 비교')
print(y_hat[0:10])
print(y_test.values[0:10])

# 모형 성능 평가 - Confusion Matrix 계산
print('=' * 100)
print('\n\n 모형성능평가')
tree_matrix = metrics.confusion_matrix(y_test, y_hat)  
print(tree_matrix)
print('\n')

# 모형 성능 평가 - 평가지표 계산
tree_report = metrics.classification_report(y_test, y_hat)            
print(tree_report)

print(y_hat)
