"""
함수안에 함수를 정의할 수 있나보네..
"""

def basef(str):
    def basef_in(str):
        return str+"_fun_in"

    result = str

    if str == "hgl":
        result = basef_in(str)
    return result

print(basef("hgl"))