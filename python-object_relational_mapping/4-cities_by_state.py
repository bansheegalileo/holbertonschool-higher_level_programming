#!/usr/bin/python3
"""
 Module that lists cities from d8ab8se.
"""
import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = """SELECT  cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id"""
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
