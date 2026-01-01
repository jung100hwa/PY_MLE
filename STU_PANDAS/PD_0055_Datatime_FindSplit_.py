# 시계열 데이터 다루기

import pandas as pd
import os
from tabulate import tabulate

G_ExFilePos = os.getcwd()
df = pd.read_csv('./E_FILE/stock-data.csv')

print(df.head())
print(df.info())    # Date 컬럼이 object형 확인

# new_date열을 만들고 추가해서 정보보기. 데이터타입으로
df['new_date'] = pd.to_datetime(df['Date'])
print(df.head())
print(df.info())
print(df)
print('\n')

# new_date를 행인덱스로 설정하고 기존 date 제거.
# 원래 기존 데이터가 인덱스로 잡혀 있으면 새로운 인덱스 설정시 자동 삭제됨
df.set_index('new_date', inplace=True)
df.drop('Date', axis=1, inplace=True)
print(df.head())
print(df.info())
print('\n')


# timestamp를 period로 변환(결국 시간데이터를 일까지만, 월까지만, 년까지 보여 줄것인지)
dates = ['2019-01-01', '2020-03-01', '2021-06-01']
to_dates = pd.to_datetime(dates)
print(to_dates)
print('\n')

pr_day = to_dates.to_period(freq='D')   # 일까지
print(pr_day)
pr_mon = to_dates.to_period(freq='M')   # 월까지
print(pr_mon)
pr_year = to_dates.to_period(freq='A')  # 년까지
print(pr_year)
print('\n')

# 시계열 데이터 만들기
# 조건이 MS 이기 때문에 월초
ts_ms = pd.date_range(start='2019-01-01',
                      end=None,
                      periods=6,    # 6개 데이터
                      freq='MS',    # 월의 시작 그냥 'M'이면 월말
                      tz='Asia/Seoul')
print(ts_ms)
print('\n')

# 6개의 데이터를 만들어 내는데 그냥 M이닌까 월말, 원래 ME의 의미
ts_ms = pd.date_range(start='2019-01-01',
                      end=None,
                      periods=6,
                      freq='M',    # 월의 시작 그냥 'M'이면 월말
                      tz='Asia/Seoul')
print(ts_ms)
print('\n')

# 1개월 간격
pr_ms = pd.period_range(start='2019-01-01',
                        periods=3,
                        freq='M')   # 함수에 따라 월까지, 월의 마지막 일까지 다양
print(pr_ms)
print('\n')

# 1시간 간격
pr_ms = pd.period_range(start='2019-01-01',
                        end=None,
                        periods=3,
                        freq='H')   # 함수에 따라 월까지, 월의 마지막 일까지 다양
print(pr_ms)
print('\n')

# 2시간 간격
pr_ms = pd.period_range(start='2019-01-01',
                        end=None,
                        periods=3,
                        freq='2H')   # 함수에 따라 월까지, 월의 마지막 일까지 다양
print(pr_ms)
print('\n')


######################################################
# 데이터타임 즉 타임스템프 형태로 인덱싱이 주어진 데이터프레임은 df['날짜검색조건']
# 바로 검색이 가능한다. loc 속성을 이용해서 날짜 인덱싱 검색조건과 해당열만 불러올수도 있다
######################################################

udf = pd.read_csv('./E_FILE/stock-data.csv')

# timestamp로 열의 타입으로 바꾸고
udf['new_date'] = pd.to_datetime(udf['Date'])
print(udf)
print('\n')

# 년, 월, 일 뽑아내기. 뽑아내는 방법은 다양한다.
udf['Year'] = udf['new_date'].dt.year
udf['Mon'] = udf['new_date'].dt.month
udf['Day'] = udf['new_date'].dt.day
print(udf.head(10))
print('\n')

