#!/usr/bin/python3
"""using a state as an argument and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    # make a connection
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # get a cursor object
    cur = db.cursor()
    # execute queries
    cur.execute("SELECT cities.name\
                FROM cities\
                LEFT JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (sys.argv[4],))
    # obtain results
    cities = cur.fetchall()
    # clean up
    cur.close()
    db.close()
    # convert tuple objects into str
    city_name = ', '.join(str(city[0]) for city in cities)
    print(city_name)
