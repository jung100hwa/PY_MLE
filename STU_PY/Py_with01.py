class Hello:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 필수정의 요소
    def __enter__(self):
        return self

    def sum(self):
        print(self.first + self.second)

    # 필수정의 요소
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


if __name__ == '__main__':
    with Hello(1,2) as h:
        h.sum()