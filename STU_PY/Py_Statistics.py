import statistics

# 주로 평균을 구할 때 사용, 평균도 종류가 많다.
# 판다스를 활용하는게 낫다.

marks = [78, 93, 99, 95, 51, 71, 52, 43, 81, 78]
print(statistics.mean(marks))       # 평균
print(statistics.median(marks))     # 중간값