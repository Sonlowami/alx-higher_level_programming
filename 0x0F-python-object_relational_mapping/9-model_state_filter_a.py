#!/usr/bin/python3

"""
This Script prints all state objects in the
database that contains a letter 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base


def main():
    """This function does not runn when imported"""
    (user, password, db) = (argv[1], argv[2], argv[3])

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    [print(f"{state.id}: {state.name}") for state in states]


if __name__ == '__main__':
    main()
