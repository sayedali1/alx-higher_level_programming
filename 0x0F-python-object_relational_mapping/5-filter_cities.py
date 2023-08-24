#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    dbcomd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cur.execute(dbcomd, (sys.argv[4],))
    print(', '.join(["{:s}".format(row[0]) for row in cur.fetchall()]))
    cur.close()
    db.close()
