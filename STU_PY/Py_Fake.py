from faker import Faker
import pandas as pd

# 가짜 데이터 생성
fake = Faker()
print(fake.name())

# 한글 데이터가 필요하다면
fake = Faker('ko-KR')
print(fake.name())

# 100건의 데이터 생성
test_data_list = [(fake.name(), fake.address(), fake.postcode(), fake.country(), fake.company(),fake.job(),
fake.phone_number(),fake.email(),fake.user_name(),fake.pyint(min_value=0, max_value=100),fake.ipv4_private(),fake.text(),
fake.color_name()) for i in range(100)]

# 데이터를 판다스에 넣어 보기 좋게 출력, 데이터를 보기위해서는 data viewer 활용
test_data_column_list = ['이름','주소','우편번호','국가명','직장명','직업','전화번호','이메일','사용자명','0-100','아이피','텍스트','색깔']
df = pd.DataFrame(test_data_list, columns=test_data_column_list,index=list(range(1,101))) # 인덱스는 없어도 된다 자동 1,2,3,..
print(df)

df.to_excel("c:\\work\\fake.xlsx")
