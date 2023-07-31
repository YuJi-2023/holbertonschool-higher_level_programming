#!/usr/bin/python3
"""a script that takes in an argument and \
displays all values in the states table of hbtn_0e_0_usa\
where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state_name_searched = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY id;".format(state_name_searched))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
