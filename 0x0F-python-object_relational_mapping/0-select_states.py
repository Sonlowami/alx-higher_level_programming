#!/usr/bin/python3

"""
This script shows all entries in table 'states'
in a particular database. The name of the database
and the authentication information are passed on the
commandline
"""


def main():
    """
    This function does not execute when imported
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states;")
    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
