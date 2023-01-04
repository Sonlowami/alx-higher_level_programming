#!/usr/bin/python3
"""Find all table values that meet certain criteria"""
import MySQLdb
from sys import argv


def main():
    """
    Find all databasse entries that meets the input provided
    by the user. This is protected from SQL injection attacks
    """
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE ( %s ) ORDER BY id;", (str(argv[4]), ))
        for item in cur.fetchall():
            print(item)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__=="__main__":
    main()
