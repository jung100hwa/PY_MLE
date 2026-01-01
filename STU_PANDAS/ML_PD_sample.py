"""
데이터를 적절하게 섞어 준다. 주로 딥러닝에서 훈련과 검증, 테스트를 할때 사용한다.
무작위로 지정한 행의 개수를 출력해 준다.
1. 먼저 개수로 추출하는 방법
2. frac=비율값 비율값으로 추출하는 방법, todo 만약에 1이면 전체를 섞는 효과가 있음
"""

import pandas as pd

df = pd.DataFrame({"이름" : ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III", "JJJ"],
                   "반" : [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
                   "점수" : [67, 100, 12, 85, 13, 92, 27, 5, 100, 98]})

print(df)

# 먼저 n개의 행을 추출할 수 있음
print(df.sample(3, random_state=11))

print("\n" * 2)
# 비율로 추출하는 방법
print(df.sample(frac=1, random_state=23))

