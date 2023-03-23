#!/usr/bin/python3

"""
This script deletes all state objects containing
letter 'a' from a database. The name of the database and
login credentials are passed to the commandline
"""


def main():
    """"
    Delete all states contanining 'a' in their names.
    Does not execute when imported
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from sys import argv

    (user, password, db) = (argv[1], argv[2], argv[3])

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    [session.delete(state) for state in states]
    session.commit()


if __name__ == '__main__':
    main()
