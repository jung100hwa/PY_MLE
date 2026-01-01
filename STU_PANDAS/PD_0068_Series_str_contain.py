import pandas as pd
import numpy as np
import re

s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
print(s1.str.contains('og', regex=False))

# regex 찾을려는 문자열이 정규식인지 그냥 문자열인지를 판단하는데 아래와 같이 그냥 문자열만 있으면 의미 없음
print(s1.str.contains('og', regex=True))

ind = pd.Index(['Mouse', 'dog', 'house and parrot', '23.0', np.NaN])
print(ind)
print(ind.str.contains('23', regex=False))

# 대소문자를 구분
print(s1.str.contains('oG', case=True, regex=True))

# 대소문자 구분없이
print(s1.str.contains('oG', case=False, regex=True))
print(s1.str.contains('oG', flags=re.IGNORECASE, regex=True))
print(s1.str.contains('PARROT', flags=re.IGNORECASE, regex=True))

# 널은 포함하지 않게 하기위해서는
print(s1.str.contains('og', na=False, regex=True))

# regex=True 옵션을 활용. 정규식으로, 이렇게 정규식을 할 때에는 반드시 붙여야 한다. 즉 'og | mo' 이러면 안된다.
print(s1.str.contains('og|mo', na=False, regex=True, flags=re.IGNORECASE))

# 숫자를 포함한 문자열 조회, '\d' 뒤에 정규식이라는 옵션이 있기 때문에 숫자로 인식
print(s1.str.contains('\d', regex=True))

# 정규표현식에서 .은 하나의 어떠한 문자를 의미한다. [] 안에서 .는 그대로 .의미
s2 = pd.Series(['40', '40.0', '41', '41.0', '35'])
print(s2.str.contains('.0', regex=True))

# startswith 함수는 특별한 문자로 시작하는 문자열 찾기
s = pd.Series(['bat', 'bbt', 'Bear', 'cat', 'ab.c', 'b.c', np.nan])
print(s.str.startswith('ba'))

# constains 정규식을 이용해도 됨
print(s.str.contains('^ba', regex=True))

# endswith 함수는 끝나는 문자열
print(s.str.endswith('bt'))

# contains 정규식을 이용하면
print(s.str.contains('bt$', regex=True))

########################################## 정규식을 활용
# 'b.' 이 포함된 문자열
print(s)
print(s.str.contains('b[.]', regex=True))

# b로 시작하고 다음에 .이 오는 문자열, 정규식에서 []안에는 문자 그 자체를 의미한다.
print(s.str.contains('^b[.]', regex=True))