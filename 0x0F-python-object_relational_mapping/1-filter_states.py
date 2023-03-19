#!/usr/bin/python3

"""
This script checks all entries in a table called states, stored
in a certaun database. The name of the database, together with
the authentication credentials are passed at the commandline
"""

def main():
    "This function does not execute when imported"""
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE ASCII(name) LIKE ASCII('N');")

    [print(item) for item in cur.fetchall()]

    cur.close()
    db.close()

if __name__=='__main__':
    main()
