#!/usr/bin/python3
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
    dbCommd = """SELECT * FROM states
                 WHERE name
                 LIKE '{:s}'
                 ORDER BY id ASC """.format(sys.argv[4])
    cur.execute(dbCommd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
