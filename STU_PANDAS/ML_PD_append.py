import pandas as pd

# 이함수는 단순히 로우를 추가하는 것
# 사용할 일이 없다.

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
print(df)

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
print(df2)

ndf = df._append(df2)
print(ndf)