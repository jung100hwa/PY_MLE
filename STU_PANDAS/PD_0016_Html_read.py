import pandas as pd
from tabulate import tabulate

# 웹페이지의 테이블 개수를 가져온다. 웹크롤링할 때 적용해볼만 하다.
url = "https://kreach.me.go.kr/repwrt/portal/notifyList.do?BOARD_NO=&BOARD_DVSN=1&searchCondition=&search02Yn=&search06Yn=&search03Yn=&search10Yn=&search13Yn="
tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(0,len(tables)):
	print(tables[i])


url = "https://kreach.me.go.kr/repwrt/portal/notifyList.do"
tables = pd.read_html(url)
print(type(tables))
# print(tables)

print(len(tables))
# 행이 하나다
for i in range(0,len(tables)):
	print(tables[i])

print(tabulate(tables, headers='keys', tablefmt='simple_outline'))


table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(type(table))
# print(table)
for i in range(0,len(table)):
	print(table[i])

print(tabulate(table, headers='keys', tablefmt='simple_outline'))