#!/usr/bin/python3
"""
a module filter cities by state input safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM `cities` as `curr` \
                INNER JOIN `states` as `s` \
                   ON `curr`.`state_id` = `s`.`id` \
                ORDER BY `curr`.`id`")
    print(", ".join([ct[2] for ct in curr.fetchall() if ct[4] == sys.argv[4]]))
