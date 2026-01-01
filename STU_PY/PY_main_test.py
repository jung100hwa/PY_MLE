# if __name__='__main__' 문구 테스트
# __main__는 파이썬 콘솔에서 실행하는 첫번째 모듈의 이름이다.
# 만약에 임포트 모듈이 a, b, c가 있고 d 에서 이들을 임포트해서 실행한다면 d모듈의 이름은(__name__) __main__이 되고
# a, b, c 모듈의 이름은 __name__==a, __name__= b, __name__== c 가 된다.
# 만약에 c만 단독으로 실행한다면(d 를 실행하면 어쩔수 없이 a, b까지 다 임포트해야 하기 때문에. 임포트한다는 것은 a,b 모듈을 실행한다는 것과 동일) c의 __name__이름은 __main__인 된다. 
# https://brunch.co.kr/@growthminder/132

import PY_main_test_01 as pt

# PY_main_test_01에 if __name__ == "__main__"에 없는 코드가 먼저 실행된다.

if __name__ == "__main__":
    print("PY_main_test_01 test...")
    print(pt.plus_fun(9,8))