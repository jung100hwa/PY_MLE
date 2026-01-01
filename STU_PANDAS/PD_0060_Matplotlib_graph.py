from numpy.lib.function_base import rot90
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import font_manager, markers, rc

# 그래프 출력은 파이썬의 옵션으로 필요할 때마다 찾아봐야 함
# 한글지원을 위해
font_path = "C:/Windows/Fonts/malgun.ttf"
# font_path = "C:/Windows/Fonts/NanumGothic.ttf"

font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 테스트 할 때에는 각각 주석을 풀고 실행
############################################################################## 기본선그래프
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# df = df.loc['경기도']

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 그래프 사이즈 및 라벨각도 지정 설정. 이들문장은 plot 함수 앞에 있어야 함
# plt.figure(figsize=(14,7))
# # plt.xticks(rotation='vertical')
# plt.xticks(size=10, rotation = 90)

# plt.plot(df.index, df.values, marker='o', markersize=10)
# # 데이터프레임 자체를 할당해도 됨
# # plt.plot(df)

# # 그래프에 라벨 달기
# plt.title('서울 -> 경기 인구 이동', size=30)
# plt.xlabel('기간', size=20)
# plt.ylabel('이동 인구수', size=20)
# plt.legend(labels=['서울->경기'], loc='best', fontsize=15)

# plt.show()

############################################################################## 하나의 화면에 2개의 그래프
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# df = df.loc['경기도']

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 그래프 사이즈 및 라벨각도 지정 설정. 이들문장은 plot 함수 앞에 있어야 함
# fig = plt.figure(figsize=(10,10))
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)

# ax1.plot(df, 'o', markersize=10)
# ax2.plot(df,marker='o',markersize=10, markerfacecolor='green', color='olive', linewidth=2, label='서울->경기')
# ax2.legend(loc='best')

# # y축범위
# ax1.set_ylim(50000,800000)
# ax2.set_ylim(50000,800000)

# ax1.set_xticklabels(df.index, rotation = 75)
# ax2.set_xticklabels(df.index, rotation = 75)

# plt.show()


############################################################################## 화면을 분할하는 방식으로 해서 하나의 선그래프 그리기
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# df = df.loc['경기도']

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 그래프 사이즈 및 라벨각도 지정 설정. 이들문장은 plot 함수 앞에 있어야 함
# fig = plt.figure(figsize=(15,5))
# ax1 = fig.add_subplot(1,1,1)

# ax1.plot(df,marker='o',markersize=10, markerfacecolor='green', color='olive', linewidth=2, label='서울->경기')
# ax1.legend(loc='best')

# # y축범위
# ax1.set_ylim(50000,800000)

# # 제목
# ax1.set_title('서울->경기 인구 이동', size = 30)

# # 축 이름 추가
# ax1.set_xlabel('기간', size= 12)
# ax1.set_ylabel('이동 인구수', size=12)

# # x축 라벨설정
# ax1.set_xticklabels(df.index, rotation = 75)

# # x, y축 라벨크기, x,y축 제목이 아닌 라벨
# ax1.tick_params(axis='x',labelsize=10)
# ax1.tick_params(axis='y',labelsize=10)

# plt.show()


############################################################################## 한 화면에 여러개의 그래프를 출력
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(1970, 2018)))
# df = df.loc[['경기도','충청남도','경상북도','강원도'], colyears]

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 그래프 사이즈 및 라벨각도 지정 설정. 이들문장은 plot 함수 앞에 있어야 함
# fig = plt.figure(figsize=(15,5))
# ax1 = fig.add_subplot(1,1,1)

# ax1.plot(colyears, df.loc['경기도'],marker='o',markersize=10, markerfacecolor='green', color='green', linewidth=2, label='서울->경기')
# ax1.plot(colyears, df.loc['충청남도'],marker='o',markersize=10, markerfacecolor='olive', color='olive', linewidth=2, label='서울->충남')
# ax1.plot(colyears, df.loc['경상북도'],marker='o',markersize=10, markerfacecolor='skyblue', color='skyblue', linewidth=2, label='서울->경북')
# ax1.plot(colyears, df.loc['강원도'],marker='o',markersize=10, markerfacecolor='magenta', color='magenta', linewidth=2, label='서울->강원')

