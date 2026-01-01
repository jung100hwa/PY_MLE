import re

# \w 문자와 숫자를 의미 함, 그리고 todo "_"를 포함한다. 아주 중요!!

text = "A1 B2 c3 d_4 e:5 ffGG77--__-- "
print(re.findall('\w', text))

# \w는 "_"를 포함한다.
text = "a_b-c"
print(re.findall('\w', text))

# \W는 정반대의 의미, 즉 문자, 숫자, _ 이 아닌 것
text = "AS _34:AS11.23  @#$ %12^*"
print(re.findall('\W', text))