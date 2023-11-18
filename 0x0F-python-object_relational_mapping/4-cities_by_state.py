#!/usr/bin/python3
"""
a module that lists all cities from the database using foreing key
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT `curr`.`id`, `curr`.`name`, `s`.`name` \
                 FROM `cities` as `curr` \
                INNER JOIN `states` as `s` \
                   ON `curr`.`state_id` = `s`.`id` \
                ORDER BY `curr`.`id`")
    [print(city) for city in curr.fetchall()]
