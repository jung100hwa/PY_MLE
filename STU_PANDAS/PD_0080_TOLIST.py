# 데이터프레임의 컬럼값을 리스트로 내보내기

import pandas as pd

values = [['aa',1],['bb',2],['cc',3]]
columns = ['col1','col2']
df = pd.DataFrame(values, columns=columns)
print(df)

print('col1:', df['col1'].to_list())