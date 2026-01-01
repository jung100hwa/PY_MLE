import pandas as pd

s = pd.Series(['dog',
               '',
               5,
               {'foo' : 'bar'},
               [2, 3, 5, 7],
               ('one', 'two', 'three')])
print(s)

# 각 요소에 대한 길이
print(s.str.len())

# 시리즈 개수
print(len(s))