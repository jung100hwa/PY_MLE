import re


# 긍정형은 ?=...
# 부정형은 ?!...

# 긍정형 전방탐색.
print("\n==========>전방탐색")
p = re.compile('.+:')
m = p.search('http://www.google.com')
print(m.group())

# 의미를 보면 엔진에서 소비되지 않는다는 외계어를 써놨는데 결국 찾을 때에는 적용되고 결과에는 제거된다라는 의미
print('\n===========>http:에서 : 만 제외하고 http만 출력')
p = re.compile(".+(?=:)")
m = p.search("http://www.google.com")
print(m.group())  # http만 출력

# 부정형 전방탐색(특정 파일 확장자 제외)
print("\n==========>부정형 탐색")
p = re.compile(r"(.*[.](?!bat$|exe$).*$)")
m = p.search("aaa.bat")
print(m)
m = p.search("aaa.bbbbat")
print(m)
m = p.search("aaa.batsss")
print(m)

m = p.search("bbb.exe")
print(m)

m = p.search("ccc.xlsx")
print(m)