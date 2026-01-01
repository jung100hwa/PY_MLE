import pandas as pd
import numpy as np

# 기본적으로 멤버를 연결 시킨다. 다른 옵션을 주지 않을 경우

s = pd.Series(["a", "b", np.nan, "d"])
print(s.str.cat(sep=" "))
print("\n")

# 널일경우 '-'으로 표시
print(s.str.cat(sep=" ", na_rep="-"))
print("\n")

# 조인 조건이 없으면 left join이 디폴트다. 값이 같은 경우가 아니라 인덱스가 같은 것끼리 조인한다.
# zip 함수와 비슷하네...
print(s.str.cat(["A", "B", "C", "D"], sep=","))
print("\n")

print(s.str.cat(["A", "B", "C", "D"], sep=",", na_rep="-"))
print("\n")


# join, 값이 아니라 같은 인덱스끼리 조인한다. 즉 아래에서 인덱스4에 해당하는 e는 조인되지 않는다.
s = pd.Series(["a", "b", np.nan, "d"])
t = pd.Series(["d", "a", "e", "c"], index=[3, 0, 4, 2])
print(s.str.cat(t, join="left", na_rep="-"))
print("\n")


print(s.str.cat(t, join="outer", na_rep="-"))
print("\n")

# inner 항상 양쪽에 있는 것끼리, NaN은 나온다.
print(s.str.cat(t, join="inner", na_rep="-"))
print("\n")

# right
print(s.str.cat(t, join="right", na_rep="-"))
print("\n")


############################################## 조금 활용
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [24, 42, 35],
        "state": ["NY", "CA", "LA"],
        "point": [64, 92, 75],
    }
)
print(df)
print("\n")

# 정말 할용도가 높을 듯. 아니네 그냥 묶으면 되지 않나.
print(df["name"].str.cat(df["state"], sep=" in ", na_rep="?"))
print("\n")

# +를 이용해서 합치기, 가능하면 이렇게 하지 말자. cat 함수 활용
# na 처리 등, 다양한 조인조건이 있는 것을 활용
print(df["name"] + " in " + df["state"])

# 문자열과 숫자열을 합칠 때 있단 숫자열을 문자열로 형변환 후에 가능하다.
# 숫자타입을 형변환하지 않고 하면 오류가 발생한다.
print(df["name"].str.cat(df["age"].astype(str), sep=" is ", na_rep="?"))
