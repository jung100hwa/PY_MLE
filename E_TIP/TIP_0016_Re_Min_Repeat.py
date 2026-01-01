import re

# 이것도 유용하게 쓰일 듯 최소한의 반복을 위함

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())  # <html~~~~title> 이러니까 다 나오는 구나
print(re.match('<.*?>', s).group()) # ?문자 앞에 점(.), + 등과 함께 쓰면 최소한의 반복을 수행