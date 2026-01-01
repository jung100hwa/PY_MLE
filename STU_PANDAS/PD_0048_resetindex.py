import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 지정된 인덱스를 삭제하지 않고 정수형 인덱스로 초기화. 이건 조금 사용할 기회가 있겠다. 
df.reset_index(inplace=True)
print(df)

df.reset_index(names=['count'])