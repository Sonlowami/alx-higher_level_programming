#!/usr/bin/python3
""" 
Print all states from a database using python's
MySQLdb API
"""
import MySQLdb
from sys import argv

def main():
    """
    Show all states stored in a database
    """
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states;')
    res = cur.fetchall()
    for item in res:
        print(item)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
