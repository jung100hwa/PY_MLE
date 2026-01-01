"""
터널링은 원격 작업하고는 조금 다르다. 원격은 vsc, pycharm 방식이 다르다
이번 예제는 로컬에서 개발하고 프라이빗 영역에 있는 db만 터널링으로 접근하는 방식이다.
터널링은 원격 AP라고 생각하면 AP안에 DB서버가 따로 있을 경우가 크다. 다만 집에서 테스트할때는 AP 자체에 DB이다.
왜냐하면 한대에서 다 돌리니까.
그리고 pandas와 같이 할려면 pymysql이 아닌 sqlalchemy를 사용해야한다. 둘다 읽기는 가능한데 쓰기에 차이가 있다.
아래의 예제는 하나는 pymysql, 하나는 pandas와 함께 sqlalchemy 예제이다.
"""

#################################################################pymysql 예제
# from sshtunnel import SSHTunnelForwarder
# import pymysql


# # SSH 접속 정보
# SSH_HOST = "211.221.212.52"
# SSH_PORT = 22
# SSH_USER = "jung100hwa"
# SSH_PASSWORD = "!!hgl1651ok"  # 또는 ssh_pkey = '/path/to/key' 둘주에 하나로 가능하다.

# # MySQL 서버 정보 (SSH 서버 내부 기준)
# REMOTE_MYSQL_HOST = "127.0.0.1"  # 또는 MySQL이 위치한 내부 IP
# REMOTE_MYSQL_PORT = 3306  # MySQL 기본 포트

# # 로컬에서 바인딩할 포트 (충돌하지 않는 포트)
# LOCAL_BIND_PORT = 3306  # 임의의 포트


# with SSHTunnelForwarder(
#     (SSH_HOST, SSH_PORT),
#     ssh_username=SSH_USER,
#     ssh_password=SSH_PASSWORD,
#     remote_bind_address=(REMOTE_MYSQL_HOST, REMOTE_MYSQL_PORT),
#     local_bind_address=("127.0.0.1", LOCAL_BIND_PORT),
# ) as tunnel:
#     # 터널이 열린 상태에서 MySQL 접속
#     conn = pymysql.connect(
#         host="127.0.0.1",
#         port=tunnel.local_bind_port,  # 터널이 연 로컬 포트 사용
#         user="jung100hwa",
#         password="!!hgl1651ok",
#         database="DB1",
#     )

#     # 데이터 조회 예시
#     # todo 중요한 것은 이것들은 터널안에서 이루어져야 한다는 것이다.
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM ta_01;")
#         results = cursor.fetchall()
#         print(results)

#     conn.close()

################################################################# pandas와 sqlalchemy 예제

from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import pandas as pd

# SSH 접속 정보
SSH_HOST = "211.221.212.52"
SSH_PORT = 22
SSH_USER = "jung100hwa"
SSH_PASSWORD = "!!hgl1651ok"  # 또는 ssh_pkey = '/path/to/key'

# MySQL 서버 정보 (SSH 서버 내부 기준)
REMOTE_MYSQL_HOST = "127.0.0.1"  # 또는 MySQL이 위치한 내부 IP
REMOTE_MYSQL_PORT = 3306  # MySQL 기본 포트

# 로컬에서 바인딩할 포트 (충돌하지 않는 포트)
LOCAL_BIND_PORT = 3306  # 임의의 포트


with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=(REMOTE_MYSQL_HOST, REMOTE_MYSQL_PORT),
    local_bind_address=("127.0.0.1", LOCAL_BIND_PORT),
) as tunnel:
    db_url = "mysql+pymysql://jung100hwa:!!hgl1651ok@127.0.0.1:3306/DB1"
    engine = create_engine(db_url)
    conn = engine.connect()
    query = "SELECT * FROM ta_01"
    df = pd.read_sql_query(query, conn)
    print(df)

    df.to_sql("ta_01", conn, if_exists="append", index=False)  # db insert
    conn.commit()

    conn.close()
