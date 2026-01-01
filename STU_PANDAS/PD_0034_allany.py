from matplotlib.pyplot import axes
import pandas as pd
import numpy as np

# 시리즈나 데이터프레임에 특정 항목의 존재여부를 확인할 때 사용
# 데이터프레임에 적용시 (컬럼, 행, 또는 전체, axis에 따라) 단위로 참, 거짓 리턴

s = pd.Series([True, True]).all()
print(s)

s = pd.Series([True, False]).all()
print(s)

# 빈값을 True로 봄
s = pd.Series([], dtype="float64").all()
print(s)


s  = pd.Series([np.nan]).all()
print(s)


s = pd.Series([np.nan]).all(skipna=False)
print(s)


df = pd.DataFrame({'col1': [True, True], 'col2': [True, False]})
print(df)


# 컬럼단위로 계산해주네
print(df.all())


# 0은 false로 인식
df = pd.DataFrame({"A": [1, 2], "B": [0, 2], "C": [0, 0]})
print(df)
print(df.any())


# 컬럼을 기준으로 행을 탐색
print(df.all(axis=0))


# 행을 기준으로 컬럼을 탐색
print(df.all(axis=1))


# todo 데이터프레임 전체를 기준으로 함. 나중에 이것이 조금 쓸모 있겠다. 값중에 0이 있는지 확인 할 때
print(df.all(axis=None))

############################## 활용
df = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})
print(df)

# a컬럼에 4가 하나라도 있나라는 질문
print((df['a'] == 4).any())


# 조건문이랑 함께 사용
if (df['a'] == 4).any():
    print("yes")


# a컬럼의 값은 전부 7로만 되어 있는지
if (df['a']==7).all():
    print('yes')
else:
    print('no')


# todo 데이터프레임 전체에서 특정 문자가 포함되어 있는지 검색
# 이게 유용하네
if (df==6).any(axis=None):
    print('6 is ok')
else:
    print('no')


# 아래는 잘 안되네. str.contains는 타입을 object로 바꾼다고 되는게  아님. 숫자로만 된 컬럼은 object는 여전히 숫자로 인식하는 듯. string 변환
# 원래부터 문자열 이어야 하는듯

df = pd.DataFrame({
'a': [4, 5, 6, 7],
'b': [10, 20, 30, 40],
'c': [100, 50, -30, -50]
})

print(df)
print(df.info())

# 숫자는 확실하게 string 
df['a'] = df['a'].astype('string')
print(df)
print(df.info())
print(df['a'].str.contains('6'))

################################################ 25.05.11 테스트
cindex = df[df['a'].str.contains('6')].index
print(cindex)
print(len(cindex))
if len(cindex) >= 1:
    print("exist")

print(df['a'].str.contains('6').any())
print(df['a'].str.contains('6').all())

if df['a'].str.contains('6').all():
    print("exist")
else:
    print("not exist")
################################################


data_season1 = {"Player": ["Lewandowski", "Haland", "Ronaldo", "Messi", "Mbappe"],
                "Goals": [10, 8, 6, 5, 4]}

data_season2 = {"Player": ["Lewandowski", "Haland", "Ronaldo", "Messi", "Mbappe"],
                "Goals": [7, 8, 6, 7, 4]}


df_1 = pd.DataFrame(data_season1)
df_2 = pd.DataFrame(data_season2)


print(df_1)
print(df_2)

# 문자열 일때 contains함수 테스트
# 아래는 2개의 데이터프레임에서 행의 값이 다른 행을 출력(df_1)
# 아래는 df_1을 df_2와 한행씩 비교하면서 false이면 참이 되니까 출력(잘 생각해야 함) 
print(df_1[(df_1 == df_2).all(axis=1) == False])

# 이렇게 해도 되는 걸 뭘 이렇게 어렵게 하지. 코딩 어렵게 하지 말자
for item in range(0, len(df_1)):
    if df_1.iloc[item,1] == df_2.iloc[item,1]:
        print(df_1.iloc[item,1])