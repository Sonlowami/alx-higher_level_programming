#!/usr/bin/python3
"""Find all table values that meet certain criteria"""
import MySQLdb
from sys import argv

try:
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{argv[4]}' ORDER BY id")
    for item in cur.fetchall():
        print(item)
    cur.close()
    db.close()
except MySQLdb.Error as e:
    print(e)
