import pickle

# 파일에 객체의 형식 그대로 넣었다가 그래로 읽을 수 있음. 바이너리 형태로 쓰기
# 대용량일 경우 가능 할런지는 확실하지 않음

f = open("c:\\work\\test.txt", "wb")
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()

f = open("c:\\work\\test.txt", "rb")
data = pickle.load(f)
print(data)
f.close()