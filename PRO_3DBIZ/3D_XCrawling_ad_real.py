"""
# todo 실제 운영서버 파일이다. 이 파일은 터널링을 구현한 것으로 운영서버전 3D_XCrawling_ad 로 테스트해서 변경된 부분을 이 파일로 대체해야 함
"""

"""
# todo 현재 15분으로 되어 있는데 이렇게 까지 해야 되나 싶다. 트위터 스펙을 한번 보고 시간을 줄여 보자

@ 프로그램 : 3D상상포털 트위터에 내용전달
@ 절차
    1-트위터 개발자사이트에서 관련키 받기
        todo 반드시 권한 설정하고. 그 다음 관련 키 받기
    2-마리아DB 연결하고 특정테이블(현재는 유투브) 자료 트윗하기
@ 주의사항 : 무료키라 트윗하는 개수의 한개가 있음(10,000 라고 하는데 맞는지 모르겠음)
"""

import tweepy
from sqlalchemy import create_engine
from datetime import date
import pandas as pd
import schedule
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


dtday = date.today()
conn = None

# TABLE_LIST = ['tn_tdb_youtube','tn_tdb_crawling','tn_tdb_busicrawling']
TABLE_LIST = ['tn_tdb_busicrawling']


########################################################################################## 트위터 인증 코드
# jung2hwa@naver.com
client = tweepy.Client(
    access_token="1998415303089504256-f5FR517feaTNaOLaM8ZHegZpYOTWgV",
    access_token_secret="1AlyLVG6ILBsJSMlEOF1sDdSTeaxmt4XDnfV1k22FirAK",
    consumer_key="PqwgesUYrPP3kGGC0mMth6xeG",
    consumer_secret="13J6MYVthfROc473d2Jvj6HGrFgjvGHwAlxzRjMKi99IlEexcv",
    bearer_token="AAAAAAAAAAAAAAAAAAAAAJ%2B95wEAAAAACWqPw1BLwSMdjKo3NoyhuYKd%2BZc%3DcrAFGltuQV4TyJtB3zhczwOdmrZGQEoVsnAJ7SXe4N1HKQlP8J",
)


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

        tweet_send_table()

        conn.commit()
        conn.close()

########################################################################################## 트위터로 보내기
def tweet_send_table():
    for table_name in TABLE_LIST:
        query = f"select title, link from {table_name} where tday ='{dtday}'"
        df = pd.read_sql_query(query, conn)

        if len(df) > 0:
            for index, row in df.iterrows():
                title_url = "3D 상상포털 https://www.3dbank.or.kr\n " + row['title']
                sendtext = f"{title_url} - {row['link']}"
                print(f"================> {sendtext}")
                client.create_tweet(text=sendtext)
                if len(df)-1 == index:
                    break
                time.sleep(60)


def crawling_exe():
    print("=======================> collection start")
    maria_db_conn()
    print("=======================> collection end")


# schedule.every().day.at("02:00").do(crawling_exe) #매일 새벽 2시에. 수집이 1시 30분이니까.

if __name__ == "__main__":
    # while True:
    #     print("===============> Tweet Processing")
    #     schedule.run_pending()
    #     time.sleep(3)
    crawling_exe()
