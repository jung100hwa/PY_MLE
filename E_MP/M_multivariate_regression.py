# 다중회귀분석
# 종속변수에 영향을 미치는 독립변수가 여러개 있을 때
# 즉 y = b + a1x1 + a2x2 + a3x3....

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import PY_PKG.SU_ALLMO_Init_MO as SI
SI.SU_MO_VarInit(SI.G_SU_INIT_LIST,'PANDAS',1)


##################### 1단계 데이터 준비
df = pd.read_csv(SI.G_SU_ExFilePosIn + 'auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print('=' * 100)
print('\n\n데이터 탐색')
print(df.head())


#문자열인 horsepower를 숫자형으로 바꾼다.
print('=' * 100)
print('\n\n데이터 정제, 널값처리, 타입변경')

print('\n\n정제전의 데이터 탐색')
print(df['horsepower'].unique())

df['horsepower'].replace('?', np.nan, inplace=True)         # 숫자로 변경하긴 힘든 문자열 널처리
print('\n\n정제후의 데이터 탐색')
print(df['horsepower'].unique())

df.dropna(subset=['horsepower'], axis=0, inplace=True)      # 널값 삭제
df['horsepower'] = df['horsepower'].astype('float')         # 타입 바꾸기
print(df.info())

# 분석에 필요한 속성정의
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())

# train_data, test_data를 7:3로 정의
x=ndf[['weight', 'horsepower', 'weight']]		    # 독립변수 x
y=ndf['mpg']	                                	# 종속변수 y

print('=' * 100)
print('\n\n데이터 분리')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print('훈련 데이터 : ', x_train.shape)
print('검증 데이터 : ', x_test.shape)

# 단순회귀분석 모형 객체 생성
print('=' * 100)
print('\n\n 학습시작 및 모형생성, 결정계수값 출력')
lr = LinearRegression()

# 학습시작
lr.fit(x_train, y_train)
r_squre = lr.score(x_test, y_test)
print(r_squre)

# 변수가 3개 니까 변수앞에 계수도 3개를 출력해준다.
print('=' * 100)
print('\n\n 독립변수의 계수와 상수항 출력')
print('x 변수의 개수 a : ', lr.coef_)   # x 변수를 3개니까 개수도 3개가 리스트 형태로 출력
print('상수항 b : ', lr.intercept_)

# 원데이터와 예측값을 그래프로 비교
# 실제 가장 좋은 방법은 x데이터를 넣고 결과y와 실제y값 비교. 아래는 테스트 데이터로만 함. 크게 상관없다.
y_hat = lr.predict(x_test)
plt.figure(figsize=(10,5))
ax1 = sns.distplot(y_test, hist=False, label='y_test')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)
plt.legend(loc='best')
#  리눅스에 먹지 않는 관계로 저장하여 비교
#  plt.show()
#  plt.close()

plt.savefig(SI.G_SU_ExFilePosImg + "result.png")
