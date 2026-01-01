import pandas as pd

# 리스트 처럼 슬라이싱 하기. slice
# 정의된 문자열의 정의한 인덱스 범위를 정의된 문자열 치환
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie']
                      , 'age': [24, 42, 35]
                      , 'state': ['NY', 'CA', 'LA']
                      , 'point': [64, 92, 75]})

print(df)

# stop를 주면 첫번째 글자만 선택하겠다는 의미
print(df['age'].astype(str).str.slice(stop=1))


# 세대를 구하는 간단한 공식(아주 유용한 공식)
# 먼저 스트링 타입으로 바꾸고, 첫번째 부터 끝까지를 "0 대"로 치환
print(df['age'].astype(str).str.slice_replace(start=1, repl='0 대'))

# replace는 특정문자열
st = "hello world"
print(st.replace("he",'HE'))


# 바꿀 문자가 많다면 translate, 문자하나 바꿈. 즉 1:1 대응이 되어야 함
# 먼저 변환테이블을 만든 다음에 적용
stable = st.maketrans('hw','HW')
print(st.translate(stable))
