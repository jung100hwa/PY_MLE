# 인덱스값과 컬럼명을 재정의 하는건데 이것도 사용빈도 낮다. 
import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
print(df)

dic_index = {'준서':'jun', '예은':'yen'}
dic_columns = {'나이':'age','성별':'sex','학교':'school'}
df.rename(index=dic_index, columns=dic_columns, inplace=True)

print(df)