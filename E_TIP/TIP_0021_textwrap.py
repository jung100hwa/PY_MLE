# 문자열을 일정한 부분만 표시하고자 할때
# 주로 데이터베이스에서 불러와서 앞부분 보여주고 싶을 때 쓰면 괜찮겠네.
# 긴문장을 정해진 길이로 줄바꿈 할 때

import textwrap

sss = "주로 데이터베이스에서 불러와서 앞부분 보여주고 싶을 때 쓰면 괜찮겠네."
sss = textwrap.shorten(sss, width=15, placeholder="...")
print(sss)

sss = 'Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python.'
sss = textwrap.wrap(sss, width=75) # list 형태로 리턴
for item in sss:
    print(item)

print("====================>")
sss = '\n'.join(sss)
print(sss)