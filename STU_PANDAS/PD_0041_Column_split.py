# split 함수를 이용한 판다스 열분리
# 날짜 인덱스를 이용한 것과 비교할 만 함
from datetime import date
import pandas as pd

df = pd.read_excel('./E_FILE/주가데이터.xlsx')
print(df.head(5))
print(df.info())

# 연 월 일 데이터 분리하기
# 자료형을 문자열로 변경, str아래의 함수를 사용할려면 일단 변경해야 함
df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(type(dates))
print(dates.head())
 
 
# 시리즈의 값이 리스트일때 get 함수 활용, 범주형 날짜 다루는 것보다 용이함
print('\n===========================')
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df)

# test. 이렇게 복잡하게 할 필요가 있나. 일단 이런 부분은 하지 말자
print(dates[:])
# print(dates[0:2])
# print(dates)
df['year'] = [x[0] for x in dates[:]]
df['mon'] = [x[1] for x in dates[:]]
df['date'] = [x[2] for x in dates[:]]
print(df)

print(type(dates))
print(dates)

# 위에 처럼 어렵게 하지
df['year1'] = [x[0] for x in dates]
df['mon1'] = [x[1] for x in dates]
df['date1'] = [x[2] for x in dates]
print(df)