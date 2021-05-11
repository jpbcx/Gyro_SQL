import sql_connect

def create_table(date):
    query = """CREATE TABLE IF NOT EXISTS bidvest.readings"""+date+""" (
        id INT NOT NULL,
        device VARCHAR (50) NOT NULL,
        time_start DATETIME,
        status VARCHAR (100) NOT NULL,
        value_1 VARCHAR (20),
        value_2 VARCHAR (20),
        time_end DATETIME,
        notification VARCHAR (100) NOT NULL);
        """
    sql_connect.cursor.execute(query)