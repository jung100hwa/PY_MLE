import pandas as pd
import numpy as np
import re
# from numpy import reshape


st = '2025-05-27'
st = st[0:7]
print(stss)

#
# # 딕셔너리를 데이터 프레임으로 변경, 여기서 인덱스는 좌측 행인덱스
# # 딕셔너리 키에 해당하는 값의 구조가 같아야 한다. 아래는 모두 3개
# df = pd.DataFrame(
#     {"a": [4, 5, 6, 7],
#      "b": [7, 8, 9, 10],
#      "c": ["2026-07-02 00:02:09", "2026-07-02 00:02:09", "2026-07-02 00:02:09","2026-07-02 00:02:09"]}
# )
# print(df)
#
#
# df['c'] = df['c'].astype(str)
# print(df)
#
# df['c'] = pd.to_datetime(df['c'])
# print(df)


#
# for item in range(0,len(df)):
#     strv = df.iloc[item,2]
#     strv = strv[3:] + "kkkk"
#     df.iloc[item,2] = strv
#
# print(df)
#
# strv = "2026-07-02 00:02:09"
# strd = "2025-06-01"
# strv = re.sub('[\d]{4}-[\d]{2}-[\d]{2}',strd, strv)
# print(strv)

