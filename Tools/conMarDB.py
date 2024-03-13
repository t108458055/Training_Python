# Module Imports
import mariadb
import sys
# Basic usage — MariaDB Connector/Python 1.1.7 documentation
# https://mariadb-corporation.github.io/mariadb-connector-python/usage.html#connecting
# conn = None
# curr = None

# Connect to MariaDB Platform
try:
    conn =  mariadb.connect(
        user="andy",
        password="`1qaz2WSX3edc",
        host="192.168.0.102",
        port=3306,
        database="nor"
    )

    # 顯示資料庫版本
    db_Info = conn.server_version
    print("資料庫版本：", db_Info)
    # Get Cursor
    curr = conn.cursor()
    curr.execute("SELECT DATABASE();")
    record = curr.fetchone()
    print("目前使用的資料庫: ", record)

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform:{e}")
    sys.exit(1)

finally:
    if curr:
        curr.close()
    if conn:
        conn.close()
    print("資料庫連線已關閉")