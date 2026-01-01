import matplotlib.pyplot as plt
import seaborn as sns

###################################################회귀선이 있는 산점도
# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
# print(titanic[['age','fare']])
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('darkgrid')

# # 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 5))   
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
 
# # 그래프 그리기 - 선형회귀선 표시(fit_reg=True)
# sns.regplot(x='age',        #x축 변수
#             y='fare',       #y축 변수
#             data=titanic,   #데이터
#             ax=ax1)         #axe 객체 - 1번째 그래프 

# # 그래프 그리기 - 선형회귀선 미표시(fit_reg=False)
# sns.regplot(x='age',        #x축 변수
#             y='fare',       #y축 변수
#             data=titanic,   #데이터
#             ax=ax2,         #axe 객체 - 2번째 그래프        
#             fit_reg=False)  #회귀선 미표시

# plt.show()


################################################### 히스토그램과 커널밀도 함수
# # 하나의 변수를 y축을 0-1까지 비율로 표시해서 대충 어떤 변수가 많은지만 알아본다.
# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('darkgrid')

# # 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 5))   
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)
 
# # 기본값
# sns.distplot(titanic['fare'], ax=ax1) 

# # hist=False
# sns.distplot(titanic['fare'], hist=False, ax=ax2) 

# # kde=False
# sns.distplot(titanic['fare'], kde=False, ax=ax3)        

# # 차트 제목 표시
# ax1.set_title('titanic fare - hist/ked')
# ax2.set_title('titanic fare - ked')
# ax3.set_title('titanic fare - hist')

# plt.show()


################################################### 히트맵
# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('darkgrid')

# # 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
# table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

# print(table)

# # 히트맵 그리기
# sns.heatmap(table,                  # 데이터프레임
#             annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
#             cmap='YlGnBu',          # 컬러 맵
#             linewidth=.5,           # 구분 선
#             cbar=True)             # 컬러 바 표시 여부

# plt.show()


################################################### 범주형 데이터 산점도

# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 5))   
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
 
# # 이산형 변수의 분포 - 데이터 분산 미고려
# sns.stripplot(x="class",      #x축 변수
#               y="age",        #y축 변수           
#               data=titanic,   #데이터셋 - 데이터프레임
#               ax=ax1)         #axe 객체 - 1번째 그래프 

# # 이산형 변수의 분포 - 데이터 분산 고려 (중복 X)
# # 중복되지 않도록 폭을 좀 더 넒혀서 표현
# sns.swarmplot(x="class",      #x축 변수
#               y="age",        #y축 변수
#               data=titanic,   #데이터셋 - 데이터프레임
#               ax=ax2)         #axe 객체 - 2번째 그래프        

# # 차트 제목 표시
# ax1.set_title('Strip Plot')
# ax2.set_title('Swarmp Plot')

# plt.show()


################################################### 막대 그래프
# # 이게 가장 많이 사용하지 않을까

# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 5))   
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)
 
# # x축, y축에 변수 할당
# sns.barplot(x='sex', y='survived', data=titanic, ax=ax1) 

# # x축, y축에 변수 할당하고 hue 옵션 추가, hue 옵션은 sex를 다시 클래스로 세분화. 멀티바의 개념
# sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2) 

# # x축, y축에 변수 할당하고 hue 옵션을 추가하여 누적 출력
# sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)       

# # 차트 제목 표시
# ax1.set_title('titanic survived - sex')
# ax2.set_title('titanic survived - sex/class')
# ax3.set_title('titanic survived - sex/class(stacked)')

# plt.show()


# ################################################### 빈도 그래프
# # 막대 그래프는 변수가 x, y이 이지만 빈도 그래프는 x가 얼마나 많은지 count를 그래프화 한것
# # 굳이 이것을 사용하지 않아도 x, y는 count해서 막대로 표시할 것 같은데.

# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')

# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 5))   
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)
 
# # 기본값
# sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1) 

# # hue 옵션에 'who' 추가 
# # who는 데이터 프레임의 컬럼. 막대그래프랑 별 차이가 없어 보임
# sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2) 

# # dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
# sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)       

# # 차트 제목 표시
# ax1.set_title('titanic class')
# ax2.set_title('titanic class - who')
# ax3.set_title('titanic class - who(stacked)')

# plt.show()


################################################### 박스 플롯/ 바이올린 그래프
# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 그래프 객체 생성 (figure에 4개의 서브 플롯을 생성)
# fig = plt.figure(figsize=(15, 10))   
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
 
# # 박스 그래프 - 기본값
# # hue옵션은 그래프의 멀티로. 즉 하나의 값을 더 세분화 함
# sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) 

# # 바이올린 그래프 - hue 변수 추가
# sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) 

# # 박스 그래프 - 기본값
# sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) 

# # 바이올린 그래프 - hue 변수 추가
# sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) 

# plt.show()


################################################### 조인트 그래프
# # Seaborn 제공 데이터셋 가져오기
# # 조인트 그래프는 한 화면에 분활해서 그릴 수가 없음
# # 산점도에다 x축 히스토그램, y축 히스토그램을 동시에 보여줌
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 조인트 그래프 - 산점도(기본값)
# j1 = sns.jointplot(x='fare', y='age', data=titanic) 

# # 조인트 그래프 - 회귀선
# j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic) 

# # 조인트 그래프 - 육각 그래프
# j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic) 

# # 조인트 그래프 - 커럴 밀집 그래프
# j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic) 

# # 차트 제목 표시
# j1.fig.suptitle('titanic fare - scatter', size=15)
# j2.fig.suptitle('titanic fare - reg', size=15)
# j3.fig.suptitle('titanic fare - hex', size=15)
# j4.fig.suptitle('titanic fare - kde', size=15)

# plt.show()


################################################### 조건을 적용하여 화면을 그리드로 분할하기
# # 거의 쓸일이 없을 것 같다. 아래 예제는 2행 3열의 그리드로 나누어서. 남자,여자,아이들 x 구조, 미구조
# # Seaborn 제공 데이터셋 가져오기
# titanic = sns.load_dataset('titanic')
 
# # 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
# sns.set_style('whitegrid')

# # 조건에 따라 그리드 나누기
# g = sns.FacetGrid(data=titanic, col='who', row='survived') 

# # 그래프 적용하기
# g = g.map(plt.hist, 'age')
# plt.show()


################################################### 이변수 데이터의 분포
# 컬럼개수 만큼 나올수 있는 모든 조합에 대하여 상호간의 그림을 그린다.
# 같은 변수끼리는 히스토그램, 다른 변수와의 그래프는 산점도
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# titanic 데이터셋 중에서 분석 데이터 선택하기
titanic_pair = titanic[['age','pclass', 'fare']]

# 조건에 따라 그리드 나누기
g = sns.pairplot(titanic_pair)
plt.show()