# ax1.legend(loc='best')

# # y축범위
# # ax1.set_ylim(50000,800000)

# # 제목
# ax1.set_title('서울->경기 충남 경북 강원 인구 이동', size = 30)

# # 축 이름 추가
# ax1.set_xlabel('기간', size= 12)
# ax1.set_ylabel('이동 인구수', size=12)

# # x축 라벨설정
# ax1.set_xticklabels(colyears, rotation = 75)

# # x, y축 라벨크기, x,y축 제목이 아닌 라벨
# ax1.tick_params(axis='x',labelsize=10)
# ax1.tick_params(axis='y',labelsize=10)

# plt.show()


############################################################################## 화면을 4개로 분리해서 각 화면에 띄우기
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(1970, 2018)))
# df = df.loc[['경기도','충청남도','경상북도','강원도'], colyears]

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 그래프 사이즈 및 라벨각도 지정 설정. 이들문장은 plot 함수 앞에 있어야 함
# fig = plt.figure(figsize=(12,5))
# ax1 = fig.add_subplot(4,1,1)
# ax2 = fig.add_subplot(4,1,2)
# ax3 = fig.add_subplot(4,1,3)
# ax4 = fig.add_subplot(4,1,4)

# ax1.plot(colyears, df.loc['경기도'],marker='o',markersize=5, markerfacecolor='green', color='green', linewidth=1, label='서울->경기')
# ax2.plot(colyears, df.loc['충청남도'],marker='o',markersize=5, markerfacecolor='olive', color='olive', linewidth=1, label='서울->충남')
# ax3.plot(colyears, df.loc['경상북도'],marker='o',markersize=5, markerfacecolor='skyblue', color='skyblue', linewidth=1, label='서울->경북')
# ax4.plot(colyears, df.loc['강원도'],marker='o',markersize=5, markerfacecolor='magenta', color='magenta', linewidth=1, label='서울->강원')

# ax1.legend(loc='best')
# ax2.legend(loc='best')
# ax3.legend(loc='best')
# ax4.legend(loc='best')

# # y축범위
# # ax1.set_ylim(50000,800000)

# # 제목
# ax1.set_title('서울->경기 인구 이동', size = 15)
# ax2.set_title('서울->충남 인구 이동', size = 15)
# ax3.set_title('서울->경북 인구 이동', size = 15)
# ax4.set_title('서울->강원 인구 이동', size = 15)

# # 축 이름 추가
# ax1.set_xlabel('기간', size= 10)
# ax1.set_ylabel('이동 인구수', size=10)
# ax2.set_xlabel('기간', size= 12)
# ax2.set_ylabel('이동 인구수', size=10)
# ax3.set_xlabel('기간', size= 10)
# ax3.set_ylabel('이동 인구수', size=10)
# ax4.set_xlabel('기간', size= 10)
# ax4.set_ylabel('이동 인구수', size=10)

# # x축 라벨설정
# ax1.set_xticklabels(colyears, rotation = 75)
# ax2.set_xticklabels(colyears, rotation = 75)
# ax3.set_xticklabels(colyears, rotation = 75)
# ax4.set_xticklabels(colyears, rotation = 75)

# # x, y축 라벨크기, x,y축 제목이 아닌 라벨
# ax1.tick_params(axis='x',labelsize=10)
# ax1.tick_params(axis='y',labelsize=10)
# ax2.tick_params(axis='x',labelsize=10)
# ax2.tick_params(axis='y',labelsize=10)
# ax3.tick_params(axis='x',labelsize=10)
# ax3.tick_params(axis='y',labelsize=10)
# ax4.tick_params(axis='x',labelsize=10)
# ax4.tick_params(axis='y',labelsize=10)

# plt.show()

# ############################################################################## 면적 그래프
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(1970, 2018)))
# df = df.loc[['경기도','충청남도','경상북도','강원도'], colyears]
# df = df.transpose()
# print(df)

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# df.index = df.index.map(int)

# # stacked=True로 하면 경기도 데이터에다 순차적으로 더하는 구나.
# df.plot(kind='area', stacked=False, alpha=0.2, figsize=(14,7))
# plt.title('서울 -> 타시도 이동', size=30)
# plt.ylabel('이동 인구수', size=20)
# plt.xlabel('기간', size=20)
# plt.legend(loc='best', fontsize=15)

