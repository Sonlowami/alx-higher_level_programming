#!/usr/bin/python3

"""
This script prints all city objects from the database.
The name of the database and login credentials are
passed to the commandline
"""

def main():
    """"
    Delete all states contanining 'a' in their names.
    Does not execute when imported
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from model_state import State, Base
    from model_city import City
    from sys import argv

    (user, password, db) = (argv[1], argv[2], argv[3])
    
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(City, State).filter(City.state_id == State.id).all()
    [print(f"{state.name}: ({city.id}) {city.name}") for city, state in states]


if __name__=='__main__':
    main()
