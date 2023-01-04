#!/usr/bin/python3
"""Find all cities in the database"""
import MySQLdb
from sys import argv

def main():
    """ 
    Search the database for all cities and their respective states
    """
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
        cur = db.cursor()
        cur.execute(f"SELECT DISTINCT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")
        for item in cur.fetchall():
            print(item)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__=="__main__":
    main()
