import sql_connect

def create_table_bidvest(date):
    query = """CREATE TABLE IF NOT EXISTS bidvest."""+date+""" (
        id INT NOT NULL,
        device VARCHAR (50) NOT NULL,
        time_start DATETIME,
        status VARCHAR (100) NOT NULL,
        value_1 VARCHAR (20),
        value_2 VARCHAR (20),
        time_end DATETIME,
        notification VARCHAR (100) NOT NULL);
        """
    sql_connect.cursor1.execute(query)

def create_table_alarms(): # This to the original `bidvest` database.
    query = """CREATE TABLE IF NOT EXISTS alarms.csv (
        Id INT NOT NULL,
        FLC VARCHAR (50) NOT NULL,
        TmStampVAS DATETIME,
        AXShortMsg VARCHAR (100) NOT NULL,
        Lolimit VARCHAR (20),
        Hilimit VARCHAR (20),
        ResolvedStamp DATETIME,
        Comment VARCHAR (100) NOT NULL,
        CSVDate DATETIME);
        """
        # Note that CSVDate is now an added column.
    sql_connect.cursor2.execute(query)

def create_table_archive():
    query = """CREATE TABLE IF NOT EXISTS archive.csv (
        Id INT NOT NULL,
        TmStamp DATETIME,
        Value DECIMAL(20, 4) NOT NULL,
        Status INT NOT NULL);
        """
    sql_connect.cursor3.execute(query)

def create_table_device():
    query = """CREATE TABLE IF NOT EXISTS device.lookup (
        FLC VARCHAR (50) NOT NULL,
        device INT NOT NULL);
        """
    sql_connect.cursor4.execute(query)