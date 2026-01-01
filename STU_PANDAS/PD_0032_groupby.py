import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print('승객수 : ', len(df))
print(df.head())


##########################################  class를 기준으로 group by
#  그룹된 데이터프레임을 바로 출력은 불가능
print('=' * 50)
print('class 기준으로 그룹')
print(df.head())
group_df = df.groupby(['class'])
print(type(group_df))
print(group_df.first())     # 각 그룹에 첫번째 행을 출력


##########################################  각 그룹의 개수. 25.02.16
print(group_df.size().reset_index(name='count'))  # 이렇게 하니 데이터프레임
print(group_df.size())


##########################################  group 정보 출력(First, Second, Third로 그룹된 정보를 출력)
# group도 하나의 데이터프레임 정도로 이해하면 됨
for key, group in group_df:
    print('* key : ', key)
    print('* num : ', len(group))
    print('* member')
    print(group.head())
    ndf = group[['sex']]
    ndf2 = ndf['sex'].drop_duplicates()
    print(len(ndf2))



##########################################  그룹별로 한방에 그룹연산, 그룹연산이 가능한 열만 알아서 함
print('=' * 50)
print('그룹별 평균 구하기(연산이 가능한 열만 알아서 계산)')
average = group_df.mean(numeric_only=True)  # 버전이 바뀌어서 옵션을 반드시 적어줘야 하네.
print(average)


########################################## 아래 두 함수는 버전이 변경되어서 반드시 숫자컬럼을 지정해 줘야 함
# agg도 동일하게 연산이 가능한 것만 한다.
# print(group_df.agg(['mean'])) # 지금은 이렇게 하면 오류난다. 정확히 기재해야 한다.
print(group_df['age'].agg(['mean']))


# print(group_df.apply(np.mean)) # 비추천
print(group_df['age'].apply('mean'))


# 그룹이 아니면 아래처럼 하면 되지만 그룹일경우 loc라는 메소드가 존재하지 않음
# gdf2 = group_df.loc[:, ['age','fare','survived']]
# print(gdf2.apply('mean'))


##########################################  그룹중에 특정 그룹만 그룹연산이 가능하다. 이때는 시리즈 리턴
# 이것도 가능한게 하나의 그룹이 데이터 프레임으로 이해하면 됨
print('=' * 50)
print('특정 그룹만 평균 구하기')
thirdaverage = group_df.get_group('Third').mean(numeric_only=True)
print(thirdaverage)
print(type(group_df))


# 아래와 같이 하면 안된다. 데이터타입이 데이터프레임이 아니다. 그룹에는 loc속성이 존재하지 않는다.
# ndf = group_df.loc['Third']
# print(ndf.mean())


# ##########################################  그룹을 다중열로 하면 sql 쿼리와 동일
print('=' * 50)
print(df.head())
grouped = df.groupby(['class','sex'])
for key, group in grouped:
    print('* key : ', key)
    print('* num : ', len(group))
    print('*member')
    print(group.head())
    print('\n')

# ##########################################  다중열 평균 구하기
print('=' * 50)
print('다중열 그룹 평균 구하기')
average = grouped.mean(numeric_only=True)
print(average)


# 멀티 그룹일때 튜플로 지정해야 함, 앞으로 이런 형태로 적으면 안되겠네. df.mean => apply agg 이 형태로 사용해야 할 듯
print('=' * 50)
print('특정그룹 평균구하기')
group3f = grouped.get_group(('Third','female'))
print(group3f.mean(numeric_only=True))


# ##########################################  그룹별로 집계함수, 사용자 함수 정의 매핑
# agg, apply 버전이 바뀌어서 아래 예제를 보면서 한다.

print('=' * 50)
grouped = df.groupby(['class'])
print(grouped.mean(numeric_only=True))


# 사용자 정의 함수
def min_max(x):
    return x.max() - x.min()


# agg는 계산가능한 열만 알아서 수행했는데 이제는 명시해야 한다. 전체가 숫자면 명시하지 않아도 된다.
agg_minmax = grouped['age'].agg(min_max)
print(agg_minmax)


agg_minmax2 = grouped['age'].apply(min_max)
print(agg_minmax2)


# 아래와 같이 단일 함수에만 먹힌다. 원래는 먹히지 않는데 max, min 문자에도 먹히기 때문. 바보야
func = lambda g:g.max()
agg_minmax2 = grouped.apply(func)
print(agg_minmax2)


