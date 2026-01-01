
# 라이브러리 불러오기
import seaborn as sns
from tabulate import tabulate

# ISNULL은 널이면 TRUE

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
print(tabulate(df.head(), headers='keys', tablefmt='simple_outline'))

# deck 열의 NaN 개수 계산하기
nan_deck = df['deck'].value_counts(dropna=False) 
print(nan_deck)

print(df.deck.value_counts(dropna=False))
print(df.deck.value_counts(dropna=True))

# isnull() 메서드로 누락 데이터 찾기
# isnull()은 널이면 True
print(df.head().isnull())

# notnull() 메서드로 누락 데이터 찾기
# notnull은 널이 아니면 True
print(df.head().notnull())

# isnull() 메서드로 누락 데이터 개수 구하기
# isnull 함수는 널이면 True ==1 이기 때문
print(df.head().isnull().sum(axis=0))