# plt.show()

############################################################################## 면적그래프에 좀더 꾸미기
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(1970, 2018)))
# df = df.loc[['경기도','충청남도','경상북도','강원도'], colyears]
# df = df.transpose()
# print(df)

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# df.index = df.index.map(int)

# # stacked=True로 하면 경기도 데이터에다 순차적으로 더하는 구나.
# ax = df.plot(kind='area', stacked=False, alpha=0.2, figsize=(14,7))
# ax.set_title('서울->타시도 인구 이동', size=30, color='brown', weight='bold')
# ax.set_ylabel('이동 인구수', size=20, color='blue')
# ax.set_xlabel('기간', size=20, color='blue')
# ax.legend(loc='best', fontsize=15)

# plt.show()


############################################################################## 막대그래프
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(2010, 2018)))
# df = df.loc[['충청남도','경상북도','강원도', '전라남도'], colyears]
# df = df.transpose()
# print(df)

# # 그래프 스타일 지정
# plt.style.use('ggplot')
# df.index = df.index.map(int)

# # 막대 그래프 보기
# df.plot(kind='bar', figsize=(15,10), width=0.7, color=['orange','green','skyblue','blue'])
# # 아래와 같이 하면 충청남도, 경상북도를 하나의 그래프에 위아래로 표시한다. 위아래 표시하는 것은 stacked=True
# # df[['충청남도','경상북도']].plot(kind='bar', figsize=(15,10), width=0.7, stacked=True)

# plt.title('서울->타시도 인구 이동', size=30)
# plt.ylabel('이동 인구수', size=20)
# plt.ylabel('기간', size=20)
# plt.ylim(5000, 30000)
# plt.legend(loc='best', fontsize=15)

# plt.show()


############################################################################## 가로형 막대
# df = pd.read_excel('./Pandas/시도별 전출입 인구수.xlsx')
# print(df)

# # 누락값 처리
# df.fillna(method='ffill', inplace=True)

# # 조건에 맞는 것만 불러오기
# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# df = df[mask]
# df = df.drop(['전출지별'], axis=1)
# df.rename({'전입지별':'전입지'}, axis=1, inplace=True)
# df.set_index('전입지', inplace=True)
# print(df)

# # 전입지가 경기도만 추출하여 선그래프
# colyears = list(map(str, range(2010, 2018)))
# df = df.loc[['충청남도','경상북도','강원도', '전라남도'], colyears]
# df['합계'] = df.sum(axis=1)

# # 합계를 정렬해서 합계만 받아오기
# df = df[['합계']].sort_values(by='합계', ascending=True)
# print(df)

# # 그래프 스타일 지정
# plt.style.use('ggplot')

# # 막대 그래프 보기
# df.plot(kind='barh', figsize=(14,7), width=0.7, color=['orange','green','skyblue','blue'])

# plt.title('서울->타시도 인구 이동', size=30)
# plt.ylabel('이동 인구수', size=20)
# plt.ylabel('기간', size=20)
# plt.legend(loc='best', fontsize=15)

# plt.show()


############################################################################## y축을 2개로. 즉 보조축을 가진 그래프
# 핵심은 ax1, ax2 2개의 객체를 각각 plot 하면된다.
# 행과열의 fig.add_subplot(4,1,1) 이런 부분을 지정하지 않으면 된다.
# 이것을 지정하면 하나의 화면에 4개의 행과 1의 열. 즉 테이블에 각각 그래프가 들어간다.

# plt.style.use('ggplot')   # 스타일 서식 지정
# plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정

# # Excel 데이터를 데이터프레임 변환 
# df = pd.read_excel('./Pandas/남북한발전전력량.xlsx', convert_float=True)
# df = df.loc[5:9]

# df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
# df.set_index('발전 전력별', inplace=True)
# df = df.transpose()

# # 증감율(변동률) 계산
# df = df.rename(columns={'합계':'총발전량'})
# df['총발전량 - 1년'] = df['총발전량'].shift(1)
# df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100      

# # 2축 그래프 그리기
# ax1 = df[['수력','화력']].plot(kind='bar', figsize=(15, 7), width=0.7, stacked=True)

