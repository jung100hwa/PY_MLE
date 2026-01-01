import pandas as pd
from scipy import stats

df = pd.read_csv("../E_FILE/PANDAS/survey.csv")

print(df.head())

# 여기서부터 t검정을 해보자, 두집단의 분산이나 표준편차를 구할 수 없을 때.
# t검정은 두집단(예를들면 남자와 여자 구분)으로 구분하고
# 다른 변수들이 구분자(남자와 여자)와 상관관계가 있는지 검정
# 즉 다른 변수들이 남자와 여자일때 뭔가 달라지는지
# 아래의 예제에서는 수입이 남자와 여자랑 관계가 있는지 검증
# 리턴값이 pvalue가 0.05 ~ 0.01 정도야지 관계가 유의미한 관계가 있다고 판단.

male = df.income[df.sex == 'm']
fmale = df.income[df.sex == 'f']
print(stats.ttest_ind(male, fmale))


# 테스트
# print(df.income[df.sex == 'm'])