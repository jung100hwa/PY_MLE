import zipfile
import os

# 파일을 압출 할 때 경로까지 압축해버리기 때문에 미리 경로를 이동한다음에 수행
print(os.getcwd())
os.chdir("c:\\temp\\")

zipfile.ZipFile("허길양.zip").extractall("c:\\temp\\aa\\")
print(os.getcwd())
