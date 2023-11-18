#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument """

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1],
                     passwd=argv[2], db=argv[3], port=3306)
cur = db.cursor()

cur.execute("""SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC""")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
