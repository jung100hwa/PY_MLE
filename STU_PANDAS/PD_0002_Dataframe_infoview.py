import pandas as pd
import numpy as np
import PY_PKG.SU_ALLMO_Init_MO as sai

sai.SU_MO_VarInit(sai.G_SU_INIT_LIST, 'auto-mpg_01.csv' )
df = pd.read_csv(sai.G_SU_ProFilLoc, header=None)


# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())
print(df.tail())

# 열과 행을 표시한다.
print(df.shape)
print(df.info())


print("-------------")
rowcount = df.shape[0]
colcount = df.shape[1]
print(rowcount, colcount)


for icol in range(rowcount):
    print(df.iloc[icol:icol+1])


# 숫자컬럼만 표시
print(df.describe())


# 모든 열에 대한 정보 표시
print(df.describe(include='all'))


# 각 열마다 유효한 값에 대한 행의 개수(nan를 포함하지 않은 값)
print(df.count())


# count()는 해당컬럼의 모든 값의 개수, value_counts()는 해당컬럼의 유일값에 대한 개수
# NaN를 포함하지 않은 고유한값에 대한 개수(디폴트)
print(df['origin'].value_counts())
print(df['origin'].count())


# NaN를 포함하지 고유한값에 대한 개수
print(df['origin'].value_counts(dropna=True))
print(df['origin'].value_counts(dropna=False))


############################################################
ndf = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, np.nan]},
                  index=['falcon', 'dog', 'cat', 'ant'])
print(ndf)
print(ndf['num_wings'].value_counts(dropna=False)) # Null값을 포함
print(ndf['num_wings'].value_counts(dropna=True))  # Null값을 포함하지 않은 값, 디폴트값
print(ndf['num_wings'].count()) # non을 포함하지 않는 총개수
# print(ndf['num_wings'].count(dropna=False)) # 이런 파라미터는 없음
############################################################

# empty 함수. Null이 아닌 빈값을 체크한다. Null은 다른 의미 이다.
print("############################################## empty")
df = pd.DataFrame({'A' : []})
print(df)
if df.empty:
    print("df is empty")
else:
    print("df is not empty")
    
    
# null은 빈값이 아니다.
df = pd.DataFrame({'A' : [np.nan]})
if df.empty:
    print("df is empty")
else:
    print("df is not empty")

# 널 삭제후 empty 검토
df.dropna(inplace=True)
print(df)

if df.empty:
    print("df is empty")
else:
    print("df is not empty")

############################################################
#nan은 빈값과 다른 개념이다.
ndf2 = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, np.nan],
                    'num_wings2': [np.nan,np.nan,np.nan,np.nan]
                     },
                  index=['falcon', 'dog', 'cat', 'ant'])
print(ndf2)

if ndf2['num_wings2'].empty:
    print("empty")
else:
    print("no empty")

ndf3 = ndf2.copy()
print(ndf3)


# nan를 제외한 다음 다시 수행
# nan이 포함된 행을 삭제
ndf2.dropna(inplace=True, axis=0)
print(ndf2)


if ndf2['num_wings2'].empty:
    print("empty")
else:
    print("no empty")


# nan이 포함된 컬럼을 삭제
ndf3.dropna(inplace=True, axis=1)
print(ndf3)

############################################################