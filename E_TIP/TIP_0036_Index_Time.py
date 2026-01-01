
# 인텍스가 시간일때는 데이터를 핸들링 할 수 있는 많은 방법들이 존재한다.

import pandas as pd

df = pd.read_csv('./E_FILE/PANDAS/stock-data.csv')
print(df.head())
print(df.info())


# 1단계 인덱스를 날짜 타입의 컬럼으로 변경
df['newDate'] = pd.to_datetime(df['Date'])
df.drop('Date', axis=1, inplace=True)
df.set_index('newDate', inplace=True)
print(df)

# 2단계 원하는 자료 가져오기. 이것은 날짜 타입이 인덱스 일때만 가능
print(df.loc['2018-07-02'])   # 원래는 이렇게 함, 보통은 이렇게 정확하게 해야 함
print(df.loc['2018-07'])      # 월까지만 해도 됨

# 3단계 이번에는 지정한 날짜부터 기간에 해당하는 데이터 출력
today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace=True)
print(df)


print("\n\n지정한 날짜부터 176 ~ 180일 기간까지의 데이터 출력")
ndf = df.loc['176 days':'180 days ']
print(ndf)


# 단계4 특정시간대의 데이터를 구함
i = pd.date_range('2018-04-09', periods=4, freq='1D20min')
ts = pd.DataFrame({'A': [1, 2, 3, 4]}, index=i)
print(ts)


# start~end 사이의 값을 구함
print(ts.between_time('0:15', '0:45'))


# end~start 바꾸면 그 외에 값을 구함
print(ts.between_time('0:45', '0:15'))