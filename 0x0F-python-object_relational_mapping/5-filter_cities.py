#!/usr/bin/python3
"""Find all cities in the database belonging
to a certain state
"""
import MySQLdb
from sys import argv

def main():
    """ 
    Search the database for all cities belonging to a user provided
    state. This is free from SQL injection
    """
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
        cur = db.cursor()
        cur.execute(f"SELECT DISTINCT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name LIKE BINARY %s ORDER BY cities.name;", (str(argv[4]), ))
        print(", ".join(str(item) for row in cur for item in row))
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(e)


if __name__=="__main__":
    main()
