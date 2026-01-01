"""
AP가 2개인데 하나만 SSH로 활용해도 됨
    -211.253.141.39(onmakersWEB01) / 3dbank@)!(01
    -211.253.141.40(onmakersWEB02)/ 3dbank@)!(02
    -아이디는 root

AP 내부에 DB서버
    -10.65.70.90 (pw: 3dbankdb1218)
    -아이디는 root
"""

from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import pandas as pd

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
    query = "SELECT * FROM class_info"
    df = pd.read_sql_query(query, conn)
    print(df)

    conn.commit()
    conn.close()
