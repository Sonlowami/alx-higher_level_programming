#!/usr/bin/python3
"""
This script lists all cities in the database given
at the commandline. Authentication details are also
passed at the commandline
"""


def main():
    """
    This function lists all cities from a database.
    It does not execute when imported
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
            states ON cities.state_id = states.id ORDER BY cities.id ASC;")

    [print(item) for item in cur.fetchall()]
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
