"""
(1) import는 클래스를 불러오는 것이 아니고 .py를 불러온다. 이 파일 안에 여러개의 클래스가 존재할 수 있다.
(2) 클래스 변수(스태틱 변수)는 클래스 함수, 스태틱 함수에서 접근 해야 함. 물론 객체에서도 접근 가능 함(문법 경고 남)
(3) 클래스 함수와 스태틱 함수는 클래스명과 객체로 접근 가능
"""


class Cparent:

    # 클래스 속성. 클래스명으로 접근해야 함.(=스택틱변수와 같은말)
    classint = 0  # 클래스 변수로써 생성된 객체의 수를 파악
    classList = []
    __classMeber = "비공개 클래스 변수"

    common_mem = "여기는 부모 클래스"  # 클래스함수와 스태틱 함수의 차이를 위해 정의

    # 생성자 함수. 이게 init 함수를 호출한다. 파라미터 개수가 init과 맞아야 한다.
    def __new__(cls, name):
        print("Cparent.__new__")
        return super().__new__(cls)

    # 클래스 인스턴스 속성은 가급적 init 생성자에 정의하하자
    def __init__(self, name):
        print("parrent__new__가 __init__함수를 자동 호출")
        self.name = name
        self.__classSecrit = "비공개 인스턴스 변수"  # 비공개 속성으로 외부에서 접근 불가. 함수를 통해서만 접근
        Cparent.classint += 1
        Cparent.classList.append(self.name)

    def print(self):
        print("Cparent class")
        print(self.name)

    def parent_func(self):
        print(self.name)

    def secrit_func(self):
        print(self.__classSecrit)

    # 상속관계에 공통으로 있는 함수
    def common_func(self):
        print(self.name)

    @classmethod
    def classPanent_fun(cls):
        print(cls.classList)

    @classmethod
    def classPanent_fun_01(cls):
        print(cls.__classMeber)

    @classmethod
    def classPanent_fun_02(cls):
        print(cls.classint)

    @staticmethod
    def classPanent_fun_03():
        print(Cparent.classint)

    # 인스턴스 함수는 인스턴스 변수만 핸들링 하는 것을 원칙으로 하자. 아니면 아래와 같이 경고
    def classint_func(self):
        print(Cparent.classint)

    @classmethod
    def classPanent_fun_04(cls):
        print(cls.common_mem)

    @staticmethod
    def classPanent_fun_05():
        print(Cparent.common_mem)


class Cson(Cparent):

    common_mem = "여기는 자식 클래스"  # 클래스함수와 스태틱 함수의 차이를 위해 정의

    def __new__(cls, name):
        print("Cson.__new__")
        return super().__new__(cls, name)

    def __init__(self, name):
        print("son__new__가 __init__함수를 자동 호출")
        super().__init__(name)  # 부모클래스 생성자 호출
        self.__classSecrit = "this is son class"  # 비공개 속성으로 외부에서 접근 불가. 함수를 통해서만 접근
        self.name = name

    def print(self):
        print("Cson class")
        print(self.name)

    def secrit_func(self):
        print(self.__classSecrit)

    # 부모 클래스에 있는 동일 함수를 먼저 부르고 자신을 부름
    def common_func(self):
        super().common_func()
        print(self.name)


if __name__ == "__main__":

    objP = Cparent("class parent")
    objP.print()

    print()

    objS = Cson("class child")
    objS.print()

    print()

    # 클래스 멤버 호출. 여기서는 자식으로 인해 한번 더 호출됨
    Cparent.classPanent_fun()

    # # 자식객체에서 부모 함수 호출
    # objP.parent_func()
    # objS.parent_func()

    # # 비공개 속성 호출
    # objP.secrit_func()
    # objS.secrit_func()

    # # 비공개 클래스 변수 호출
    # Cparent.classPanent_fun_01()

    # # 부모 함수를 먼저 부르고 자신의 함수 내용을 출력
    # # 자식에서 불렀기 때문에 부모 클래스의 이름도 자식 클래스 이름으로 출력된다.
    # objS.common_func()

    # # 다시한번 클래스 변수를 불러보자
    # print("\nclass변수 호출")
    # Cparent.classPanent_fun_02()

    # # 스태택 함수에서 스태틱 변수
    # print("\nclass변수를 스태틱 함수에서 호출")
    # objS.classPanent_fun_03()
    # objP.classPanent_fun_03()

    # print("\n스태틱 함수를 클래스로 접근")
    # Cparent.classPanent_fun_03()

    # print("\n클래스 함수를 객체로 접근")
    # Cparent.classPanent_fun_02()

    # # 객체를 임시로 생성해 봄
    # aaa = Cparent("class parent")

    # print("\n일반함수에서 클래스 멤버 호출")
    # objP.classint_func()

    # """
    # (1) 부모와 자식 객체에 클래스 변수 정의
    # (2) 부모 클래스에 클래스 변수 호출 함수 정의
    # (3) 자식객체를 생성
    # (4) 부모와 자식객체에 둘다 존재하는 클래스 변수(스태틱 변수) 중 어떤 것이 존재하는지 확인
    # """
    # print("\n클래스 함수와 스태틱 함수 차이")
    # objS.classPanent_fun_04()   # 클래스 함수는 자식 객체의 속성을 유지
    # objS.classPanent_fun_05()   # 스태틱 함수는 속성을 유지 하지 않음
