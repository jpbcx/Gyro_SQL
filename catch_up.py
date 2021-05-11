import os
import to_SQL

"""
    Rename this to catch_up.py
"""

# for name in os.listdir("C:\\Users\\jonathanp\\Documents\\Bidvest CSV-SQL\\Work\\CSV files"):
path = "C:\\Users\\jonathanp\\Documents\\Bidvest CSV-SQL\\Work\\CSV files"
for name in os.listdir(path):
    if name.endswith(".csv"):
        print(name)
        # Do a table for each day.
        to_SQL.to_DB(path, name)