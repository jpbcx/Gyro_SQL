import csv
import sql_connect
import create

"""
    There has been some changes.
    `alarms`, `divice` and `archive`
    have been moved to a single db
    called `gyro_bms`.
"""

#########
def insert_bidvest(row, date):
    insert_a = row[2]
    insert_b = row[6]
    if row[2] in (None, ""):
        insert_a = '0000-00-00 00:00:00'
    if row[6] in (None, ""):
        insert_b = '0000-00-00 00:00:00'
    query = """INSERT INTO bidvest."""+date+"""
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(int(row[0]), row[1], insert_a, row[3], row[4], row[5], insert_b, row[7])
    sql_connect.cursor1.execute(query)

def to_bidvest(path, myCSV):
    date = myCSV[13:21]
    create.create_table_bidvest(date)
    with open(path + "\\" + myCSV) as myFile:
        reader = csv.reader(myFile)

        for row in reader:
            insert_bidvest(row, date)
            # print(date)
            # print("-----")
#########

#########
def insert_alarms(row, date):
    insert_a = row[2]
    insert_b = row[6]
    if row[2] in (None, ""):
        insert_a = '0000-00-00 00:00:00'
    if row[6] in (None, ""):
        insert_b = '0000-00-00 00:00:00'
    query = """INSERT INTO gyro_bms.alarm
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(int(row[0]), row[1], insert_a, row[3], row[4], row[5], insert_b, row[7], date)
    sql_connect.cursor2.execute(query)

def to_alarms(path, myCSV):
    date = myCSV[13:17]+'-'+myCSV[17:19]+'-'+myCSV[19:21]+' '+myCSV[22:24]+':'+myCSV[24:26]
    # print(date)
    # create.create_table_alarms()
    with open(path + "\\" + myCSV) as myFile:
        reader = csv.reader(myFile)

        for row in reader:
            insert_alarms(row, date)
#########

"""
    The below code is not needed so it has been commented out.
    I've kept it incase but will delete soon.
"""

#########
# def insert_archive(row):
#     insert_a = row[1]
#     if row[1] in (None, ""):
#         insert_a = '0000-00-00 00:00:00'
#     query = """INSERT INTO archive.csv
#     VALUES('{}', '{}', '{}', '{}');""".format(int(row[0]), insert_a, float(row[2]), int(row[3]))
#     sql_connect.cursor3.execute(query)

# def to_archive(path, myCSV):
#     create.create_table_archive()
#     with open(path + "\\" + myCSV) as myFile:
#         reader = csv.reader(myFile)

#         for row in reader:
#             print(row)
#             insert_archive(row)
#             # print(date)
#             # print("-----")
#########

#########
# def insert_device(flc, num):
#     query = """INSERT INTO device.lookup
#     VALUES('{}', '{}');""".format(flc, int(num))
#     sql_connect.cursor4.execute(query)

# def to_device(path):
#     create.create_table_device()
#     with open(path) as myFile:
#         for line in myFile:
#             line = line.strip()
#             print(line)
#             if line[0].isdigit():
#                 continue
#             hold = line.split()
#             if not hold[1].isdigit():
#                 continue
#             if hold[0][0] == '-':
#                 hold[0] = hold[0][1:]
#             insert_device(hold[0], hold[1])
#########