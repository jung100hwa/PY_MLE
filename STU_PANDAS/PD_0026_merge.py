from tabulate import tabulate
import pandas as pd
import os

os.chdir("c:\\projects\\PY_MLE")

df1 = pd.read_excel('./E_FILE/stock price.xlsx', index_col = 'id')
df2 = pd.read_excel('./E_FILE/stock valuation.xlsx', index_col = 'id')

print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))


# 두데이터 프레임 합치기, on=None 이면 2개의 데이터프레임에 공통적으로 들어있는 컬럼 기준
# None이니까 오류 나네
print('\n')
merge_inner = pd.merge(df1, df2, on='id')
print(tabulate(merge_inner, headers='keys', tablefmt='simple_outline'))

# 아래와 같이 해도 되네...
test_inner = df1.merge(df2, on='id')
print(tabulate(test_inner, headers='keys', tablefmt='simple_outline'))


# todo indicator를 True로 하면 "_merge"라는 컬럼이 추가되고 'both','left_only', 'right_only' 값들이 추가됨
test_df = df1.merge(df2, how='outer', on=['id'], indicator=True).loc[
    lambda x: x['_merge'] == 'left_only']


################################################################################## join으로 구현
# join index_col을 정의해 주어야 한다.
ndf = df1.join(df2, how='inner')
print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))

##################################################################################

# 공통된 열중에서 id 열을 기준으로 합친다, outer이기 때문에 양쪽에 있는 값 전체
merge_outer = pd.merge(df1, df2, on='id', how='outer')
print(tabulate(merge_outer, headers='keys', tablefmt='simple_outline'))
print(merge_outer)

################################################################################## join으로 구현

ndf = df1.join(df2, how='outer')
print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))
print(ndf)

##################################################################################

# 조인할 컬럼명을 지정한다. 보통은 이렇게 사용한다.
left_outer2 = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(tabulate(left_outer2, headers='keys', tablefmt='simple_outline'))


# align과 비교해서 사용할 것. align NaN 값을 다른 값으로 채출수도 있다.
# 데이터프레임 합치것 비교
df1 = pd.DataFrame({'a':['a0','a1','a2','a3'],
                   'b':['b0','b1','b2','b3'],
                   'c':['c0','c1','c2','c3']},
                  index = [0,1,2,3])

df2 = pd.DataFrame({'a':['a2','a3','a4','a5'],
                   'b':['b2','b3','b4','b5'],
                   'c':['c2','c3','c4','c5'],
                   'd':['d2','d3','d4','d5']},
                   index = [2,3,4,5])

print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))

# 행방향으로 단순하게 추가한다. 데이터프레임에 없는 컬럼은 NaN처리한다.
# 인덱스를 그대로 유지한다.
result1 = pd.concat([df1,df2])
print(tabulate(result1, headers='keys', tablefmt='simple_outline'))


# 컬럼기준일때는 join이나 merge로 대체가 가능하다.
result1 = pd.concat([df1,df2], axis=1)
print(tabulate(result1, headers='keys', tablefmt='simple_outline'))

################################################################################## join으로 구현
# 위에 컬럼 기준으로 했을 때에는 join 가능하다.
# 일단 한번 찍어보고
print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))

# 아래와 같이 하면 오류가 발생한다. 인덱스 컬럼 외에 동일한 컬럼명이 존재하기 때문에(a,b,c) 컬럼명에 프리픽스를 붙여주어야 한다.
# ndf = ndf1.join(ndf2, how='outer')
# print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))

# TODO 양쪽에 동일 컬럼이 존재할 경우 프리픽스를 주어서 구분해줘야 한다.
ndf = df1.join(df2, how='outer', lsuffix='_left', rsuffix='_right')
print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))
##################################################################################


################################################################################## merge으로 구현
# concat이 컬럼 기준일때 가능
df1.rename_axis('id', inplace=True)
df2.rename_axis('id', inplace=True)

print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))

# TODO merge는 동일 컬럼일때 알아서 서브픽스를 붙여준다.
merge_outer = pd.merge(df1, df2, on='id', how='outer')
print(tabulate(merge_outer, headers='keys', tablefmt='simple_outline'))
##################################################################################


# 인덱스를 재부여한다.
result2 = pd.concat([df1,df2], ignore_index=True)
print(tabulate(result2, headers='keys', tablefmt='simple_outline'))


# 컬럼을 이어서 붙인다
# 이때는 위에 예제를 보듯이 join , merge로 대체 가능하다. 가능하면 merger만 사용하자.
result3 = pd.concat([df1,df2],axis=1)
print(tabulate(result3, headers='keys', tablefmt='simple_outline'))

merge_outer = pd.merge(df1, df2, on='id', how='outer')
print(tabulate(merge_outer, headers='keys', tablefmt='simple_outline'))

# concat은 기본이 outer이다.
result3_in = pd.concat([df1,df2],axis=1, join='inner')   #열방향(axis=1), 교집합(inner)
print(tabulate(result3_in, headers='keys', tablefmt='simple_outline'))


merge_outer = pd.merge(df1, df2, on='id', how='inner')
print(tabulate(merge_outer, headers='keys', tablefmt='simple_outline'))


# 데이터프레임에 시리즈도 붙일 수 있다.
sr1 = pd.Series(['e0','e1','e2','e3'], name = 'e')
sr2 = pd.Series(['f0','f1','f2'], name = 'f', index = [3,4,5])
sr3 = pd.Series(['g0','g1','g2','g3'], name = 'g')

result4 = pd.concat([df1,sr1], axis=1)
print(result4, '\n')

result5 = pd.concat([df2,sr2], axis=1)
print(result5, '\n')


# 시리즈끼리도 결합할 수 있다.
result6 = pd.concat([sr1, sr3], axis = 1)  #열방향 연결, 데이터프레임
print(result6)
print(type(result6), '\n')

result7 = pd.concat([sr1, sr3], axis = 0)  #행방향 연결, 시리즈
print(result7)
print(type(result7), '\n') 
