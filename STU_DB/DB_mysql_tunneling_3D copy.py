from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine, text
import pymysql

# SSH 및 DB 접속 정보
SSH_HOST = 'your_ssh_server_ip'
SSH_PORT = 22
SSH_USER = 'your_ssh_user'
SSH_PASSWORD = 'your_ssh_password' # 또는 SSH 키 파일 경로

DB_HOST = 'private_db_host' # SSH 서버 내부 DB 호스트 (보통 localhost 또는 127.0.0.1)
DB_PORT = 3306 # 실제 DB 포트
DB_USER = 'db_user'
DB_PASSWORD = 'db_password'
DB_NAME = 'your_db_name'

# 로컬에서 사용할 포트
LOCAL_BIND_PORT = 3307 # 임의의 사용하지 않는 포트

with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_password=SSH_PASSWORD, # 또는 ssh_pkey='path/to/your/key'
    remote_bind_address=(DB_HOST, DB_PORT),
    local_bind_address=('127.0.0.1', LOCAL_BIND_PORT)
) as tunnel:
    # SQLAlchemy 연결 문자열
    # 로컬 포트(LOCAL_BIND_PORT)를 통해 원격 DB로 연결됨
    db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{tunnel.local_bind_host}:{tunnel.local_bind_port}/{DB_NAME}"
    
    engine = create_engine(db_url)
    
    # DB 연결 및 쿼리 실행 예시
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"DB Connection Successful: {result.scalar()}")
        # 추가적인 쿼리 작업...

print("SSH Tunnel closed.")
