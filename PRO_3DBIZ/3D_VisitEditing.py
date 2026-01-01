"""
1. 대충 어느 정도의 사용자가 필요한지 협회에 문의
2. 데이터에서 언제부터가 원하는 데이터가 나오는지 기간을 설정
3. 개발서버(또는 운영서버)에서 기간에 맞게, 건수에 맞게 불러온다.
"""

from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
from holidayskr import is_holiday
import numpy as np
import random
import re
from typing import List, Tuple


conn = None

# 평일과 주말 비율을 임의로 정하자. 주말로 일하는 사람들이 있다.
WROK_RATIO = [0.97, 0.03]


# 실제 구하고자 하는 방문자수 날짜
START_DAY = datetime(2025, 6, 1)
END_DAY = datetime(2025, 12, 18)


# 샘플데이터를 구하기 위한 날짜. 이 날짜는 DB에서 쿼리로서 기간을 대략 산정한다.
SAMPLE_SDAY = "2024-04-01"
SAMPLE_EDAY = "2024-12-31"


########################################################################################## 데이터베이스 연결
# 여기는 현재 개발서버이다.
def maria_db_conn():
    global conn
    try:
        db_url = "mysql+pymysql://root:3dbankdb1218@175.126.176.174:3307/3dbank_v1"
        engine = create_engine(db_url)
        conn = engine.connect()
        print("DBConnection is success!!")
    except:
        print("DBConnection is not availableon this machine")
        exit()


################################################################ 대략산정한 데이터를 평일과 주말 비율로 분리한다.
def split_dataframe_by_ratios(startDate, endDate):
    """
    strDate: 대략 산정한 기간 중 시작일
    endDate: 대략 산정한 기간 중 종료일
    :rtype: tuple[평일리스트, 주말리스트]
    """

    ratios = WROK_RATIO  # 평일과 주말 비율
    shuffle = True       # 데이터를 섞는다.
    random_state = 42    # 매번 동일하게 결과를 얻기 위해서. None 함수를 돌릴때 마다 달라진다.

    query = f"select * from visit where VISIT_DT between '{startDate} 00:00:00.000' and '{endDate} 23:59:59.999'"
    df = pd.read_sql_query(query, conn)

    # 비율의 합이 1인지 확인
    if not np.isclose(sum(ratios), 1.0, atol=0.01):
        raise ValueError(f"비율의 합이 1이 되어야 합니다. 현재 합: {sum(ratios)}")

    # 데이터를 무작위로 섞는다.
    if shuffle:
        df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)

    splits = []
    start_idx = 0
    total_len = len(df)

    for i, ratio in enumerate(ratios):
        # 마지막 부분인 경우 남은 모든 데이터를 포함
        if i == len(ratios) - 1:
            end_idx = total_len
        else:
            end_idx = start_idx + int(total_len * ratio)

        # 이것때문에 리스트에 컬럼이 포함된다.
        splits.append(df.iloc[start_idx:end_idx].reset_index(drop=True))
        start_idx = end_idx

    # 대략산정한 기간산정데이터 중 비율에 맞게 평일과 주말 데이터로 구분해서 리턴한다.
    return splits[0], splits[1]


################################################################ 요청기간의 주말과 휴일 날짜 구하기
def get_splitdata():
    """
    :rtype: tuple[실제기간의 평일리스트, 실제기간의 주말리스트]
    """
    current_date = START_DAY
    end_date = END_DAY

    wday = []
    hday = []

    while current_date <= end_date:

        # 주말과 평일을 구분해서 담자
        dday = current_date.strftime('%Y-%m-%d')
        if not current_date.weekday() >= 5 and not is_holiday(dday):
            wday.append(dday)
        else:
            hday.append(dday)
        current_date += timedelta(days=1)

    return wday, hday



