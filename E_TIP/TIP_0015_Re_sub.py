import  re

# sub 메소드의 참조를 이용하여 이름과 전화번호의 순서를 바꿈
strList = ["park1 010-1234-5678", "park2 010-1234-5678", "park3 010-1234-5678"]

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
for str in strList:
    print(p.sub(r'\g<phone> \g<name>', str))
    
    
    
# 예제는 정규화를 써서 ++이상을 바꿔버리는 것
text = "사과+딸기+수박+메론+++++포토"
str = r'\++'
text = re.sub(str,'-',text)
print(text)