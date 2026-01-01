import pandas as pd
from scipy import stats

df = pd.read_csv("./E_FILE/survey.csv")
# df = pd.read_csv("./PANDAS/survey.csv")

print(df.head())

print('=' * 50)
print('평균 조회')
print(df.mean())  # 오류 문자열이 있기 때문

print('=' * 50)
print('기초 통계랑')
print(df.describe())

# 빈도 분석은 컬럼 단위로
print('=' * 50)
print('빈도 분석')
print(df.sex.value_counts())


# 남자와 여자 평균을 구해보자
print('=' * 50)
print('남자와 여자 평균을 구해보자')
ndf = df.groupby(['sex'])
print(ndf.mean())


# 여기서부터 t검정을 해보자, 두집단의 분산이나 표준편차를 구할 수 없을 때.
# t검정은 두집단(예를들면 남자와 여자 구분)으로 구분하고
# 다른 변수들이 구분자(남자와 여자)와 상관관계가 있는지 검정
# 즉 다른 변수들이 남자와 여자일때 뭔가 달라지는지
# 아래의 예제에서는 수입이 남자와 여자랑 관계가 있는지 검증
# 리턴값이 pvalue가 0.05 ~ 0.01 정도야지 관계가 유의미한 관계가 있다고 판단.
male = df.income[df.sex == 'm']
fmale = df.income[df.sex == 'f']
print(stats.ttest_ind(male, fmale))


