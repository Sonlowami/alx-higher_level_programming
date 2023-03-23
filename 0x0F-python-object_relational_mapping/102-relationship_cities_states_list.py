#!/usr/bin/python3

"""
This module creates a state and lists all cities in
database given on the commandline
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


def main():
    """This function does not run when imported"""
    (user, password, db) = (argv[1], argv[2], argv[3])

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City).all()
    [print(f"{city.id}: {city.name} -> {city.state.name}") for city in results]


if __name__ == '__main__':
    main()
