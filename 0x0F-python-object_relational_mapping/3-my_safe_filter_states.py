#!/usr/bin/python3
"""
a module that filters states by user input safe from
MySQL injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM `states`")
    [print(state) for state in curr.fetchall() if state[1] == sys.argv[4]]
