#!/usr/bin/python3
# script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa
# sintax: mysql username mysql_password database name

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
