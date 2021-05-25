import mysql.connector

"""
    Different connectors for the different database.
"""

conn_bidvest  = mysql.connector.connect(
    host = "127.0.0.1",
    user = "",
    password = "",
    database = "bidvest",
    autocommit = True
)
cursor1 = conn_bidvest.cursor()
# Tables have been named according to date.

conn_alarms  = mysql.connector.connect(
    host = "127.0.0.1",
    user = "",
    password = "",
    database = "gyro_bms", # This is the new DB that has been created.
    autocommit = True
)
cursor2 = conn_alarms.cursor()
# Tables:
#   -alarm
#   -device
#   -archive