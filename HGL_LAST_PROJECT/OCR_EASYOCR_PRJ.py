# 아래 코드를 먼저 수행한 다음에 하자.
# 뭔가 충돌이라고 하는데 인터넷 찾아보면 안다.
# https://2-54.tistory.com/59
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'



import easyocr
import pandas as pd
import re


reader = easyocr.Reader(['ko','en'])
result = reader.readtext('lastsample/ocr_test01.jpg')
# result = reader.readtext('lastsample/ocr_test01.jpg', detail=0) #좌표가 나오지 않고 글씨만 나옴

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
nm = []

# 아래와 같이 데이터프레임으로 바꿔서 출력해보면 답이 나온다.
# 좌표는 위에서부터 순차적으로 내려오기 때문에...뭔말인지 알지지
for detection in result:
    x1.append(detection[0][0][0])
    y1.append(detection[0][0][1])
    x2.append(detection[0][1][0])
    y2.append(detection[0][1][1])
    x3.append(detection[0][2][0])
    y3.append(detection[0][2][1])
    x4.append(detection[0][3][0])
    y4.append(detection[0][3][1])

    nm.append(detection[1])

df = pd.DataFrame({"x1":x1, "y1":y1,"x2":x2, "y2":y2,"x3":x3, "y3":y3,"x4":x4, "y4":y4,"nm":nm})
print(df)


# 핵심적인 내용만 추출해 본다.
# 사업자등록번호
for row1 in df.index:
    if str(df.loc[row1,'nm']).replace(' ','') == "등록번호":
        
        # 사업자등록번호가 한줄에 있다는 가정하에
        for row2 in df.index:
            strnm = str(df.loc[row2,'nm']).replace(' ','')
            p = re.compile(r'[\d]{3}[-][\d]{2}[-][\d]{5}')
            if p.search(strnm):
                print(p.search(strnm).group())
                break
                