agg_minmax2 = grouped.apply('max')
print(agg_minmax2)


#  apply함수를 적용해도 된다. 시리즈로 계산해서 합치면 되지만 전체일 경우에는 그냥 agg 함수 사용
print('=' * 50)
print('apply함수를 적용한 통계함수 지정')
apply_minmax2 = grouped['age'].apply(min_max)
print(apply_minmax2)


# ############################################## apply실행되지 않는 이유
# todo 아래 내용은 과거 버전이다. 지금은 무조건 통계함수는 데이터타입이 가능한 것만 됨.
# apply는 모든 컬럼에 대해서 수행한다. 그러니 문자가 있는 sex 컬럼때문에 max-min 연산이 되지 않는다.
# agg는 문자 컬럼을 알아서 제외한다. 그런데 위에서 단일함수가 되는 것은 문자든 숫자든 min, max는 다 구할 수 있다.
# 제일 아래 부분에 좋은 예제가 있다.
# print('아래는 실행되지 않는다.')
# apply_minmax3 = grouped.apply(min_max)
# print(apply_minmax3)
#
# # agg는 실행된다.
# print(grouped.agg(min_max))


# 그룹이 아닐때
# 테스트. 아래의 예제를 보자 문자가 포함될때 apply, agg는 둘다 되지 않는다.
# 하나의 컬럼이 전체가 문자이면 agg는 알아서 제외하는 것 같은데 숫자와 문자가 하나의 컬럼에 섞여 있으면 안됨
# 여하튼 판다스는 뭘 하든 처음에는 클리닝 작업이 필수 이다.
# exam_data = {'수학' : [ 90, 80, 70, 'aa'], '영어' : [ 98, 89, 95, 'bb'],
#              '음악' : [ 85, 95, 100, 'cc'], '체육' : [ 100, 90, 100,'dd']}
# df = pd.DataFrame(exam_data, index=['a','b','c','d'])
# print(df)
#
# # 실패
# print(df.apply(min_max))
# print(df.apply('max'))
#
# # 실패
# print(df.agg(min_max))
# print(df.agg('max'))


# ###########################################  컬럼별 다른 함수 적용
#  그룹된 데이터프레이임에 일괄적으로 2개의 내장함수를 적용
# todo 중요한 것은 min, max는 문자도 가능하다.
print('=' * 50)
print('agg 함수를 이용한 통계함수 다중으로 지정')
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())


# todo 그룹된 데이터프레임에 컬럼마다 다른 함수를 적용. 정말 효과적인 것 같음.
print('=' * 50)
print('컬럼마다 다른 통계함수를 적용')
agg_all = grouped.agg({'fare':['min','max'], 'age': ['mean']})
print(agg_all.head())


#  그룹된 데이터프레임에서 조건에 맞는 것만 출력한다.
print('=' * 50)
for key, group in grouped:
    print('* key = ', key)
    print('* len = ', len(group))


# 그룹의 개수가 200이상인 것만 추출->first, third만 추출
# 컬럼별 개수를 구했다.
print('\n')
print(grouped.agg(len))


# 200개 이상인 그룹이 있는 참과 거짓으로 출력
print('\n')
print(grouped.agg(lambda x : len(x) > 200))


# 그룹의 요소별로 수행하여 데이터프레임그룹이 아닌 데이터프레임 타입으로 리턴
# 그럼 본 예제에서는 second 출력되지 않음
# todo 쉽게 얘기해서 그룹 개수로 조건을 걸고 세부 요소들을 출력함
print('그룹의 개수가 200이상인 것만 추출')
gfilter = grouped.filter(lambda x : len(x) >= 200)
print(gfilter.head())
print(type(gfilter))


# 먼저 그룹별 평균을 알아보고('First'만 30이상이다.)
testg = grouped['age'].agg('mean')
print(testg)
print(type(testg))

# 아래의 필터 함수는 쓸일이 있나 싶네.
# 30미만인 그룹의 멤버 전체를 출력해보면('First'가 나오면 안된다.)
# 조건은 그룹의 요소. 여기서는 first second third 계산하고 리턴은 그룹요소가 아닌 일반 데이터프레잉으로 리턴
# 그런데 filter를 쓸일이 있나????
gfilter5 = grouped.filter(lambda x : x.age.mean() < 30)
print(gfilter5)
print(type(gfilter5)) # 리턴은 일반데이터프레임 타입으로 리턴


