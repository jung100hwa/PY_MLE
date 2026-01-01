import time

#  이것은 c언어 time.h를 그대로 사용
current = time.time()
print(current)

timeinfo = time.localtime(current)
print( timeinfo.tm_year, timeinfo.tm_mon, timeinfo.tm_mday)

print(time.asctime(time.localtime(current)))


#  항상 현재 시간만을 리턴
print(time.ctime())

# 다양한 포맷으로 출력
print(time.strftime('%c',time.localtime(time.time())))



from datetime import date
import datetime

sss = date.today()

print(date.today())
print(date.today() + datetime.timedelta(days=-1))

def data_collect(x):
    sss= date.today() + datetime.timedelta(days=-x)
    sss = sss.strftime('%Y-%m-%d')
    return sss

# 날짜가 안되네.
alist = list(map(data_collect, range(1,4)))

for item in alist:
    print(item)

aa = '2025-10-14'
print(alist.count(aa))

print(alist)