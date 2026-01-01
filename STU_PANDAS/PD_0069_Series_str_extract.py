import pandas as pd

s = pd.Series(['a1', 'b2', 'c3'])

# 하나의 요소를 아래와 같이 그룹 정규식으로 뽑아낸다
# 아래는 a 또는 b로 시작하고 다음에 숫자가 오는 것을 행과 열로 분리해서 출력
print(s.str.extract(r'([ab])(\d)'))

# expand값은 그룹이 하나 일때 시리즈 또는 데이터프레임으로 리턴할지를 결정
# 만약에 그룹이 2개일 때는 무조건 데이터프레임으로 리턴
print(s.str.extract(r'([ab])', expand=True))  # 데이터프레임
print(s.str.extract(r'([ab])', expand=False))  # 시리즈로 리턴

# 아래는 정규식 그룹이 2개이기 때문에 데이터프레임을 리턴한다.
print(s.str.extract(r'([ab])(\d)', expand=True))
print(s.str.extract(r'([ab])(\d)', expand=False))

# 모든 group을 만족해야 한다. 정규표현식의 ? 의미는 앞에 a 또는 b가 있어도 {0,1}의미이다.
print(s.str.extract(r'([ab])?(\d)'))

# 데이터프레임을 리턴할때 그룹명을 줄때 이 그룹명이 컬럼명이 된다. 
print(s.str.extract(r'(?P<letter>[ab])(?P<digit>\d)'))


s = pd.Series(['a1', 'b2', 'c3', 'a11b32'])

# extract 하나가 일치하면 나머지는 무시하고 처음것만 나온다.
print(s.str.extract(r'([ab])(\d)'))

# extractall은 하나의 시리즈값에서 일치하면 전체다 출력된다. 대신 일치하지 않는 것은 나오지 않음
print(s.str.extractall(r'([ab])(\d)'))

print(s.str.extractall(r'(?P<letter>[ab])(?P<digit>\d)'))

print(s.str.extractall(r'(?P<letter>[ab])?(?P<digit>\d)'))