import zlib
import gzip     # 파일을 압축 해제
import bz2      # 쓰레드 환경에서. 압축률이 상당히 좋다
import zipfile  # 파일을 합치고 해제하기
import os

######################################################################## 가장 단순한 방법
data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 1077 출력
print(compress_data)

org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data))
print(org_data)


########################################################################이 부분은 파일로 저장되니 파일 사이즈를 검사
data = "Life is too short, you need python." * 10000

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))

with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

# 처음 파일 사이즈와 동일한지 테스트 누락여부
assert data == read_data


########################################################################bz2 압축률이 상당히 좋다.
print('=' * 50)
data = "Life is too short, You need python." * 10000
compress_data = bz2.compress(data.encode(encoding='utf-8'))
print(len(compress_data))

org_data = bz2.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

assert data == org_data

# bz2로 gzip 동일하게 파일로 압축해서 저장할 수도 있다. 압축률이 무척 좋다.
data = "Life is too short, you need python." * 10000

with bz2.open('data.txt.bz2', 'wb') as f:
    f.write(data.encode('utf-8'))

with bz2.open('data.txt.bz2', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data


######################################################################## 파일합치기
print('=' * 50)

# 파일 합치기
# 파일을 압출 할 때 경로까지 압축해버리기 때문에 미리 경로를 이동한다음에 수행
os.chdir("c:\\work\\PY_MYD_G\\ODT\\")

with zipfile.ZipFile("mytext.zip", 'w') as myzip:
    myzip.write("test1.txt")
    myzip.write("test2.txt")
    myzip.write("test3.txt")

# 해제하기
with zipfile.ZipFile("mytext.zip") as myzip:
    myzip.extractall()