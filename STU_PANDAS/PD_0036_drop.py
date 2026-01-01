import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

# 우현 행을 삭제한다.
# 아래 복사하는 방법을 잘 알아두자
ndf = df[:]
ndf.drop('우현',axis=0, inplace=True)
print(ndf)


# 서준, 우현 행을 삭제한다. axis가 함수마다 약간씩 의미가 틀린듯
ndf = df[:]
ndf.drop(['서준','우현'], axis=0, inplace=True)
print(ndf)


# 인덱스를 적으면 axis 적을 필요가 없다.
ndf = df[:]
ndf.drop(index=['서준', '우현'], inplace=True)
print(ndf)


# 컬럼을 삭제한다.
ndf = df.copy()
ndf.drop('수학', axis=1, inplace=True)
print(ndf)


# 여러 컬럼을 삭제한다.
ndf = df.copy()
ndf.drop(['수학','영어'], axis=1, inplace=True)
print(ndf)


# columns 적으면 axis를 적을 필요가 없다. 이런것 까지 외워야 하나.
ndf = df.copy()
ndf.drop(columns=['영어', '체육'], inplace=True)
print(ndf)

# 이런 함수를 굳이 외울필요는 없다. 뒤에 행은 범위로만 선택 가능 함.
# todo 가능하면 이런 방식을 쓰지 않는게 낫다. df로 행까지 선택할 때 행은 범위로만 선택이 가능함.
ndf = df[['수학','영어']]['서준':'우현']
print(ndf)