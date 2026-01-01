"""
linespace 두 사이에 값에 균등하게 나눠눈다.
이걸 어디다 써도 쓰겠다.
"""

import numpy as np

# 0부터 1사이를 5개의 숫자로 나눈다.
aa = np.linspace(0, 1, 5)
print(aa)

# 다음은 숫자사이의 간격이 얼마인지 표시하고 싶다면
aa = np.linspace(0, 1, 5, retstep=True)
print(aa)
