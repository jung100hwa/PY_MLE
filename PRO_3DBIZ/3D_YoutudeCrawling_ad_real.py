"""
유튜브에서 관련 3D프린팅 관련 최근 3년간 영상을 가져온다
이 모듈은 다른 모듈과 테이블 컬럼이 약간 다르다. 대표적인게 유튜브 게시일자를 컬럼에 넣어 줬다.
배포시 유튜브 키를 3D협회 담당자로 받아야 한다.

# todo 실제 운영서버 파일이다. 이 파일은 터널링을 구현한 것으로 운영서버전 3D_YoutudeCrawling_ad 테스트해서 변경된 부분을 이 파일로 대체해야 함
"""

from googleapiclient.discovery import build
import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine
import schedule
import re
import time

########################################################################################## 터널링 정보
from sshtunnel import SSHTunnelForwarder

# SSH 접속 정보
SSH_HOST = "211.253.141.39"
SSH_PORT = 22
SSH_USER = "root"
SSH_PASSWORD = "3dbank@)!(01"  # 또는 ssh_pkey = '/path/to/key'


# MySQL 서버 정보 (SSH 서버 내부 기준)
REMOTE_MYSQL_HOST = "10.65.70.90"  # 또는 MySQL이 위치한 내부 IP
REMOTE_MYSQL_PORT = 3306  # MySQL 기본 포트
REMOTE_MYSQL_USER = "root"
REMOTE_MYSQL_PASSWORD = "3dbankdb1218"
REMOTE_MYSQL_DB = "3dbank_new"

# 로컬에서 바인딩할 포트 (충돌하지 않는 포트)
LOCAL_BIND_HOST = "127.0.0.1"
LOCAL_BIND_PORT = 3306  # 임의의 포트
########################################################################################## 터널링 정보

# 아래 구글 API를 일단 얻어야 한다. 많이 수집하면 유료라고 하는데 유료인지는 잘 모르겠음
mov_url = "https://www.youtube.com/watch?v="
api_key = "AIzaSyBhMXAVJnM7hblfOH1CHvmD3qrI5uHA6J0"
youtube = build("youtube", "v3", developerKey=api_key)
KEYWORD = ['3D프린팅', '3Dprinter', '3D프린팅성공사례', '3D프린팅정보','3D프린터', '3Dprinting', '삼차원프린팅','쓰리디프린팅','적층제조', 'Rapid Prototyping', 'Rapid Prototype']


# 날짜 제한을 두자.
def date_collect(x):
    return (datetime.date.today() + datetime.timedelta(days=-365*x)).strftime('%Y') # 최근 3년간만

dtday = datetime.date.today().strftime('%Y-%m-%d')
coll_day = list(map(date_collect,range(0,4)))

column_list = ['OKEY', 'LINK', 'THUMBLINK', 'TITLE','TAG', 'CONF', 'PDAY','TDAY']

conn = None

G_Result_list = []

########################################################################################## 데이터베이스 연결
def maria_db_conn():
    global conn

    with SSHTunnelForwarder(
            (SSH_HOST, SSH_PORT),
            ssh_username=SSH_USER,
            ssh_password=SSH_PASSWORD,
            remote_bind_address=(REMOTE_MYSQL_HOST, REMOTE_MYSQL_PORT),
            local_bind_address=(LOCAL_BIND_HOST, LOCAL_BIND_PORT),
    ) as tunnel:
        db_url = f"mysql+pymysql://{REMOTE_MYSQL_USER}:{REMOTE_MYSQL_PASSWORD}@{LOCAL_BIND_HOST}:{LOCAL_BIND_PORT}/{REMOTE_MYSQL_DB}"
        engine = create_engine(db_url)
        conn = engine.connect()

        maria_db_insert()

        conn.commit()
        conn.close()

########################################################################################## 마리아db로 인서트
def maria_db_insert():
    for ii, result_list in enumerate(G_Result_list):
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

                # 기존 db에 등록되어 있는 중복값 제거
                df = df.merge(result_df, how='outer', on=['LINK'], indicator=True).loc[
                    lambda x: x['_merge'] == 'left_only']
                df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
                df.columns = column_list

                if len(df) > 0:
                    df.to_sql('tn_tdb_youtube', conn, if_exists='append', index=False)
                    print(f"{len(df)} Insert")

                else:
                    print(f"No recent data")
            except:
                print("Data insert error")
        else:
            print(f"No recent data")


def youtube_search():
    orign_key  ='301'
    tag_text = '유튜브영상'
    conf_text = "1"

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

    G_Result_list.append(result_list)


def crawling_exe():
    print("=======================> collection start")

    G_Result_list = []

    youtube_search()

    maria_db_conn()

    print("=======================> collection end")


# schedule.every().day.at("01:30").do(crawling_exe) #매일 새벽 1시 30분에

if __name__ == "__main__":
    # while True:
    #     print("===============> YouTube Processing")
    #     schedule.run_pending()
    #     time.sleep(3)
    crawling_exe()