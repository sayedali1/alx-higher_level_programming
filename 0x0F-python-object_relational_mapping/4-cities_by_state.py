#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
name = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=name)
    cur = db.cursor()
    dbcomd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cur.execute(dbcomd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
