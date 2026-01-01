"""
# 이 파일은 기본적인 연습용이다. 앞으로 사용할일이 없다.
# todo 3D_XCrawling_ad 대체 되었고. 터널링을 위해서 3D_XCrawling_ad_real 사용해야 한다.
"""

"""
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

dtday = date.today()
conn = None

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
    try:
        db_url = "mysql+pymysql://root:3dbankdb1218@175.126.176.174:3307/3dbank_v1"
        engine = create_engine(db_url)
        conn = engine.connect()
        print("DBConnection is success!!")
    except:
        print("DBConnection is not availableon this machine")
        exit()


########################################################################################## 트위터로 보내기
# 현재는 유트브 스크롤링 데이터를 하루에 3개씩만 보냄
def youtube_search():
    query = f"select title, link from tn_tdb_youtube where tday ='{dtday}'"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            title_url = "3D 상상포털 https://www.3dbank.or.kr\n " + row['title'] 
            # sendtext = f"{row['title']} - {row['link']}"
            sendtext = f"{title_url} - {row['link']}"
            print(f"================> {sendtext}")
            client.create_tweet(text=sendtext)
            time.sleep(60 * 15)
    print("Youtube Tweet has been success!!")


# 수집한 자료
def collection_search():
    query = f"select title, link from tn_tdb_crawling where tday ='{dtday}'"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            title_url = "3D 상상포털 https://www.3dbank.or.kr\n " + row['title'] 
            # sendtext = f"{row['title']} - {row['link']}"
            sendtext = f"{title_url} - {row['link']}"
            print(f"================> {sendtext}")
            client.create_tweet(text=sendtext)
            time.sleep(60 * 15)
    print("Tweet has been success!!")


# 사업,입찰 등
def business_search():
    query = f"select title, link from tn_tdb_busicrawling where tday ='{dtday}'"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            title_url = "3D 상상포털 https://www.3dbank.or.kr\n " + row['title'] 
            # sendtext = f"{row['title']} - {row['link']}"
            sendtext = f"{title_url} - {row['link']}"
            print(f"================> {sendtext}")
            client.create_tweet(text=sendtext)
            time.sleep(60 * 15)
    print("Tweet has been success!!")


def crawling_exe():
    print("=======================> collection start")
    maria_db_conn()
    youtube_search()
    # collection_search()
    # business_search()
    conn.close()
    print("=======================> collection end")


# schedule.every().day.at("02:00").do(crawling_exe) #매일 새벽 2시에. 수집이 1시 30분이니까.

if __name__ == "__main__":
    # while True:
    #     print("===============> Tweet Processing")
    #     schedule.run_pending()
    #     time.sleep(3)
    crawling_exe()
