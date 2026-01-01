# 2개의 구조가 같은 데이터프레임이 있고 값을 비교해서 적은값 또는 큰값으로 구성된 새로운 데이터프레임을 생성할 때 유용하게 사용

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [10, 11, 1], 'B': [13, 14, 6]})

# 두개의 데이터 프레임에서 적은 값으만 구성된 새로운 데이터 프레임 생성
df = df1.combine(df2, np.minimum)
print(df)

# 넘파이 함수를 이용해서 해보자, 이렇게 하는게 나을 듯.
ndf = pd.DataFrame(np.minimum(df1.values, df2.values))
print(ndf)