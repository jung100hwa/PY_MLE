# 1차 함수로 기울기와 y절편을 구하는 것
# y = ax + b, a,b를 구하여 실제데이터(y)와 구한공식에 x를 넣어 구한 y를 비교
# 단순회귀분석으로 이게 잘 맞지 않을 경우 2차, 즉 다향회귀분석을 이용해야 함

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import PY_PKG.SU_ALLMO_Init_MO as SI

# 인자값 1은 데이터베이스 연결하지 않도록 하기 위해서 윈도우에는 깔려 있지 않음
# 머신러닝에는 사실상 데이터베이스가 필요하지 않음
SI.SU_MO_VarInit(SI.G_SU_INIT_LIST,'PANDAS',1)


##################### 1단계 데이터 준비
df = pd.read_csv(SI.G_SU_ProFilLoc + 'auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print('=' * 100)
print("1단계 데이터 준비")
print(df.head(5))


##################### 2단계 데이터 전처리
print('=' * 100)
print("데이터 타입을 살펴보기")
print(df.info())

print("행과열은 아래와 같이 간단하게 알아볼 수 있음")
print(df.shape)

#  통계정보는 숫자만 해당 됨
print('=' * 100)
print('데이터 통계정보 살펴보기')
print(df.describe())


# 문자열인 horsepower를 유일값을 본다.
print('=' * 100)
print('문자열 컬럼의 유일값 정보보기')
print(df['horsepower'].unique())


#  숫자로 변경하기 힘든 문자열 변경, 널값 삭제, 타입바꾸기
print('=' * 100)
print('문자열 변경, 널값 삭제, 타입변경후 통계정보 보기')
df['horsepower'].replace('?', np.nan, inplace=True)

ndf = df.copy()
# dropna만 특이하게 subset이라는 키워드로 컬럼을 한정 짓는다.
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
print(df.describe())

print('=' * 100)
print(df.info())

print('=' * 100)
print('바꾸기 전에 널값 개수 확인')
# print(ndf.horsepower.isnull().sum())
# 이렇게 하는 것이 나을 듯 함. 한가지 방식으로만 해야지 헷갈림
print(ndf['horsepower'].isnull().sum())

print('=' * 100)
print('info로 타입과 널값이 아닌 개수 보기')
print(df.info())


# ###################### 3단계 속성선택
# 종속변수 : mpg        나머지는 독립변수로 사용
print('=' * 100)
print('종속변수와 독립변수 데이터프레임 보기')
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())

# scatter와 mpg 변수간의 상관관계 스캐터 그래프로 알아보기
print('=' * 100)
print('두 변수간의 상관관계를 산점도 그래프로 보기')
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10,5))
#  아래의 코드는 리눅스에서 안된다.
plt.show()
plt.close()

#  아래와 같이 이미지로 저장해서 확인하자
# plt.savefig(SU_Init.G_SU_ExFilePosOut + " sss.png")

# seaborn 라이브러리로 그래프 그려보기
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)   # 회귀선 미표시
#  마찬가지로 아래의 코드는 윈도우에서만
plt.show()
plt.close()

# plt.savefig(SU_Init.G_SU_ExFilePosOut + " sss.png")

# seaborn jointplot() 함수를 이용해서 그려보기
sns.jointplot(x='weight', y='mpg', data=ndf)
sns.jointplot(x='weight', y='mpg', data=ndf, kind='reg')
plt.show()
plt.close()

# seaborn pairplot() 함수를 이용한 데이터프레임의 모든 열간의 관계 그래프 그리기
# 자기 자신은 히스토그램으로 그리고 나머지는 산점도로 그린다.
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()



# ###################### 4단계 훈련/검증 데이터 분할
# train data와 test data로 구분(7:3)
print('=' * 100)
print('종속변수와 독립변수를 정의 데이터 보기')

# 독립변수 x, !!!!반드시 2차원 배열로 넣어야 함
# 아래와 같이 배열로 넣으면 데이터프레임 됨
x = ndf[['weight']]
print(type(x))

# 종속변수 y
# 이렇게 [] 하나만 있으면 시리즈가 됨
y = ndf['mpg']
print(type(y))

print(x)
print(y)

print('=' * 100)
print('훈련데이터와 검증데이트를 7:3으로 분리하여 개수 확인하기')
x_train, x_test, y_train, y_test = train_test_split(x,
        y,
        random_state=10,
        test_size=0.3)

print('train data 개수 : ', len(x_train))
print('test  date 개수 : ', len(x_test))

# 이것들은 항상 쌍으로 존재한다. 즉 weight에 해당하는 mpg가 선택된다.
xtestList   = x_test.values.tolist()
xtestIndex  = x_test.index.tolist()
ytestList   = y_test.values.tolist()

print('=' * 100)
print(x_test)

# 이렇게 원본과 비교했을 때 훈련데이터 x, y 검증데이터의 x,y는 항상 쌍을 유지한다. 무조건 개수만큼 x,y를 선정하는게 아니다.!!!!!
# 엑셀의 하나의 로우 단위로 x_train, y_train를 선택한다고 보면된다. x_test, y_test마찬가지. 당연한 얘기를 혹시 몰라 검증 했음
for item in range(0,len(xtestList)):
    print(str(xtestList[item][0]) + " : " + str(ytestList[item]) + " : " + str(df.loc[xtestIndex[item],'weight']) +
          " : " + str(df.loc[xtestIndex[item],'mpg']))


###################### 5단계 모형 학습 및 검증
# skelearn 라이브러리에서 선형회귀분석 모듈 가져오기
lr = LinearRegression()

# train data를 가지고 모형 학습
lr.fit(x_train, y_train)

# 학습을 마친 train_data를 적용하여 결정계수(R-제곱) 계산
# 값이 클수록 정확도가 높다.
print('=' * 100)
print('훈련시킨 모형이 얼마나 정확한지 검증데이터로 테스트')
r_square = lr.score(x_test, y_test)
print(r_square)

# 선형회귀의 기울기, y절편
print('=' * 100)
print('모형에서 기울기와 y절편을 한다.')
print('기울기 a : ', lr.coef_)
print('y절편 : ', lr.intercept_)

# y = ax + b에서 a와 b가 구해졌으니 실제 데이터를 넣어서 테스트
# x데이터를 넣어서 구한 1차방정식에 넣어서 y_hat를 구하고 실제 즉 원래 mpg의 y값과 그래프로 비교한다
# 실제 두그래프를 비교하면 약간의 차이가 발생한다. 이럴때는 직선보다는 곡선의 형태가 더 잘 들어 맞는다.
y_hat = lr.predict(x)
plt.figure(figsize=(10,5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
ax1.legend(loc='best')

plt.show()
plt.close()

#  리눅스에서 그래프로 표시가 안되니 저장 후 확인
# plt.savefig(G_FilePos + " result.png")
