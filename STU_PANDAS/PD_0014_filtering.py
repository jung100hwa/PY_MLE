# 조건을 주어서 원하는 데이터만 불러오는 것
# 아마도 판다스에서 가장 많이 사용하지 않을 까 생각됨
# isin 같은 함수보다는 mask를 사용해야 함. 더 많은 조건을 줄 수 있으니까
# todo query 가장 많이 사용할 것 같기는 하다. 단지 차이는 query "and", "or" mask는 &, |

from tabulate import tabulate
import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
print(type(df))
print(df.head(10))

# 행의 조건에 해당되는 것만 추출, loc에 마스크 할당
print('\n===============================')
mask1 = (df.age >= 10) & (df.age < 20)
df_teen = df.loc[mask1]
print(tabulate(df_teen.head(), headers='keys', tablefmt='simple_outline'))


# query and or , mask & | 차이
strQ = "(age >= 10) and (age <=20)"
df_teen = df.query(strQ)
print(tabulate(df_teen.head(), headers='keys', tablefmt='simple_outline'))


mask2 = (df.age < 10) & (df.sex == 'female')
df_teen = df.loc[mask2, : ]
print(tabulate(df_teen.head(), headers='keys', tablefmt='simple_outline'))


# 마스크끼리 조합.
mask3 = mask1 | mask2
df_teen = df.loc[mask3, : ]
print(tabulate(df_teen, headers='keys', tablefmt='simple_outline'))


print('\n===============================')
print(df.head())


mask1 = df['sibsp'] == 3
mask2 = df['sibsp'] == 4
mask3 = df['sibsp'] == 5

# 이렇게 해도 된다.
# mask1 = df.sibsp == 3
# mask2 = df.sibsp == 4
# mask3 = df.sibsp == 5

mask = mask1 | mask2 | mask3
ndf = df.loc[mask, :]
print(tabulate(ndf, headers='keys', tablefmt='simple_outline'))


# isin() 함수를 이용해서 간단하게 추출, 이 함수는 조건에 맞으면 true, 거짓이면 false를 리턴한다.
print('\n===============================')
print(df)


isin_filter = df['sibsp'].isin([3, 4, 5]) # 조건에 해당되는 행들만 시리즈 타입으로 반환
print(type(isin_filter))
print(isin_filter)  # 행마다 true, false


# todo !!(아주중요) 여기를 잘보면 df가 어떻게 동작하는지 알 수가 있음. 즉 한행씩 읽어내는데 참일때만 읽어 낸다
dfis = df[isin_filter]
print(tabulate(dfis, headers='keys', tablefmt='simple_outline'))


adic = {'a':[1, 2, 3], 'b':[11, 22, 33], 'c':[111, 222, 333]}
ndf = pd.DataFrame(adic)
print(ndf)


fs = ndf['a'].isin([1]) | ndf['b'].isin([22])
print(type(fs))
print(fs)


# 이렇게 컬럼명을 할 수도 있지만 대부분 컬럼 즉 시리즈에 관한 함수를 쓸때는 df[] 형태로 가자
# 일단 컬럼이 문자일때만 아래와 같이 가능함. 굳이 이유가 아니라도 저렇게 쓰지 말자. 컬럼을 숫자로 하는 띨빵이는 없겠지
# fs = ndf.a.isin([1]) | ndf.b.isin([22])
nfs = ndf[fs]
print(nfs)