# 아래와 같이 문자열로 바꾸어서 split 한 다음. 시리즈에서 get 함수를 이용해서 불러와서 컬럼을 만들면 된다.
# udf['sss'] = udf['new_date'].astype(str)
# dates = udf['sss'].str.split('-')
# print(type(dates))
# print(dates.head())

# udf['s1'] = dates.str.get(0)
# udf['s2'] = dates.str.get(1)
# udf['s3'] = dates.str.get(2)

# print(udf)


# 타임스템프를 피리어드로 변환해서 년, 월, 일 추출. 이 방법이 가장 낫네.
udf['Data_y'] = udf['new_date'].dt.to_period(freq='A')    # 년까지만
udf['Data_m'] = udf['new_date'].dt.to_period(freq='M')    # 월까지만
udf.set_index('Data_m', inplace=True)
print(udf.head(10))
print(tabulate(udf.head(), headers='keys', tablefmt='simple_outline'))

print('\n')

# 날짜 인덱스를 이용한 인덱싱, 슬라이싱
print('\n==================================')
# 먼저 타임스템프로 만든 다음 인덱싱으로 지정해야 함
udf.set_index(udf['new_date'], inplace=True)
print(udf)
print('\n')


# 원래 loc행 인덱스값 또는 조건, 컬럼값 또는 조건이 오는데 2018-01도 아니고 그냥 2018해도 됨
df_y = udf.loc['2018-07']
print(df_y)


# loc 속성을 이용해서 검색, 행조건과 특정열만
# 날짜가 인덱스로 잡혀 있으닌까. loc행인덱스 또는 검색조건 뿐만아니라. 그냥 년을 적어도 됨
df_col = udf.loc['2018','Start':'High']
print(df_col)
print('\n')

print('\n==================================날짜인덱스')
# 원래 일반적인 인덱스 일때는 이렇게 하면 안되는데 날짜 인덱스 일때는 가능하다.
# 보통 df[] 열명이 온다.
print(udf)
df_ymd = udf['2018-06-01':'2018-06-20']
# df_ymd = udf['2018-06':'2018-07']
print(df_ymd)
print('\n')

# 최근 180일 ~ 189일 데이터만 선택
# 2018-12-25일를 기준으로 180일 전 부터 190일 전까지 데이터를 구함
# 인덱스가 차이를 의미하지 데이터타임을 의미 하지 않기 때문 조건검색해야 함. 날짜 인덱스가 아니기 때문에
print('\n==================================')
today = pd.to_datetime('2018-12-25')
print(tabulate(udf.head(), headers='keys', tablefmt='simple_outline'))

# 아래는 index, Date object 형이라 오류 남
# udf['time_delta'] = today - udf.index
# udf['time_delta'] = today - udf.Date
udf['aaa'] = pd.to_datetime(udf['Date'])
print(udf.info())
udf['time_delta'] = today - udf.aaa

udf.set_index('time_delta', inplace=True)
print(tabulate(udf.head(), headers='keys', tablefmt='simple_outline'))
print('\n')


# 이것은 날짜 인덱스일 경우만 해당 됨. 즉 조건검색을 대신함.
udf_180 = udf['180 days':'189 days']
print(udf_180)


print('\n==================================')
# 이것은 단지 순차적일때 행과 열의 범위 사이를 리턴(조건에 의한 검색이 아님)
# 189일까지 이니까.189도 포함해야 한다. 다른 범위일때는 포함되지 않는 것으로 알고 있다.
udf_180_1 = udf_180.loc['180 days':'189 days',:]
print(tabulate(udf_180_1, headers='keys', tablefmt='simple_outline'))


# 특정시간대의 데이터를 구함, 아래는 하루 10분 간격으로 4개의 데이터를 만들어 냄
i = pd.date_range('2018-04-09', periods=4, freq='1D20min')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
print(ts)

# start~end 사이의 값을 구함
print(ts.between_time('0:15', '0:45'))

# end~start 바꾸면 그 외에 값을 구함
print(ts.between_time('0:45', '0:15'))