#  그룹별로 apply적용하기, 그룹의 하나의 요소별로
print('\n')
print('apply 함수를 이용한 그룹별로 통계함수 지정')
gfilter6 = grouped.apply(lambda x : x.describe())
print(gfilter6)



print('\n')
print('agg 함수를 이용한 그룹별로 통계함수 지정')
agg_all = grouped.agg('describe')
print(agg_all.head())


# 아래는 안되네
# agg_all = grouped.agg(lambda x : x.describe())
# print(agg_all.head())

# ########################################### apply와 agg차이
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
# df = titanic.loc[:, ['age', 'fare', 'survived']]
print(df.head())

############################################# 1.그룹이 아닐때
# 둘다 통계 함수를 위한 타입이 맞는지 확인.
# todo 그런데 아래는 max, min 원래 되는데 컬럼명이 'class' 이기 때문 오류
# todo 두번째는 오류 이유는 그룹이 아닐경우 숫자형태만 가능
# print(df.apply('max'))
# print(df.agg('max'))


# 아래도 오류
df.columns=['age', 'sex', 'class_mod', 'fare', 'survived']
# print(df.apply('max'))
# print(df.agg('max'))


print(df.info())
df_m = df[['age', 'fare', 'survived']]
print(df_m.apply('max'))
print(df_m.agg('min'))

def testfunc1(a):
    return a.max()

print(df)
print(df_m.apply(testfunc1))  # 오류, 카테고리 컬럼이 없으면 정상
print(df_m.apply('max'))


print(df_m.agg(testfunc1))  # 오류, 카테고리 컬럼이 없으면 정상
print(df_m.agg('max'))


# testfunc2 = lambda x:x.max()
# print(df.apply(testfunc2))
# print(df.agg(testfunc2))

############################################# 2.그룹일때
# 단일함수 일때는 apply, agg 알아서 제외
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

gdf = df.groupby(['class'])

# todo 그룹일 때 min, max는 object, categori 타입이든 다 된다. 개떡같네.
print(gdf.apply('max'))
print(gdf.agg('max'))

# 아래는 통계함수는 반드시 숫자만 가능. 오류
# print(gdf.apply('mean'))
# print(gdf.agg('mean'))


def testfunc1(a):
    return a.max()

print(gdf.apply(testfunc1))
print(gdf.agg(testfunc1))

testfunc2 = lambda x:x.max()
print(gdf.apply(testfunc2))
print(gdf.agg(testfunc2))

# todo 아래 함수는 오류난다. 당연하다. max 또는 min 있으면 Object, categori 등 가능하지만
# todo 아래 최대값에서 최소값을 어떻게 빼냐. 등신아
def testfunc3(a):
    return a.max() - a.min()

# 당연 오류지
# print(gdf.apply(testfunc3))


# 아래와 같이 하면 되겠지
print(gdf[['age','fare']].apply(testfunc3))

# 아니면 아래 처럼
print(gdf.age.apply(testfunc3))

# 아래도 당연히 오류가 발생하지
print(gdf.agg(testfunc3))


exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 100], '평가' :['aa','bb','cc']}
df = pd.DataFrame(exam_data, index=['a','b','c'])
print(df)
print(df.dtypes)

df['평가'] = df['평가'].astype('category')
print(df.dtypes)

# 아래는 모두 실행 불가. 왜냐하면 그룹이 아니기 때문에 min, max는 숫자만 가능
# print(df.apply('max'))
# print(df.apply(testfunc1))
# print(df.apply(testfunc3))
#
# print(df.agg('max'))
# print(df.agg(testfunc1))
# print(df.agg(testfunc3))

############################################# 결론
# todo 1.그룹이 아닐때는 무조건 숫자 컬럼만 인식(min, max). 다른 함수(mean 등)는 말할 것도 없고
# todo 2.그룹일 경우 희한하게 숫자가 아닌 컬럼도 된다(min, max 만), 다른 함수는 무조건 숫자 컬럼만
# todo apply, agg 든 가능하면 숫자 컬럼만 사용한다.
# todo 그리고 가능하면 agg를 사용하자.