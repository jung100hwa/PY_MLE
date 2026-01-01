import pandas as pd
import numpy as np
from tabulate import tabulate

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90.012, 80, 90.23245],
             '영어' : [ 98, 89, 95],
             '음악' : [ 95.09, 95, '?'],
             '체육' : [ 100.0999, 90, np.nan]}
df = pd.DataFrame(exam_data)
ndf = df.copy()
print(tabulate(df, headers='keys', tablefmt='simple_outline'))

df['수학'] = df['수학'].round(2)
print(tabulate(df, headers='keys', tablefmt='simple_outline'))