# # 똑같은 객체를 복사해서 plot으로 특성을 변경한다.  
# ax2 = ax1.twinx()
# ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=20, 
#          color='green', label='전년대비 증감율(%)')  

# # ax1, ax2는 둘다 x축은 년도이다. 즉 index는 년도이다.

# ax1.set_ylim(0, 500)
# ax2.set_ylim(-50, 50)

# ax1.set_xlabel('연도', size=20)
# ax1.set_ylabel('발전량(억 KWh)')
# ax2.set_ylabel('전년 대비 증감율(%)')

# plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
# ax1.legend(loc='upper left')

# plt.show()


############################################################################## y축을 2개로. 즉 보조축을 가진 그래프
# plt.style.use('classic')   # 스타일 서식 지정

# # read_csv() 함수로 df 생성
# df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']

# # 연비(mpg) 열에 대한 히스토그램 그리기
# df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# # 그래프 꾸미기
# plt.title('Histogram')
# plt.xlabel('mpg')
# plt.show()



############################################################################## 산점도 그리기
# plt.style.use('classic')   # 스타일 서식 지정

# # read_csv() 함수로 df 생성
# df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']


# # 연비(mpg)와 차중(weight) 열에 대한 산점도 그리기
# # c="점색깔",s=점의 크기
# df.plot(kind='scatter', x='weight', y='mpg',  c='coral', s=10, figsize=(10, 5))
# plt.title('Scatter Plot - mpg vs. weight')
# plt.show()



# ############################################################################## 산점도 그리기(점의 크기를 달리한다.)
# plt.style.use('default')   # 스타일 서식 지정

# # read_csv() 함수로 df 생성
# df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']

# # cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
# cylinders_size = df.cylinders / df.cylinders.max() * 300
# print(cylinders_size)

# # 3개의 변수로 산점도 그리기 
# df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10, 5),
#         s=cylinders_size, alpha=0.3 )
# plt.title('Scatter Plot: mpg-weight-cylinders')
# plt.show()

############################################################################## 산점도 그리기(점의 크기, 색깔, 그림으로 저장하기)
# plt.style.use('default')   # 스타일 서식 지정

# # read_csv() 함수로 df 생성
# df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']

# # cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
# cylinders_size = df.cylinders / df.cylinders.max() * 300
# print(cylinders_size)

# # 3개의 변수로 산점도 그리기
# # cmap은 컬러 범위이다. 이것은 matplotlib 사이트를 참조한다. 
# df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
#         cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
# plt.title('Scatter Plot: mpg-weight-cylinders')

# plt.savefig("./Pandas/scatter.png")   
# plt.savefig("./Pandas/scatter_transparent.png", transparent=True)   

# plt.show()


# ############################################################################## 파이차트
# # read_csv() 함수로 df 생성
# df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# plt.style.use('default')   # 스타일 서식 지정

# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']


# # 데이터 개수 카운트를 위해 값 1을 가진 열을 추가
# df['count'] = 1
# df_origin = df.groupby('origin').sum()   # origin 열을 기준으로 그룹화, 합계 연산
# print(df_origin.head())                  # 그룹 연산 결과 출력

# # 제조국가(origin) 값을 실제 지역명으로 변경
# # 이렇게 하면 기존 인덱스는 사라진다.
# df_origin.index = ['USA', 'EU', 'JAPAN']
# print(df_origin)

# # 제조국가(origin) 열에 대한 파이 차트 그리기 – count 열 데이터 사용
# df_origin['count'].plot(kind='pie', 
#                      figsize=(7, 5),
#                      autopct='%1.1f%%',   # 퍼센트 % 표시
#                      startangle=10,       # 파이 조각을 나누는 시작점(각도 표시)
#                      colors=['chocolate', 'bisque', 'cadetblue']    # 색상 리스트
#                      )

# plt.title('Model Origin', size=20)
# plt.axis('equal')    # 파이 차트의 비율을 같게 (원에 가깝게) 조정
# plt.legend(labels=df_origin.index, loc='upper right')   # 범례 표시
# plt.show()


############################################################################## 박스 플롯

plt.style.use('seaborn-poster')            # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정

# read_csv() 함수로 df 생성
df = pd.read_csv('./Pandas/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메서드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'],
         vert=False)

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()