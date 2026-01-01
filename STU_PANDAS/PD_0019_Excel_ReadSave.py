# -*- coding: utf-8 -*-
# import sys
# sys.path.append("c:\\work\\MLE")

import pandas as pd

# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('E_FILE/남북한발전전력량.xlsx')               # header=0 (default 옵션)
df2 = pd.read_excel('E_FILE/남북한발전전력량.xlsx', header=None)  # header=None 옵션
df3 = pd.read_excel('E_FILE/남북한발전전력량.xlsx', header=None)  # header=None 옵션

# 데이터프레임 출력
print(df1)
print('\n')

print(df2)
print('\n')

print(df3)

data = {'name':['Jerry','Riah','Paul'],
'algol':['A','A+','B'],
'basic': ['C','B','B+'],
'c++' : ['B+','C','C+']}


df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# 내부적으로 openxl 라이브러리를 이용한다.
# df.to_excel('./Pandas/df_smaple.xlsx')


# 여러개의 데이터프레임을 하나의 엑셀시트에 저장하기
data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c2':[7,8,9],
         'c3':[10,11,12],
         'c4':[13,14,15]}


df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)


writer = pd.ExcelWriter('E_FILE/df_excelsheet.xlsx')
df.to_excel(writer, sheet_name='df1')
df2.to_excel(writer, sheet_name='df2')

writer.close()
