import re

# 특정문자단위로 끊어서 보여주기

text = "Regular expressions are powerful!!! "
print(re.findall(r'......', text))