################################################################ 대략산정한 기간의 데이터를 분리하기 위한 기간의 각 날짜마다 적당히 분배
def split_total_near_equal_random(total: int, k: int, noise: float = 0.05, seed: int = None) -> Tuple[List[int], List[float]]:
    """
    todo 실제 구하고자 하는 기간의 날짜맏 대략 생플데이터를 어느 정도씩 분배해야 되는지를 구하기 위함.
    비율이 서로 비슷(1/k 근처)하지만 약간 랜덤하게 total을 k개 정수로 분할.
    - counts 합 = total
    - ratios 합 = 1
    noise: 0에 가까울수록 거의 균등, 커질수록 변동 증가 (권장 0~0.2)
    """
    if seed is not None:
        random.seed(seed)
    if k <= 0:
        raise ValueError("k must be positive")
    if total < 0:
        raise ValueError("total must be non-negative")
    if total == 0:
        return [0]*k, [0.0]*k

    # 1 주변의 가중치 생성 (음수 방지)
    weights = [max(0.0, 1.0 + random.uniform(-noise, noise)) for _ in range(k)]
    s = sum(weights)
    if s == 0:
        weights = [1.0]*k
        s = k

    ratios = [w / s for w in weights]
    ratios[-1] = 1.0 - sum(ratios[:-1])  # 합 보정

    # 비율대로 정수 할당: floor 후 남은 개수는 소수점 큰 순으로 추가
    raw = [r * total for r in ratios]
    counts = [int(x) for x in raw]
    remain = total - sum(counts)

    # 남은 remain을 fractional part 큰 순으로 1씩 배분
    frac_idx = sorted(range(k), key=lambda i: raw[i] - counts[i], reverse=True)
    for i in frac_idx[:remain]:
        counts[i] += 1

    # 최종 ratios는 counts 기반으로 다시 계산(정수 배분 결과와 일치)
    ratios = [c / total for c in counts]
    ratios[-1] = 1.0 - sum(ratios[:-1])

    return counts, ratios

