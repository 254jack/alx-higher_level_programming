#!/usr/bin/python3
"""
A function that Lists all states from
the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    curr = db.curr()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in curr.fetchall():
        print(state)
    curr.close()
    db.close()
