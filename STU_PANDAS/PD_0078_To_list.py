# 데이터프레임 중 원하는 컬럼만 리스트로 출력
# zip 함수를 이용해서 묶기


import pandas as pd

df = pd.read_excel('./E_FILE/서울지역 대학교 위치.xlsx', index_col=0)
print(df)

# 위 데이터프레임(대학교명, 위도, 경도) 중에서 위도, 경도만 리스트로 출력, 컬럼단위로 밖에 안됨
xlist = df['위도'].tolist()
ylist = df['경도'].tolist()

print(xlist)
print(ylist)

# zip함수를 이용해서 묶기
xylist = list(zip(xlist,ylist))
print(xylist)

# 아래는 대학교명, 위도, 경도가 다 출력된다. 이유는 상단에 index_col=0으로 했기 때문에 "대학교명"은 인덱스이지 컬럼이 아니기 때문
# 아래에서 tolist()함수는 먹지 않는다. 2개 이상 컬럼은 먹지 않는다. 이게 무슨 말이지
xylistd = df[['위도','경도']]
print(xylistd)

df = pd.read_excel('./E_FILE/서울지역 대학교 위치.xlsx')
xylistd = df[['위도','경도']]
print(xylistd)

print(df)

################################# 다시 원하는 컬럼만 리스트로 내보내기 하면 되는 것 아닌가
xlist = df['위도'].tolist()
ylist = df['경도'].tolist()
xylist = list(zip(xlist,ylist))
print(xylist)
#################################