#!/usr/bin/python3
"""
 Module that does the same as 2 but MYSQL safe.
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
    search = sys.argv[4]
    cur.execute("""SELECT id,name FROM states where name = %s
                ORDER by id ASC""", (search,))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
