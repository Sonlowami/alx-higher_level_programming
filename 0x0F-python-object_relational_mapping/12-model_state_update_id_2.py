#!/usr/bin/python3

"""
This script updates state object with id = 2 to New Mexico.
The database name, along with the authentication
details are passed to the commandline
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv
from model_state import State, Base

def main():
    """This function does not runn when imported"""
    (user, password, db) = (argv[1], argv[2], argv[3])

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.add(state)
    session.commit()


if __name__=='__main__':
    main()
