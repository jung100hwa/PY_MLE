"""
@ 프로그램 : 3D상상포털 트위터에 내용전달
@ 절차
    1-트위터 개발자사이트에서 관련키 받기
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
client = tweepy.Client(
    access_token="240128907-l6oalhysTqRcK8jFwZgNYuCsuyA8eILTZ6w14r7F",
    access_token_secret="jtN73lKxIKhiHaHTYm5wVOWXuEuOT5wqC3gMPU5qfCRIA",
    consumer_key="SpAEPoQnWreQF3rMn7FjQCG2R",
    consumer_secret="nkodLcxk7DXGNEr3HUx1AGTDDPmMqeBbqic4Sah4gbHLNY1NzQ",
    bearer_token="AAAAAAAAAAAAAAAAAAAAAEFH4gEAAAAAR9rw%2FdvQJT64BVTZ%2BLjcx9KlAqs%3D3C9pbEyDjW9Es063amJJpjIYVT3Iobaze2ht5r4AaexObzFxjM"
)

########################################################################################## 데이터베이스 연결
def maria_db_conn():
    global conn
    try:
        db_url = "mysql+pymysql://root:3dbankdb1218@175.126.176.174:3307/3dbank_new"
        engine = create_engine(db_url)
        conn = engine.connect()
        print("DBConnection is success!!")
    except:
        print("DBConnection is not availableon this machine")
        exit()


########################################################################################## 트위터로 보내기
# 현재는 유트브 스크롤링 데이터를 하루에 3개씩만 보냄
def youtube_search():
    query = f"select title, link from tn_tdb_youtube where tday ='{dtday}' and conf=1 limit 3"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            sendtext = f"{row['title']} - {row['link']}"
            client.create_tweet(text=sendtext)
    print("Youtube Tweet has been success!!")

# 수집한 자료
def collection_search():
    query = f"select title, link from tn_tdb_crawling where tday ='{dtday}' limit 3"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            sendtext = f"{row['title']} - {row['link']}"
            client.create_tweet(text=sendtext)
    print("Tweet has been success!!")

# 사업,입찰 등
def business_search():
    query = f"select title, link from tn_tdb_busicrawling where tday ='{dtday}' limit 3"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        for index, row in df.iterrows():
            sendtext = f"{row['title']} - {row['link']}"
            client.create_tweet(text=sendtext)
    print("Tweet has been success!!")


def crawling_exe():
    print("=======================> collection start")
    maria_db_conn()
    youtube_search()
    collection_search()
    business_search()
    conn.close()
    print("=======================> collection end")

schedule.every().day.at("02:00").do(crawling_exe) #매일 새벽 2시에. 수집이 1시 30분이니까.

if __name__ == "__main__":
    while True:
        print("===============> Tweet Processing")
        schedule.run_pending()
        time.sleep(3)
    # crawling_exe()
