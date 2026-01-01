"""
유튜브에서 관련 3D프린팅 관련 최근 3년간 영상을 가져온다
이 모듈은 다른 모듈과 테이블 컬럼이 약간 다르다. 대표적인게 유튜브 게시일자를 컬럼에 넣어 줬다.
배포시 유튜브 키를 3D협회 담당자로 받아야 한다.

# 이 파일은 기본적인 연습용이다. 앞으로 사용할일이 없다.
# todo 3D_YoutudeCrawling_ad 대체 되었고. 터널링을 위해서 3D_YoutudeCrawling_ad_real 사용해야 한다.

"""

from googleapiclient.discovery import build
import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine
import schedule
import re
import time

# 아래 구글 API를 일단 얻어야 한다. 많이 수집하면 유료라고 하는데 유료인지는 잘 모르겠음
mov_url = "https://www.youtube.com/watch?v="
api_key = "AIzaSyBhMXAVJnM7hblfOH1CHvmD3qrI5uHA6J0"
youtube = build("youtube", "v3", developerKey=api_key)
KEYWORD = ['3D프린팅', '3Dprinter', '3D프린팅성공사례', '3D프린팅정보','3D프린터', '3Dprinting', '삼차원프린팅','쓰리디프린팅','적층제조', 'Rapid Prototyping', 'Rapid Prototype']


# 날짜 제한을 두자.
def date_collect(x):
    return (datetime.date.today() + datetime.timedelta(days=-365*x)).strftime('%Y') # 최근 3년간만

dtday = datetime.date.today().strftime('%Y-%m-%d')
coll_day = list(map(date_collect,range(0,3)))

column_list = ['OKEY', 'LINK', 'THUMBLINK', 'TITLE','TAG', 'CONF', 'PDAY','TDAY']

conn = None

########################################################################################## 데이터베이스 연결
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

########################################################################################## 마리아db로 인서트
def maria_db_insert(result_list):
    if len(result_list) > 0:
        df = pd.DataFrame(data=result_list, index=np.arange(1, len(result_list) + 1),
                          columns=['OKEY', 'LINK', 'THUMBLINK', 'TITLE','TAG', 'CONF','PDAY','TDAY'])

        # 빈값 삭제
        df['LINK'] = df['LINK'].replace('', np.nan)
        df['THUMBLINK']=df['THUMBLINK'].replace('', np.nan)
        df['TITLE'] = df['TITLE'].replace('', np.nan)
        df.dropna(subset=['LINK', 'THUMBLINK','TITLE'], how='any', inplace=True)

        # 중복값 삭제
        df.drop_duplicates(subset=['LINK'], keep='first', inplace=True, ignore_index=True)
        df.drop_duplicates(subset=['THUMBLINK'], keep='first', inplace=True, ignore_index=True)
        df.drop_duplicates(subset=['TITLE'], keep='first', inplace=True, ignore_index=True)

        # DB로 인서트
        try:
            query = f"select LINK, THUMBLINK, TITLE from tn_tdb_youtube"
            result_df = pd.read_sql_query(query, conn)
            conn.commit()

            # 기존 db에 등록되어 있는 중복값 제거
            df = df.merge(result_df, how='outer', on=['LINK'], indicator=True).loc[
                lambda x: x['_merge'] == 'left_only']
            df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
            df.columns = column_list

            if len(df) > 0:
                df.to_sql('tn_tdb_youtube', conn, if_exists='append', index=False)
                conn.commit()
                print(f"{len(df)} Insert")

                # 데이터베이스 입력건수를 데이터베이스에 입력(다른데 하고 조금 틀림)
                query = f"select ORIGIN, TDAY from tn_tdb_collectinfo where OKEY='301' and TDAY='{dtday}'"
                result_df = pd.read_sql_query(query, conn)
                
                if len(result_df) == 0:
                    alist = [['301', '유튜브 영상', str(len(df)), dtday]]
                    df_in = pd.DataFrame(data=alist, index=np.arange(1, 2),
                                         columns=['OKEY', 'ORIGIN', 'INNUM', 'TDAY'])
                    df_in.to_sql('tn_tdb_collectinfo', conn, if_exists='append', index=False)
                    conn.commit()

            else:
                print(f"No recent data")
                
                # 아래 동일한 코드가 여기도 있어야 함. result_list에는 값이 있는데 동일한 값이 db에 있는 경우가 있음
                non_data = {
                    "OKEY": ['301'],
                    "ORIGIN": ['유튜브영상'],
                    "INNUM": [0],
                    "TDAY": [dtday]
                }
                non_df = pd.DataFrame(non_data)
                non_df.to_sql('tn_tdb_collectinfo', conn, if_exists='append', index=False)
                conn.commit()
        except:
            print("DBConnection is not availableon this machine")
            
    # 수집한 데이터가 없을 경우도 0 건수를 입력 함. 단지 시스템 가동되는지 확인하기 위해
    else:
        try:
            non_data ={
                "OKEY": ['301'],
                "ORIGIN":['유튜브영상'],
                "INNUM": [0],
                "TDAY":[dtday]
            }
            non_df = pd.DataFrame(non_data)
            non_df.to_sql('tn_tdb_collectinfo', conn, if_exists='append', index=False)
            conn.commit()
        except:
            print("Data insert error")


def youtube_search():
    orign_key  ='301'
    tag_text = '유튜브영상'
    conf_text = "0"

    request = youtube.search().list(
        q=KEYWORD,
        part="snippet",
        maxResults=10,
        # order="date",
        type="video"
    )
    response = request.execute()
    result_list =  []

    try:
        for item in response["items"]:
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            title = title.replace("\xa0", " ")
            thumbnail_url = item['snippet']['thumbnails']['high']['url']

            # 최근 3년간 동영상만 보자. 너무 오래된 것은 현실성이 떨어진다.
            publish_date = item['snippet']['publishedAt']
            publish_date2 =''
            if publish_date:
                publish_date1 = publish_date[0:4]
                publish_date1=coll_day.count(publish_date1)
                if publish_date1 == 0:
                    continue

                publish_date2 = publish_date[0:10]

            video_id_url = f"{mov_url}{video_id}"
            result_list.append([orign_key, video_id_url, thumbnail_url, title, tag_text, conf_text, publish_date2, dtday])
    except:
        print("Youtube search error")

    marial_db_insert(result_list)


def crawling_exe():
    print("=======================> collection start")
    maria_db_conn()
    youtube_search()
    conn.close()
    print("=======================> collection end")


# schedule.every().day.at("01:30").do(crawling_exe) #매일 새벽 1시 30분에

if __name__ == "__main__":
    # while True:
    #     print("===============> YouTube Processing")
    #     schedule.run_pending()
    #     time.sleep(3)
    crawling_exe()