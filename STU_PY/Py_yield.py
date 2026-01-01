"""_summary_
결과를 한번에 리턴하지 않고 그때그때 리턴 함
"""

def return_abc():
    return list('abc')

print(return_abc())

def yield_abc():
    yield 'a'
    yield 'b'
    yield 'c'
    
for item in yield_abc():
    print(item)
    

import time

def return_abc1():
    alist = []
    for ch in "abc":
        time.sleep(1)
        alist.append(ch)
    return alist


# 3초 경과후에 결과를 하나씩 리턴
for ch in return_abc1():
    print(ch)
    

# 1초마다 하나씩 리턴
def yield_abc1():
    for ch in "abc":
        time.sleep(1)
        yield ch
        
for ch in yield_abc1():
    print(ch)
    

############################# yield from
print("------------->")
def yield_abc2():
    for ch in ['a','b','c']:
        yield ch

for item in yield_abc2():
    print(item)
    
# 한번에 리스트로부터
print("------------->")
def yield_abc3():
    yield from ['a','b','c']
    
for ch in yield_abc3():
    print(ch)
    
