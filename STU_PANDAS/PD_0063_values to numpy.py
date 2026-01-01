import numpy as np
import pandas as pd

# 데이터프레임 값을 넘파이 배열로 내보내기

df = pd.DataFrame({'age': [ 3, 29],
'height': [94, 170],
'weight': [31, 115]})

print(df)

print('############### array 내보내기')
num = df.values
print(num)

print('\n')
for item in num:
    print(item)
    for item2 in item:
        print(item2)
