#!/usr/bin/python3
# an SQL injection to delete all records of a table…
# Sintax: ./3-select_states.py username password database_name 'state'
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
