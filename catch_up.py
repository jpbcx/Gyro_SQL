import os
import to_SQL

"""
    Rename this to catch_up.py
"""

path = ""
for name in os.listdir(path):
    if name.endswith(".csv"):
        print(name)
        # Do a table for each day.
        to_SQL.to_DB(path, name)