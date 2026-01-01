
import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)


############################################# loc를 선택
# 하나의 행을 선택한다. 이럴때는 시리즈로 리턴한다. 데이터프레임으로 리턴을 워한면 [[]]
ndf = df.loc['서준']
print(ndf)

# 2개의 행을 리턴한다. 2개 이상일때는 [[]]
ndf = df.loc[['서준','우현']]
print(ndf)

# values는 값만 리턴하는데 여기에 슬라이싱을 해서 첫번째 값만 얻어 올수가 있다
xval = df.loc['서준'].values[0]
print(xval)


# 슬라이싱으로 적는다.
ndf = df.loc['서준':'우현']
print(ndf)


# 행과 열의 하나의 값만 선택하면 행명, 열명이 출력되지 않는다.
# 당연한다 이미 값이 행과 열명이 정의되어 있기 때문
ndf = df.loc['서준','수학'] # 이것은 행과 열임. 행의 인덱스는 [[]] 이형태나 슬라이싱을 해야 함.
print(ndf)


# 이렇게도 가능하다. 값수정이나 이럴때 편리할 것 같음
ndf = df.loc['서준']['영어']
print(ndf)


# 행과 열 범위를 선택하면 당연히 행과 열의 명칭까지 출력한다.
ndf = df.loc[['서준','우현'],['수학','영어']]
print(ndf)


# 하나의 행에 다수의 열을 선택하는 것도 가능하다.
ndf = df.loc['서준',['수학','영어']]
print(ndf)
print(type(ndf))


# 위의 값과 동일하나 아래는 데이터프레임이다. 즉 출력하고자 하는 값이 리스트, 튜플 등이면
# todo 항상 이런 형태로 하자
ndf = df.loc[['서준'],['수학','영어']]
print(ndf)
print(type(ndf))


# 보통 지금까지는 이렇게 함
print(df['수학'].loc['서준'])


# print(df.loc['서준','수학'])
print(df['수학'].loc[['서준','우현']])


# 이론 컬럼도 여러개 선택이 가능하네...
print(df)
print(df[['수학','영어']].loc['서준'])


############################### 251219일 추가
# 특정 행만 제외하고 가져오기
ndf = df.loc[df.index != '서준']
print(ndf)


############################################# iloc를 선택
print(df)
ndf = df.iloc[0]
print(ndf)


ndf = df.iloc[[0,1]]
print(ndf)


# todo 여기서 이름하고 차이가 있다. 인덱스로 슬라이싱 할 때에는 마지막값이 포함되지 않는다.
# df.iloc[0]과 차이는 데이터프레임을 리턴한다는 것이다. 슬라이싱은 항상 데이터프레임이다!!!!!


# 여기서는 서준과 우현이 포함된다.
ndf = df.loc[['서준','우현']]
print(ndf)


# 여기서도 서준과 우현이 포함된다. 이름으로 슬라이싱 할 때는 마지막값이 포함된다.
ndf = df.loc['서준':'우현']
print(ndf)


# 아래는 시리즈로 출력한다.
ndf = df.iloc[0]
print(ndf)

# todo 여기서는 인덱스 1이 포함되지 않는다. 그리고 슬라이싱은 항상 데이터프레임이다.
ndf = df.iloc[0:1]
print(ndf)


ndf = df.iloc[0:2, 0:2]
print(ndf)


# 마지막 인자에 슬아이싱 간격을 줄수가 있다.
ndf = df.iloc[::1]
print(ndf)


ndf = df.iloc[::2]
print(ndf)


# 슬라이싱 간격을 -로 주면 역순으로 출력
ndf = df.iloc[::-1]
print(ndf)


# 열은 슬라이신 간격이 먹지 않는다.
ndf = df.iloc[0:3:-1, 0:3:-1]
print(ndf)


############################################# df를 통한 원하는 열의 원하는 행 선택
# todo df를 통한 행 선택은 항상 슬라이싱만 지원
print('#' * 50)
print(df)
print(df['수학'])
print(df.수학)
print(df['수학']['서준':'우현'])
print(df['수학']['서준'])
print(df[['수학','영어']]['서준':'우현'])
# print(df[['수학','영어']]['서준'])



exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

print(df[['수학','영어']])

for index, val1 in enumerate(df['수학']):
    print(df['영어'].iloc[index])