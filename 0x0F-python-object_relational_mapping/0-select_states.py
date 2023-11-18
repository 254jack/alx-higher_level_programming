#!/usr/bin/python3
"""
a module that lists all states from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM `states`")
    [print(state) for state in curr.fetchall()]
