# 말줄임
import textwrap
result = textwrap.shorten("Life is too short, you need python", width=15)
print(result)

# 한글도 동일하게 한글자가 1로 계산된다.
result = textwrap.shorten("인생은 짧으니 파이썬이 필요해", width=15)
print(result)

# 긴문장을 특정 바이트로 해서 줄바꿈 하는 것
long_text = 'Life is too short, you need python. ' * 10
print(long_text)


print('='*50)
result = textwrap.wrap(long_text, width=70)
for item in result:
    print(item)