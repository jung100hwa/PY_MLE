# 인덱스를 정의하는 것 이것도 활용도는 높지 않다.
# 판다스는 분석을 위한 것이지만 선행조건이 기본 데이터 정비를 한후에 해야 한다.

import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

# copy함수를 적어도 된다.
ndf = df[:]
ndf.set_index('이름', inplace=True)
print(ndf)

# 새로운 인덱스를 부여할 때마다 기존 인덱스는 삭제된다.
ndf.set_index('수학', inplace=True)
print(ndf)

# 멀티 인덱스를 부여할 수도있다
ndf = df[:]
ndf.set_index(['이름','수학'], inplace=True)
print(ndf)