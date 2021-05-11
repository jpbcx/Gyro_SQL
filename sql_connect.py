import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "",
    password = "",
    database = "bidvest",
    autocommit = True
)
# if conn.is_connected():
#     print("---Connected to DB---")
#     print(conn.get_server_info())

cursor = conn.cursor()