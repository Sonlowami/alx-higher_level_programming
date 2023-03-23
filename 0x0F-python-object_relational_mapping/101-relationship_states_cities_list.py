#!/usr/bin/python3

"""
This module creates a state and links a city to it
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


def main():
    """This function does not runn when imported"""
    (user, password, db) = (argv[1], argv[2], argv[3])

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).all()
    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")


if __name__ == '__main__':
    main()
