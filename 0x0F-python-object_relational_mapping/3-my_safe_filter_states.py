#!/usr/bin/python3

"""
This script searches the table called 'states' in a particular
database for a user generated query. The name of the database,
the search term, and authentication credentials are passed on
the commandline.

This query is secured from SQL Injection attacks
"""


def main():
    """
    This function does not run when imported
    """

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY ( %s );",
            (str(argv[4]), ))

    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
