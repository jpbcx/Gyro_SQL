import sql_connect

query = """SHOW TABLES
FROM bidvest;
"""
sql_connect.cursor1.execute(query)
table_list = [item[0] for item in sql_connect.cursor1.fetchall()]
# The above line translates the tuple to a list.
print(table_list)

sum = 0

for table in table_list:
    # print(table)
    query = """SELECT COUNT(*)
    FROM bidvest."""+table+""";
    """
    sql_connect.cursor1.execute(query)
    result = sql_connect.cursor1.fetchall()
    sum = sum + int(result[0][0])

print(str(sum)+" rows")

##########

print("`alarm`")

query = """SELECT COUNT(*)
FROM gyro_bms.alarm;
"""
sql_connect.cursor2.execute(query)
result = sql_connect.cursor2.fetchall()
sum = int(result[0][0])

print(str(sum)+" rows")