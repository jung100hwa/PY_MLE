import cx_Oracle
import sshtunnel

# HOST = "127.0.0.1"
# REMOTE_PORT = 1521
# LOCAL_PORT = 1521
# USER_NAME = "root"
# ssh_pw = '!!hgl1651ok'
# DSN = "scott/tiger@127.0.0.1:1521/XE"
#
# with sshtunnel.SSHTunnelForwarder(HOST, ssh_username = USER_NAME,
#                                   remote_bind_address = ("127.0.0.1", REMOTE_PORT),
#                                   ssh_password=ssh_pw,
#                                   local_bind_address = ("", LOCAL_PORT)) as server:
#
#     conn = cx_Oracle.connect(DSN)
#     cursor = conn.cursor()
#     cursor.execute("select * from dept")
#     for row in cursor:
#         print(row)


connection = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/XE')
cursor = connection.cursor()
cursor.execute("select * from dept")
for row in cursor:
    print(row)
