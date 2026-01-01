import pandas as pd
import numpy as np

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 95, 95, 100],
             '체육' : [ 100, 90, np.nan]}
df = pd.DataFrame(exam_data)
print(df)


# 유일한 값만 추출, NaN 출력 됨
print("="* 50)
print(df['체육'].unique())


# 유일한 값들의 수를 출력, NaN의 포함하지 않음, 값을 출력하는게 아니고 값의 수를 출력함.
print("="* 50)
print(df['체육'].nunique())


# 값들만 추출, 전체에 대해 NaN이 없은 행들만
print("="* 50)
print(df.value_counts())


print("="* 50)
print(df['체육'].value_counts())
print(df['체육'].value_counts().count())


# dropan=False NaN까지 구한다.
print("="* 50)
print(df['체육'].value_counts(dropna=False))


# 아래는 최고점수가 아닌 각 점수의 유일값에 대한 개수에 대한 최고값을 출력
print("="* 50)
print(df['음악'].value_counts())
print(df['음악'].value_counts(dropna=True).idxmax())


# 널값이 아닌 값들의 비율(거의 사용할 일이 없을 듯)
print("="* 50)
print(df['음악'].value_counts(normalize=True))


# 정렬, 오름차순, 데이터프레임 자체가 아닌 유일값들의 소팅
# 자료를 비교할 때나 검토할 때 유용할 것으로 판단됨
print("="* 50)
print(df['음악'].value_counts(sort=True, ascending=False))


##################################################################24년 09월 21일 테스트
import PY_PKG.SU_ALLMO_Init_MO as sai

sai.SU_MO_VarInit(sai.G_SU_INIT_LIST, 'auto-mpg_01.csv' )
df = pd.read_csv(sai.G_SU_ProFilLoc, header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df)
print(df.value_counts())
print(df.value_counts().count())
print(df.value_counts(dropna=True).count())
print(df.value_counts(dropna=False).count())
print(df['origin'].value_counts(sort=True, ascending=True))
print(df['origin'].value_counts(normalize=True))
