alist = [1,2,3,4,5,6,7,8]
print(min(alist))
print(max(alist))

alist = [1,2,3]
alist2 = [4,5,6]
print(min(alist,alist2))

####################################이게 중요하다.
# key 값을 기준으로 min값을 구한다.
d = {'one':1, 'two':2, 'three':3}
print(min(d, key=d.get))

arr = [(0,10),(1,14),(2,2),(3,24)]
print(min(arr, key=lambda x:x[1]))

# key 값을 기준으로 max값을 구한다.
d = {'one':1, 'two':2, 'three':3}
print(max(d, key=d.get))


arr = [(0,10),(1,14),(2,2),(3,24)]
print(max(arr, key=lambda x:x[1]))