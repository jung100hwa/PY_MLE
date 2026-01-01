# pandas 정보보기를 확장한 패키지
# pandas.info 등은 게임자체가 되지 않을 정도의 상세한 분석을 해줌
# 현재는 오류가 발생하네.


import pandas as pd
from ydata_profiling import ProfileReport


data = pd.read_csv('./E_FILE/spam.csv',encoding='latin1')
profile = ProfileReport(
    data, title="test", explorative=True
)

profile.to_file('./E_FILE/PANDAS/spam.html')