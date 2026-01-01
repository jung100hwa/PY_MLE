
from tabulate import tabulate
import pandas as pd


#join은 반드시 index_col이 있어야 한다.
df1 = pd.read_excel('./E_FILE/stock price.xlsx', index_col='id')
df2 = pd.read_excel('./E_FILE/stock valuation.xlsx', index_col='id')

print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))

# join의 기본은 left outer join, todo 인덱스 컬럼을 기준으로 함
df3 = df1.join(df2, how='left')
print(tabulate(df3, headers='keys', tablefmt='simple_outline'))

# 양쪽에 공통으로 존재하는 값만 -> inner
print('\n')
df4 = df1.join(df2, how='inner')
print(tabulate(df4, headers='keys', tablefmt='simple_outline'))