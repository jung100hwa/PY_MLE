"""
두개의 시리즈를 합치는 것
예제를 보는 것이 나을 듯 함
"""

import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [24, 42, 35],
        "state": ["NY", "CA", "LA"],
        "point": [64, 92, 75],
    }
)

# cat은 2개의 시리즈를 합치는데 값이 아닌 인덱스를 기준으로 함
print(df["name"].str.cat(df["state"], sep=" in ", na_rep="?"))
print("\n")