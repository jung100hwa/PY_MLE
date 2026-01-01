import shutil
import os


#  파일 복사
print('파일 복사')
shutil.copy('../test/test.py', '../test/test2.py')

#  디렉토리 전체를 삭제
print('폴더 전체를 삭제')
if os.path.isdir('../test2'):
    print('디렉토리가 존재하여 일단 삭제 함')
    shutil.rmtree('../test2')

print('test 경로 아래 파일명')
aList = os.listdir('../test')
print(aList)

# 폴더 전제를 복사
print('폴더전체를 복사')
shutil.copytree('../test', '../test2')