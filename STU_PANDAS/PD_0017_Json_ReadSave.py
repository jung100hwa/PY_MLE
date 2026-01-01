import pandas as pd

# read_json() 함수로 데이터프레임 변환 
df = pd.read_json('./E_FILE/read_json_sample.json')
print(df)


# json 내보내기
data = {'name':['Jerry','Riah','Paul'],
'algol':['A','A+','B'],
'basic': ['C','B','B+'],
'c++' : ['B+','C','C+']}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_json('./E_FILE/df_sample.json')