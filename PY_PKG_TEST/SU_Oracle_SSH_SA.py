import cx_Oracle
from sshtunnel import SSHTunnelForwarder

HOST = "127.0.0.1"
REMOTE_PORT = 1521
LOCAL_PORT = 1521
USER_NAME = "root"
ssh_pw = '!!hgl1651ok'
DSN = "scott/tiger2@192.168.56.1:1521/XE"


server = SSHTunnelForwarder(HOST, ssh_username = USER_NAME,
                                  remote_bind_address = ("127.0.0.1", REMOTE_PORT),
                                  ssh_password=ssh_pw,
                                  local_bind_address = ("", LOCAL_PORT))
server.start()

conn = cx_Oracle.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from dept")
for row in cursor:
    print(row)

server.stop()