import pandas as pd

s = pd.Series(pd.date_range("2000-01-01", periods=3, freq="Y"))
print(s)

print(s.dt.date)
print(s.dt.time)
print(s.dt.timetz)
print(s.dt.year)

s2 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="M"))  # 월
print(s2)
print(s2.dt.month)

s3 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="D"))  # 일
print(s3)
print(s3.dt.day)

s4 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="H"))  # 시간
print(s4)
print(s4.dt.hour)

s5 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="T"))  # 분
print(s5)
print(s5.dt.minute)

s6 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="S"))  # 초
print(s6)
print(s6.dt.second)

s7 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="US"))  # 마이크로 세컨드
print(s7)
print(s7.dt.microsecond)

# 나노라서 그런지 더 세밀하게..
s8 = pd.Series(pd.date_range("2000-01-01", periods=3, freq="NS"))  # 마이크로 세컨드
print(s8)
print(s8.dt.nanosecond)

# 일장에 해당하는 요일(0-월요일 , 6-일요일)
s = pd.date_range("2024-10-31", "2024-11-02", freq="D").to_series()
print(s)
print(s.dt.dayofweek)

# 일년 중 해당 년월일은 몆주째인가
# 아래 함수가 오류가 나네
# print(s.dt.week)

# 년 월 일 옵션이 없으면 일 기준
s = pd.Series(pd.date_range("2023-10-15", periods=3))
print(s)

# 그달의 시작인지 끝인지 참거짓으로 리턴
print(s.dt.is_month_start)

print(s.dt.is_month_end)


########################################### 날짜 관련 메소드
df = pd.DataFrame(
    {"y": [1, 2, 3]},
    index=pd.to_datetime(
        ["2000-03-31 00:00:00", "2000-05-31 00:00:00", "2000-08-31 00:00:00"]
    ),
)

print(df)

print(df.index.to_period("M"))

print(df.index.to_period("D"))

# 날짜를 정해진 포맷으로 변환, 넘파이 배열로 리턴
s = pd.date_range(pd.Timestamp("2022-01-02 12:00"), periods=3, freq="H")
print(s)

# 데이터타입이 datetime이기 때문에 s.strftime 가능함. 시리즈 일때는 s.dt.strftime으로 해야 함
print(type(s))

ser = pd.Series(s)
print(type(ser))
print(ser)

# 월을 영문으로 리스트로 변환해서 출력
rs = list(s.strftime("%Y-%m-%d"))
print(rs)

rs = list(ser.dt.strftime("%Y-%m-%d"))
print(rs)

# 시간을 24시로 표시
rs = list(s.strftime("%Y-%m-%d-%H"))
print(rs)

# 시간을 12시로 표시
rs = list(s.strftime("%Y-%m-%d-%I"))
print(rs)

# 정의할 때 시간까지만 정했기 때문에 분 초는 0 이다
rs = list(s.strftime("%Y-%m-%d-%M-%S"))
print(rs)

# 요일을 영문으로
rs = list(s.strftime("%Y-%m-%d-%A"))
print(rs)

# 요일 영문의 단축
rs = list(s.strftime("%Y-%m-%d-%a"))
print(rs)

# 월 영문
rs = list(s.strftime("%Y-%B-%d"))
print(rs)

# 월영문 단축
rs = list(s.strftime("%Y-%b-%d"))
print(rs)


s = pd.date_range(pd.Timestamp("2022-01-02 12:00"), periods=3, freq="D")
print(s)

# 주간보고 같은데 써먹을 수 있을 것 같은데
rs = list(s.strftime("월요일 기준 년중 %W 주, 일요일 기준 년중 %U 주, 년중 %j 일"))
print(rs)


# 시간. 분, 초 등을 기준으로 반올림 어떻게 할지를 고민 함
df = pd.DataFrame(
    pd.to_datetime(
        ["2020-01-02 11:59:00", "2020-01-02 11:02:00", "2020-01-02 11:32:00"]
    ),
    columns=["da"],
)
print(df["da"])

# 시간을 기준으로 반올림. 즉 분을 보고 30분이 넘으면 다음 시간
print(df["da"].dt.round(freq="H"))
print(df["da"].dt.round("H"))

# 이것과 동일하다. 시리즈에서 바로 사용하기 위해서는..
print(df["da"].round("H"))

# 아래 nonexistent의 옵션은 해당 시간이 존재하지 않을 때 얘기 인듯 한데
# 데이터 사전작업을 먼저해야 하는게 낫지 않나. 먹지도 않네
print(df["da"])
print(df["da"].dt.round(nonexistent="shift_forward", freq="H"))
print(df["da"].dt.round(nonexistent="shift_backward", freq="H"))


# 아래 내림계산과 올림계산은 반올림이 아님, round하고는 다름
# 내림계산
print(df["da"].dt.floor(freq="H"))

# 올림계산
print(df["da"].dt.ceil(freq="H"))
