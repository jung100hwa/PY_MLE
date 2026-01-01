# *args
# 함수를 만들 때 인자의 개수를 정확히 지정하지 못할때 사용
# 굳이 리스트라던지 이런걸 사용하면 되지. 사용할 일이 있나 모르겠네

# **kwargs는 키와 밸루 형태이다. 이것도 그냥 딕셔너리 쓰면 되지 굳이.

# 함수(일반파라미터, *args, **kwargs) 인자는 항상 이순서로 해야 함.


def getname(*args):
    print(args)                 # 인자 자체는 튜플형태로 된다.
    for item in args:
        print(item)
        
# *args는 항상 뒤에 적는다.
def getname2(name, *args):
    for item in args:
        print(name + "->" + item)
        

def getname3(**kwargs):
    print(kwargs)
    
    for key, value in kwargs.items():
        print("{0} is {1}".format(key, value))

# args 사용
getname('a1','a2')
getname2('hgl', 'b1', 'b2')


#kwargs 사용
getname3(a='k1', b='k2', c='k3')