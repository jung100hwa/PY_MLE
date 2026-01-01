# 첫글자를 슬라이싱 해서 세대 구하기

import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie']
                      , 'age': [24, 42, 35]
                      , 'state': ['NY', 'CA', 'LA']
                      , 'point': [64, 92, 75]})

print(df)

# 먼저 스트링 타입으로 바꾸고, 첫번째 부터 끝까지를 "0 대"로 치환
df['SED'] = df['age'].astype(str).str.slice_replace(start=1, repl='0대')
print(df)