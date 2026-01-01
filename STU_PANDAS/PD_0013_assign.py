
# 기존 데이프레임에 새로운 컬럼을 할당하여 데이터프레임을 리턴
# 굳이 이것을 써야 하는 이유가 모르겠네

from this import s
import pandas as pd

df = pd.DataFrame({'temp_c': [17.0, 25.0]},
                  index=['Portland', 'Berkeley'])
print(df)


# 람다의 x는 데이터프레임 자체. 그러기 때문에 x.temp_c라는 표현이 가능함.
ndf = df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
print(ndf)


# 이렇게도 가능하다. 이렇게 사용하는 것이 맞을 듯 람다는 해석에 문제가 있음
ndf = df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)
print(ndf)


# 단순하게 이렇게도 가능함. 이렇게 하는게 가장 낫다.(추천)
s = df['temp_c'] * 9 / 5 + 32
df['temp_f'] = s
print(df)


# 추가하고자 하는 열을 계속추가하면 됨
ndf = df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
          temp_k=lambda x: (x['temp_f'] + 459.67) * 5 / 9)
print(ndf)
