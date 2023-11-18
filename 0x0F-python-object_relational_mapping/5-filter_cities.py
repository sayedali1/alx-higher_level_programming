#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (argv[4],))

    rows = cur.fetchall()

    output = [row[0] for row in rows]

    print(*output, sep=", ")

    cur.close()
    db.close()
