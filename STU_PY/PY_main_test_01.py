def plus_fun(a, b):
    return a+b

# 아래 코드는 다른 모듈에서 현재 이 모듈을 임포트하는 곳마다 실행된다.
# 이렇게 하면 안된다. 
print(plus_fun(8,2))

# 아래 코드는 단독으로 실행할 때만 실행된다.
if __name__ == "__main__":
    print(plus_fun(1,2))