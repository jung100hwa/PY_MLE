import numpy as np
import pandas as pd
import seaborn as sns

# 이 함수는 숫자형 컬럼끼리 계산을 하여 새로운 컬럼을 만들거나 아니면 시리즈로 리턴한다.
# cut, np.histogram 이 함수의 조합을 한번에 할 수 있을 것 같음

pd.options.display.float_format = '{:,.2f}'.format # 소수점 2자리에서 반올림 + 천단위 쉼표

data = {'몸무게': [95, 70, 65, 45, 85],
        '키': [170, 170, 170, 170, 170]}
df = pd.DataFrame(data)
print(df)

# 키와 몸무게 더하기
print("=" * 50)
result = df.eval('몸무게 + 키') # 이때는 시리즈로 리턴함
print(result)

# BMI지수를 구해 보자
df.eval('BMI = 몸무게 / ((키 / 100) * (키 / 100))', inplace=True)
print(df)

# 논리연산을 해보자
df.eval('LOC = 몸무게 > 90', inplace=True)
print(df)

# loc와 함께 하나의 칼럼에 다른 값을 넣어 보자. 
df.loc[df.eval('               BMI < 18 '), '분류'] = '저체중'
df.loc[df.eval(' 18 <= BMI and BMI < 23 '), '분류'] = '정상'
df.loc[df.eval(' 23 <= BMI and BMI < 25 '), '분류'] = '과체중'
df.loc[df.eval(' 25 <= BMI and BMI < 30 '), '분류'] = '비만'
df.loc[df.eval(' 30 <= BMI              '), '분류'] = '고도비만'
print(df)

# 이게 가능한가
print(df.eval(' 18 <= BMI and BMI < 23 '))

# BMI 지수를 기반으로 소팅. 이거 정말 많이 쓰겠다. 그냥 소팅이 아니라 BMI 오름차순의 순서의 값 즉 BMI 15.57이 가장 작기 때문에 1이된다.
# 속도가 중요한 곳에서는 inplace를 가급적 사용하지 말자.
df['BMI_rank'] = df['BMI'].rank(ascending=True)
print(df)

# 이렇게 하는 것은 보여주기 위한 것으로 실제 코딩에서는 하지 않는게 좋다.
# 다만 엑셀로 뽑아야 할 경우가 있으면 하는데 엑셀로 일단 뽑아놓고 엑셀에서 소팅하는것을 추천한다.
df.sort_values(by=['BMI_rank'], ascending=[True], inplace=True)
print(df)

# loc가 앞에 조건이 될 수가 있나.
data = {'aa': [95, 70, 65, 45, 85],
        'bb': [170, 170, 170, 170, 170]}
df = pd.DataFrame(data)
print(df)

# 이와 같은 예시는 앞으로 하지 말자. 이게 말이돼. 이런걸 코딩에 쓸 이유가 없지
df.loc[[True,True,True,False,False],'cc'] = 300
print(df)

# print(df.loc[df.eval('aa > 90')])
# print(df.loc[1,:])
