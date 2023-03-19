#!/usr/bin/python3

"""
This Script prints a state object that matches the
user's search query, while being shielded against
SQL injection attacks
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv
from model_state import State, Base

def main():
    """This function does not runn when imported"""
    (user, password, db, search) = (argv[1], argv[2], argv[3], argv[4])

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(search))
    [print(f"{state.id}") for state in states]
    if not states.first():
        print("Not Found")


if __name__=='__main__':
    main()
