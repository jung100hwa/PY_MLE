import pandas as pd

# # read_csv() 함수로 df 생성
# df = pd.read_csv('./auto-mpg.csv', header=None)
#
# # 열 이름을 지정
# df.columns = ['mpg','cylinders','displacement','horsepower','weight',
#               'acceleration','model year','origin','name']

# method = 'pearson', 'spearman', 'kendall'이것들 중의 하나
# +1은 양의 상관관계,-1은 음의 상관관계. 여하튼 +, - 이면 관계가 있다는 것이다.
# 0이면 관계가 없다는 것이다. 관계파악에서 필요할 듯
# ndf = df.corr(method='pearson')


# 위에 예제를 실행할려면 정제부터 아래 예제로 하는 게 나을 듯


col1 = [1,2,3,4,5,6]
col2 = [1,4,2,8,16,32]
col3 = [6,5,4,3,2,1]
data = {"col1":col1,"col2":col2,"col3":col3}
df = pd.DataFrame(data)
ndf = df.corr(method='pearson')
print(ndf)
