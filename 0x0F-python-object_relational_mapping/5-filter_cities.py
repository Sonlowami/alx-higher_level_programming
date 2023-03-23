#!/usr/bin/python3

"""
This script shows all cities that belong to a user-
specified state. The name of the state, database, and
authentication are passed on the commandline
"""


def main():
    """
    This function shows all cities belonging to a state.
    It does not execute when imported.
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute(
            """SELECT cities.name FROM cities JOIN states\
               ON cities.state_id = states.id WHERE states.name = %(state)s\
               ORDER BY cities.id""", {'state': argv[4]})
    cities = []
    [cities.append(item) for items in cur.fetchall() for item in items]
    print(', '.join(city for city in cities))
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
