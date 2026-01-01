"""
터널링은 원격 작업하고는 조금 다르다. 원격은 vsc, pycharm 방식이 다르다
이번 예제는 로컬에서 개발하고 프라이빗 영역에 있는 db만 터널링으로 접근하는 방식이다.
터널링은 원격 AP라고 생각하면 AP안에 DB서버가 따로 있을 경우가 크다. 다만 집에서 테스트할때는 AP 자체에 DB이다.
왜냐하면 한대에서 다 돌리니까.
그리고 pandas와 같이 할려면 pymysql이 아닌 sqlalchemy를 사용해야한다. 둘다 읽기는 가능한데 쓰기에 차이가 있다.
아래의 예제는 하나는 pymysql, 하나는 pandas와 함께 sqlalchemy 예제이다.
"""

################################################################# pandas와 sqlalchemy 예제

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

# 로컬에서 바인딩할 포트 (충돌하지 않는 포트)
LOCAL_BIND_PORT = 3306  # 임의의 포트


with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=(REMOTE_MYSQL_HOST, REMOTE_MYSQL_PORT),
    local_bind_address=("127.0.0.1", LOCAL_BIND_PORT),
) as tunnel:    
    db_url = "mysql+pymysql://root:3dbankdb1218@127.0.0.1:3306/3dbank_new" # 이부분이 로커 호스트와 로컬 포트를 적는 구나.
    engine = create_engine(db_url)
    conn = engine.connect()
    query = "SELECT * FROM class_info"
    df = pd.read_sql_query(query, conn)
    print(df)

    conn.commit()
    conn.close()
