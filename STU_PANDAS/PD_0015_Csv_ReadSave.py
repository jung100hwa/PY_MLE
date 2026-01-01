
# 라이브러리 불러오기
import pandas as pd

# 파일경로를 찾고, 변수 file_path에 저장
file_path = './E_FILE/read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환. 변수 df1에 저장
# header = 0이 디폴트이다. 0이면 첫번째 행을 데이터프레임의 헤더로 사용
df1 = pd.read_csv(file_path)
print(df1)
print('\n')


# read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. header=None 옵션
# none 이면 헤더를 기존 파일에 있는 첫행을 사용하지 않고 임으로 0,1,2,3....
# 이렇게 정의한다.
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')


# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)


# CSV로 저장함. 요즘은 엑셀로 저장함. CSV로 하지 않음
data = {'name':['Jerry1','Riah1','Paul1'],
'algol':['A','A+','B'],
'basic': ['C','B','B+'],
'c++' : ['B+','C','C+']}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_csv('./df_sample.csv')

