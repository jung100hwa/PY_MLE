import pandas as pd
import numpy as np

# 이 함수는 인덱스가 시간일때 일정한 간격으로데이터를 넣어준다.

index = pd.date_range('1/1/2000', periods=4, freq='T')
series = pd.Series([0.0, None, 2.0, 3.0], index=index)
df = pd.DataFrame({'s': series})

print(df)

# 30초 단위로 행을 추가 한다. 값은 100
ndf = df.asfreq(freq='30S', fill_value=100)
print(ndf)

# 이전값을 넣어준다
ndf = df.asfreq(freq='30S', method='bfill')
print(ndf)