import pandas as pd
import numpy as np

from tabulate import tabulate

pd.set_option('display.max_columns', 50)

# read_csv() 함수로 df 생성
df = pd.read_csv('./E_FILE/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin', 'name']


print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

# method = 'pearson', 'spearman', 'kendall'이것들 중의 하나
# +1은 양의 상관관계,-1은 음의 상관관계. 여하튼 +, - 이면 관계가 있다는 것이다.
# 0이면 관계가 없다는 것이다. 관계파악에서 필요할 듯

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')



# 숫자가 아닌 컬럼 삭제
df.drop(['name'], axis=1, inplace=True)

print(df.info())

ndf = df.corr(method='pearson')
print(tabulate(ndf.head(), headers='keys', tablefmt='simple_outline'))