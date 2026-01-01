from io import StringIO
import pandas as pd

# 이렇게도 가능하네. 거의 쓸일이 없겠다.

txt = '''series NAME VAL1 VAL2 
0 AAA 27 678 
1 BBB 45 744
2 CCC 34 275
3 AAA 29 932
4 CCC 47 288
5 BBB 24 971
'''

# StringIO는 문자열을 파일처럼 변경
df = pd.read_table(StringIO(txt),sep = '\s+')
print(df)


# 이걸또 이렇게도 하네. 나참. 이렇게 복잡하게 할 필요가 있나.
print(df.groupby('NAME')[['VAL1','VAL2']].apply(lambda x : x.max() - x.min()))