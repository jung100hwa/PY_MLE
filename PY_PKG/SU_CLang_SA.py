# 폴터 모니터링 테스트
import ctypes

# c언어로 작성된 모듈을 불어옴
# 모듈안에 포함된 함수를 사용
# 리눅스에서 테스트해야 함. so는 유닉스에서 사용함

c_code_add = ctypes.cdll.LoadLibrary("TES/SU_CLANG_MO.so")
c_code_fun = c_code_add.add_int
print(c_code_fun(11, 22))

