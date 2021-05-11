import csv
import sql_connect
import create

def insert(row, date):
    insert_a = row[2]
    insert_b = row[6]
    if row[2] in (None, ""):
        insert_a = '0000-00-00 00:00:00'
    if row[6] in (None, ""):
        insert_b = '0000-00-00 00:00:00'
    query = """INSERT INTO bidvest.readings"""+date+"""\
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(int(row[0]), row[1], insert_a, row[3], row[4], row[5], insert_b, row[7])
    sql_connect.cursor.execute(query)

def to_DB(path, myCSV):
    date = myCSV[13:21]
    create.create_table(date)
    with open(path + "\\" + myCSV) as myFile:
        reader = csv.reader(myFile)

        for row in reader:
            insert(row, date)
            # print(date)
            # print("-----")