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
    dbComd = """SELECT * FROM states WHERE name = %s ORDER BY id ASC """
    cur.execute(dbComd, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
