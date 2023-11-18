#!/usr/bin/python3
"""
a module that lists all states with a name starting
with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY 'N%'\
             ORDER BY states.id ASC"
    curr = db.curr()
    curr.execute(query)
    for state in curr.fetchall():
        print(state)
    curr.close()
    db.close()
