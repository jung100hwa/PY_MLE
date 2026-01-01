"""
2개의 값이 허용 오차안에 있는지를 검사
비율의 합이 0이 되는지를 검사하는데 사용했는데 보통 비율은 0~1 사이임으로 딱 1로 떨어지지 않는다. 그래서 사용하는 듯
"""

import numpy as np

a = [0.95, 0.05, 0.02]

if not np.isclose(sum(a), 1.0, atol=0.01):
    raise ValueError(f"비율의 합이 1이 되어야 합니다. 현재 합: {sum(ratios)}")
else:
    print('ok')