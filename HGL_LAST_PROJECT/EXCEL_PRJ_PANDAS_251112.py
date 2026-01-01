"""
-일자:2025.11.12
-내용:판다스를 이용한 엑셀 다루기
-장점
 : openpyxl모드 다루기 쉽고 판다스의 모든 작업을 활용할 수가 있다.
 : 판다스는 openpyxl, xlrd를 동시에 사용한다.
 # todo openpyxl은 xlsx, xlrd는 xls를 열때 사용한다.
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.chdir(r"c:\projects\PY_MLE\HGL_LAST_PROJECT")

import pandas as pd

# openpyxl에서 불러올 수 없는 xls파일도 불러온다(내부적으로 xlrd 모듈을 사용)
# df = pd.read_excel('oldexcel.xls', header=0)
# print(df)


df = pd.read_excel('./lastsample/EXCEL_PRJ_TEST01.xlsx', header=0)
df.set_index('번호', inplace=True)
print(df)


# 컬럼타입을 조사해서 컬럼타입에 해당하는 합계, 최근일 등을 구해보자
# todo 아래와 같이 조사하면 절대 안됨. 무조건 str. 컬럼명에 타입이니까
# for column in df.columns:
#     print(type(column))


# 이렇게 해야 한다.
for column in df.columns:
    print(column, df[column].dtype)


df['금액'] = df['금액'].astype('float')
namemax = df['이름'].max()
monysum=df['금액'].sum()
datamax=df['날짜'].max()
print(df)

# 이렇게도 되고
# rowdf = pd.DataFrame({'이름':['합계'],'금액':[monysum],'날짜':[datamax]})
# ndf = pd.concat([df, rowdf], ignore_index=True)

# 이렇게도 됨
ndf=df.copy()
rowcount = len(df)
ndf.loc['TOT'] = [namemax,monysum,datamax]
print(ndf)

ndf.to_excel('.\lastsample\EXCEL_PRJ_TEST01_RESULT.xlsx')