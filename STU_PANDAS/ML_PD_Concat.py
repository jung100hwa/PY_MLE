# 단순하게 데이터프레임을 합치는 것
# align 함수도 참고로 해야함
from tabulate import tabulate
import pandas as pd

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                   index=[0, 1, 2, 3])


df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                   index=[2, 3, 4, 5])


print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))


# 기본적으로 outer라 모든 컬럼이 생성되고 컬럼값이 없으면 nan으로 된다.
result1 = pd.concat([df1, df2], axis=0)
print(tabulate(result1, headers='keys', tablefmt='simple_outline'))


# 새로 행인덱스를 메긴다. 행인덱스를 새로 생성하지 않으면 행인덱스가 겹친다.
# 단순하게 합칠 때 얘기
result2 = pd.concat([df1, df2], axis=0, ignore_index=True)
print(tabulate(result2, headers='keys', tablefmt='simple_outline'))


# 열방향으로 합친다. 이때는 행인덱스를 기준으로 한다. 일치하지 않은 행인덱스는 nan 처리된다.
result3 = pd.concat([df1, df2], axis=1, join='outer')
print(result3)


# outer 합집합, inner 교집합, 아래 inner는 축이 1일때 의미가 있다.
# 중요한게 ignore_index=True라서 인덱스를 새로 매기는데 axix=1이닌까 기존 컬럼(인덱스)을 0,1,2,3...새로매긴다.
print(tabulate(df1, headers='keys', tablefmt='simple_outline'))
print(tabulate(df2, headers='keys', tablefmt='simple_outline'))


result4 = pd.concat([df1, df2], axis=0, join='inner')
print(tabulate(result4, headers='keys', tablefmt='simple_outline'))


result4 = pd.concat([df1, df2], axis=1, join='inner')
print(tabulate(result4, headers='keys', tablefmt='simple_outline'))


# 동일컬럼이 존재하면 보기 싫으니까 다시 매긴다.
result4 = pd.concat([df1, df2], axis=1, join='inner', ignore_index=True)
print(tabulate(result4, headers='keys', tablefmt='simple_outline'))


# 시리즈를 데이터프레임에 추가한다.
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
result5 = pd.concat([df1, sr1, sr2, sr3], axis=1)
print(result5)