from datetime import datetime, timedelta

print('='*50)
print('\n\n현재시간')
now = datetime.now()
print(now)

print('\n\n날짜지정')
before = datetime(2020,3,22,23,10,12)
print(before)

print('='*50)
print('\n\n두날짜간의 차이')
print(now-before)
print((now-before).days,'일')
print((now-before).seconds/3600,'시간')
print((now-before).seconds/60,'분')
print((now-before).seconds,'초')

print('='*50)
print('\n\n현재 시간부터 5일 뒤')
print(now + timedelta(days=5))

print('\n\n현재 시간부터 3일 전')
print(now + timedelta(days=-3))

print('\n\n현재 시간부터 1일 뒤의 2시간 전')
print(now + timedelta(days=1, hours=-2))

print('\n\n현재 시간부터 1일 뒤의 2시간 30분 10초 뒤')
print(now + timedelta(days=1, hours=2,minutes=30, seconds=10))


print('='*50)
print('\n\n형식에 맞게 출력')
now = datetime.now()
print(now.strftime('%y-%m-%d'))
print(now.strftime('%Y-%m-%d'))

print('='*50)
print(datetime.now().today())
print(datetime.now())

print('='*50)
# startday = datetime(2021, 1, 1).strftime('%Y%m%d')
startday = datetime(2021, 1, 1)
print(startday)

strendday   = datetime.now().strftime('%Y%m%d') + '0000'
print(strendday)

beforeday = startday
afterday  = startday + timedelta(weeks=1)

strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
strafterday  = afterday.strftime('%Y%m%d')  + '0000'


while strbeforeday <= strendday:
    print(strbeforeday + "~" + strafterday)
    beforeday    = beforeday + timedelta(weeks=1)
    afterday     = afterday + timedelta(weeks=1)
    strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
    strafterday  = afterday.strftime('%Y%m%d') + '0000'
