"""
우리가 일반적으로 db 핸들링시 sql를 사용하는데 데이터프레임에도 sql사용할 수 있다
우리가 할수 있는 모든 쿼리를 지원한다고 보면 된다.
pip install pandasql를 설치 해야 한다.
"""

import pandas as pd
import pandasql as psql


# 예제 데이터
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['Seoul', 'Busan', 'Incheon', 'Daegu']}

df = pd.DataFrame(data)
print(df)

print("-" * 50)

# 기본적인 쿼리
query = "select * from df where Age > 30"
result = psql.sqldf(query)
print(result)


data2 = {'Name': ['Alice', 'Charlie'],
         'Salary': [5000, 7000]}
df2 = pd.DataFrame(data2)

# 조인도 지원(컬럼명 대소문자 상관없네)
print("-" * 50)
query = "select df.name, df.age, df2.salary from df left join df2 on df.name = df2.name"
result = psql.sqldf(query)
print(result)

# 정렬
print("-" * 50)
query = "select * from df order by city desc"
result = psql.sqldf(query)
print(result)

