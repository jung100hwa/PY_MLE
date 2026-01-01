import os
import glob


# 지정한 디렉토리내의 조건에 맞는 파일과 폴더를 리스트로 돌려준다.
# 중요한 것은 패턴에 맞는 파일과 폴더를 리스트로 돌려준다.
# 예를 들어 *.* 이렇게 하면 확장자가 있는 파일만 돌려주는 것이 아니라 폴더명에 "."들어가 있는 폴더명도 돌려준다는 것 !!!!

# 지정한 디렉토리의 모든 폴더와 파일명을 돌려준다. 하부까지는 하지 않는다. 지정한 디렉토리내에서만 수행
output = glob.glob("c:\\work\\*")
for item in output:
    print(item)


# *.* 이렇게 하면 파일명과 폴더명에 "."이 포함된 결과를 돌려준다.
print ("*" * 50)
output = glob.glob("c:\\work\\*.*")
for item in output:
    print(item)


# *.* 이렇게 하면 파일명과 폴더명에 "."이 포함된 결과를 돌려준다.
# 전체경로가 아닌 파일명만 추출. 이 함수는 폴더 든 아니면 파일이든 경로의 제일 마지막 부분을 파일로 인식
# 즉 basename 이함수는 폴더명도 파일로 인식해버림. splitext함수로 파일명 다시 검색
# 이렇게 해도 폴더명에 "." 있으면 파일로 인식
print ("*" * 50)
output = glob.glob("c:\\work\\*")
for item in output:
  filename = os.path.basename(item)
  filename, ext = os.path.splitext(filename)
  if len(ext):
      print(filename)


# 파일과 폴더 분리. !!!!!!!!!!!!! 이렇게 하자
# 폴더명에가 "." 경우도 폴더로 인식
print ("*" * 50)
output = glob.glob("c:\\work\\*")
for item in output:
  if os.path.isfile(item):
      filename = os.path.basename(item)
      print(filename)


#  특정파일만 검색
print('=' * 50)
output = glob.glob("c:\\work\\*.zip")
for item in output:
    print(item)


print('=' * 50)
output = glob.glob("c:\\work\\test?.py")
print(output)


#  자리수와 매핑하기
print('=' * 50)
output = glob.glob("c:\\work\\?????.*")
print(output)