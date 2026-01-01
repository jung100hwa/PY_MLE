import pandas as pd

# 가능하면 소트는 하지 않는것이 좋다. 성능에 심각한 문제를 일으킨다.
# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# c4컬럼값을 내림차순으로 정렬
df.sort_values(by='c4',ascending=False, inplace=True)
print(df)

# 이렇게 하면 소팅을 해서 원하는 컬럼만 받아오기
ndf = df[['c0','c4']].sort_values(by='c4',ascending=False)
print(ndf)

print(df)
