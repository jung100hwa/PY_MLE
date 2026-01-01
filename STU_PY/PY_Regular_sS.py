import re

# '\s'는 공백문자, '\S'는 공백문자가 아닌 것

# 아래에서 class만 출력됨. 뒤에 as는 출력되지 않음. 왜냐하면 앞뒤 공백을 이미 class에서 사용했기 때문 !!!아주 중요
p = re.compile('\s[a-zA-Z]+\s')
m = p.findall('no class as all')
print(m)

# 아래는 class, as 가 출력 됨. as 공백을 하나 더 넣었기 때문 !!!아주중요
p = re.compile('\s[a-zA-Z]+\s')
m = p.findall('no class  as all')
print(m)


# 아래에서 all이 출력되는 이유는 앞에 공백이 있지만 at에서 이미 읽었기 때문에 all은 앞에 공백이 적용되지 않는다.
# 헛갈리수 있으니 하나의 단어씩 적용해 보면 답이 나온다. noclasstwo가 나오는 이유는 t->w일때 다음 o가 공백이 아니기 때문
# 이후에 o-> 공백이기때문에 o까지만 읽는다.
p = re.compile('\S[a-zA-Z]+\S')
m = p.findall('noclasstwo at all')
print(m)