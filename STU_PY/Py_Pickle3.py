# 규칙이 있는 데이터를 파일에 영구적으로 저장, 중복되는 번호는 없어야 함
# 클래스 자체가 저장이 가능함.

import pickle

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Student('jung100hwa', 27)

with open('student.p', 'wb') as f:
    pickle.dump(a, f)


with open('student.p', 'rb') as f:
    student = pickle.load(f)

print(student.name)