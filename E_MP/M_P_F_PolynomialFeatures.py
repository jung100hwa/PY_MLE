import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

x = np.arange(6).reshape(3,2)
print(x)

# df = pd.DataFrame(x)
# print(df)

# PolynomialFeatures 함수는 다항식에 맞게 하나의 숫자를 다항식 개수만큼 변경시킨다.
# x→[1,x,x2,x3,⋯]
# PolynomialFeatures은 "입력값 x를 다항식으로 변환한다."
#
# x→[1,x,x2,x3,⋯]
# 만약 열의 갯수가 두 개이고 2차 다항식으로 변환하는 경우에는 다음처럼 변환한다.
#
# [x1,x2]→[1, x1, x2, x1**2, x2**2, x1x2]
#
# 다음과 같은 입력 인수를 가진다.
#
# degree : 차수
# interaction_only: True면 제곱은 빼고, 서로x끼리 상호작용하는만큼 (x1x2, x2x3 --- )
# include_bias : 상수항 생성 여부


poly = PolynomialFeatures(2)
x = poly.fit_transform(x)
print(x)