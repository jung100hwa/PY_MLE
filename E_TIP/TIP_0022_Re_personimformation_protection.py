import re

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

# 먼저 일반적인 방법을 한번 써보자
mod_data = []
for text in data.split('\n'):
    word_data = []
    for text_item in text.split(" "):    
        if len(text_item)==14 and text_item[:6].isdigit() and text_item[7:].isdigit():
            text_item = text_item.replace(text_item[7:],"*" * 7)
        word_data.append(text_item)
    mod_data.append(" ".join(word_data))

for item in mod_data:
    print(item)
                        
print("=" * 50)

# re 모듈을 이용해서 간단히
m = re.compile(r"(\d{6})[-]\d{7}")
data = m.sub("\g<1>-*******",data)
print(data)