import os
import filecmp
import fileinput
import glob
import fnmatch

# 현재 실행 위치 담기
G_ExFilePos = os.getcwd() + '\\'
print(G_ExFilePos)

# 두 디렉토리 비교
print('=' * 50)
fd = filecmp.dircmp(G_ExFilePos+'IDT', G_ExFilePos + 'ODT')
for a in fd.left_only:
    print("a: %s" % a)

for b in fd.right_only:
    print("b: %s" % b)

for x in fd.diff_files:
    print("x: %s" % x)


# 특정 디렉토리에 특정 확장자를 가진 파일 한꺼번에 처리
# 모든 텍스트 파일을 읽어서 출력. *.py같은 것은 좀더 노력해봐야 하겠음
print('=' * 50)
with fileinput.input(glob.glob(G_ExFilePos + "ODT\*.txt")) as f:
    for line in f:
        print(line)


# 특정디렉토리에 해당되는 모든 파일 읽기
print('=' * 50)
for filename in glob.glob(G_ExFilePos + "**/*.*"):
    print(filename)


# 특정디렉토리에 해당되는 모든 파일 중 특정 조건에 맞는 파일만 출력
# 정규식을 써서 간단하게
print('=' * 50)
for filename in glob.glob(G_ExFilePos + "**/t???[0-9][0-9].*"):
    print(filename)