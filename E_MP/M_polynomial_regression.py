# 다항회귀분석(2차함수)
# 단항회귀분석(1차함수)로 두 변수간의 상관관계를 정확이 예측하지 못할 경우
# train data로 학습시키고 -> test data를 가지고 score() 로 결정계수를 구한다음 -> 예측값을 구한다.
# 그리고 기존에 가지고 있던 train data와 예측값을 그래프로 비교한다.
# 즉 테스트 데이터는 단지 score() 통하여 결졍계수를 구하는데 사용된다.
# 마지막은 기존 y값과 함수를 통해 뽑아낸 y_hat값을 비교

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

import PY_PKG.SU_ALLMO_Init_MO as SI
SI.SU_MO_VarInit(SI.G_SU_INIT_LIST,'PANDAS',1)

##################### 1단계 데이터 준비
df = pd.read_csv(SI.G_SU_ExFilePosIn + 'auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print('='*100)
print("\n\n준비된 데이터 보기")
print(df.head(5))


##################### 2단계 데이터 탐색
#문자열인 horsepower를 숫자형으로 바꾼다.
print('='*100)
print("\n\n데이터 정제, 널값, 타입바꾸기")
df['horsepower'].replace('?', np.nan, inplace=True)         # 숫자로 변경하긴 힘든 문자열 널처리

print("\n\n널처리되기전에 널값 정도")
ndf = df.copy()
print(ndf.info())


df.dropna(subset=['horsepower'], axis=0, inplace=True)      # 널값 삭제
df['horsepower'] = df['horsepower'].astype('float')         # 타입 바꾸기
print("\n\n널처리후의 정보")
print(df.info())

# ###################### 3단계 속성선택
# 분석에 필요한 속성정의
print('='*100)
print("\n\n분석에 필요한 데이터 정의")
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf)


# train_data, test_data를 7:3로 정의
print('='*100)
print("\n\n데이터를 분리")
x=ndf[['weight']]	# 독립변수 x
y=ndf['mpg']		# 종속변수 y
print(type(x))
print(type(y))

# ###################### 4단계 훈련/검증 데이터 분할
print('='*100)
print('종속변수와 독립변수를 정의 데이터 보기')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

print('훈련 데이터 : ', x_train.shape)
print('검증 데이터 : ', x_test.shape)


##################### 5단계 모형 학습 및 검증
# 다항식 변환. 여기서는 다차항을 위한 자료를 만둘어 낸다.
print('='*100)
print("\n\n모형 학습 및 검증")

# 아래 PolynomialFeatures, fit_transform 이함수는 일정한 규칙에 의해서 하나의 변수를 여러개로 만들어냄
# 판다스 함수 예제를 참조하거나 원노트 참조
poly = PolynomialFeatures(degree=2)	# 2차항 적용
x_train_poly = poly.fit_transform((x_train))
print('원 데이터 : ', x_train.shape)
print('2차항 변환 데이터 : ', x_train_poly.shape) # 데이터구조가 3개열로 늘어난다

print(x_train)
print(x_train_poly)

# 여기서 학습하여 모형을 만들어 내다.
pr = LinearRegression()
pr.fit(x_train_poly, y_train)

# 학습이 끝나면 test_data를 가지고 평가하는데 마찬가지로 test_data도 2차항으로 변경
print('='*100)
print("\n\n 모형가지고 검증을 수행")
x_test_poly = poly.fit_transform(x_test)        # 검증데이터도 2차항으로 변경해야 함
r_squre = pr.score(x_test_poly, y_test)		    # pr객체에 이미 학습결과가 숨겨져 있다.
print(r_squre)

print('=' * 100)
print('\n\n 독립변수의 계수와 상수항 출력')
print('x 변수의 개수 a : ', pr.coef_)
print('상수항 b : ', pr.intercept_)


# 이제는 원래의 가지고 있던 train data와 test data로 예측한 회귀선을 그래프로 출력
print('='*100)
print("\n\n 훈련 데이터와 학습된 모형 회귀선 비교")
y_hat_test = pr.predict(x_test_poly)

fig = plt.figure(figsize=(10,3))
ax = fig.add_subplot(1,1,1)
ax.plot(x_train, y_train,'o', label='Train Data')
ax.plot(x_test, y_hat_test, 'r+', label='Predict Value')
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
#  아래는 리눅스에 먹지 않으니 저장하여 비교
plt.show()
plt.close()
# plt.savefig(G_FilePos + " result.png")


# 마지막으로 y데이터와 뽑아낸 함수의 결과인 y를 선형값으로 비교
print('='*100)
print("\n\n 실제값을 예측모형의 결과 y값과 실제 y값을 비교")
x_poly = poly.fit_transform(x)
y_hat = pr.predict(x_poly)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)    # 테스트 데이터인 y_hat_test도 비슷
ax1.legend(loc='best')
plt.show()
plt.close()
# plt.savefig(G_FilePos + " result.png")