########################################################################################## 데이터를 에디팅 하자
def data_editing():

    # 1.여기서 평일과 주말로 분리된 데이터를 가져온다. 여기는 개발서버에서 수집한 샘플데이터이다.
    print("====================> 에디팅 시작")
    workingdata_list, holidaydata_list = split_dataframe_by_ratios(SAMPLE_SDAY, SAMPLE_EDAY)

    # 2.평일과 주말 날짜를 가져온다.
    print("====================> 평일과 주말 날짜를 세팅")
    wday_list, hday_list = get_splitdata()


    # 3.가져온 데이터를 평일과 주말 개수에 맞게 적절하게 분리하게 위한 개수를 구한다.
    print("====================> 데이터 분리를 위한 개수 세팅")
    workingdata_count = len(workingdata_list)
    wday_count = len(wday_list)

    holidaydata_count = len(holidaydata_list)
    hday_count = len(hday_list)

    # 4.실제 구하고자 하는 기간의 배분된 개수와 비율을 구한다.
    print("====================> 기간의 배분된 개수와 비율 세팅")
    w_c, w_r = split_total_near_equal_random(workingdata_count, wday_count, noise=0.4, seed=42)
    h_c, h_r = split_total_near_equal_random(holidaydata_count, hday_count, noise=0.4, seed=42)


    # 5. 평일데이터를 분리해서 담는다.
    print("====================> 평일데이터 세팅")
    start_index = 0
    end_index = 0

    working_df = pd.DataFrame(data=workingdata_list)
    working_df['D_Day'] = '0000-00-00'

    for i, item in enumerate(w_c):
        end_index = start_index + item
        if i == len(w_c) - 1:
            working_df.iloc[start_index:, 5] = wday_list[i]         #여기서 인덱스 5는 새로추가한 D_Day컬럼이다.
        else:
            working_df.iloc[start_index:end_index, 5] = wday_list[i]
        start_index = end_index


    # 6. 주말데이터를 분리해서 담는다.
    print("====================> 주말데이터 세팅")
    start_index = 0
    end_index = 0

    holiday_df = pd.DataFrame(data=holidaydata_list)
    holiday_df['D_Day'] = '0000-00-00'

    # 주말데이터를 분리해서 담는다.
    for i, item in enumerate(h_c):
        end_index = start_index + item
        if i == len(h_c) - 1:
            holiday_df.iloc[start_index:, 5] = hday_list[i]
        else:
            holiday_df.iloc[start_index:end_index, 5] = hday_list[i]
        start_index = end_index

    result_df = pd.concat([working_df, holiday_df])


    print("====================> 전체 데이터 세팅")
    # 수집한 날짜를 세팅하자
    # 잠시 타입을 바꾸자. 데이터타입이라 수정하기 좀 곤란해서 일단 문자열로 바꾼다.
    result_df['VISIT_DT'] = result_df['VISIT_DT'].astype(str)

    for item in range(0,len(result_df)):
        strv = result_df.iloc[item, 3]  # 과거날짜를 아래 날짜로 바꾼다.
        strd = result_df.iloc[item, 5]  # 이 날짜를 기준으로
        strv = re.sub('[\d]{4}-[\d]{2}-[\d]{2}',strd, strv)
        result_df.iloc[item, 3] = strv


    # 다시 타입원상태
    result_df['VISIT_DT'] = pd.to_datetime(result_df['VISIT_DT'])
    result_df.sort_values(by='VISIT_DT', ascending=True, inplace=True)

    # 나중 db에 넣기 위해 엑셀로 내보내기 한번 해놓고
    result_df.to_excel("Result.xlsx")

    print("====================> 일별 통계 작성")
    # 지금부터가 본격적인 작업. 통계를 만들어보자
    # 1. 날짜별 통계를 구하자
    groupdf = result_df.groupby(['D_Day'])
    data_list = []
    col_list = ['날짜', '방문자수', '순방문자수']
    for key, group in groupdf:
        ilist = []
        ilist.append(key[0])

        count1 = len(group)     # 전체 방문자수
        ilist.append(count1)

        ndf = group[['VISIT_IP']]
        ndf = ndf['VISIT_IP'].drop_duplicates()
        count2 = len(ndf)       # 전제 순방문자수
        ilist.append(count2)

        data_list.append(ilist)

    to_df = pd.DataFrame(data=data_list, columns=col_list)
    to_df.to_excel("Result_DateSumary.xlsx")

    # 2. 월별 통계를 구하자
    print("====================> 월별 통계 작성")
    wdf = result_df.copy()
    wdf['M_Mon'] = result_df['D_Day']

    for item in range(0, len(wdf)):
        strv = wdf.iloc[item, 5]
        strv = strv[0:7]
        wdf.iloc[item, 6] = strv

    groupdf = wdf.groupby(['M_Mon'])
    data_list = []
    col_list = ['년월', '방문자수', '순방문자수']
    for key, group in groupdf:
        ilist = []
        ilist.append(key[0])

        count1 = len(group)  # 전체 방문자수
        ilist.append(count1)

        ndf = group[['VISIT_IP']]
        ndf = ndf['VISIT_IP'].drop_duplicates()
        count2 = len(ndf)  # 전제 순방문자수
        ilist.append(count2)

        data_list.append(ilist)

    to_df = pd.DataFrame(data=data_list, columns=col_list)
    to_df.to_excel("Result_MonSumary.xlsx")

    # 3. 기간내 통계를 구하자
    print("====================> 전체 통계 작성")
    wdf = result_df.copy()
    count1 = len(wdf)  # 기간내 총방문자수

    wdf = wdf['VISIT_IP'].drop_duplicates()
    count2 = len(wdf)  # 기간내 순방문자수

    print(f"기간내 총방문자수:{count1}, 순방문자수:{count2}")


if __name__ == "__main__":
    maria_db_conn()
    data_editing()
    print("work complete")