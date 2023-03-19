#!/usr/bin/python3

"""
This script returns the first state in the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import State, Base
from sys import argv

def main():
    """This function returns the first state in the database
    and does not execute when imported.
    """
    (user, password, db) = (argv[1], argv[2], argv[3])
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).first()
    print(f"{first.id}: {first.name}")


if __name__=='__main__':
    main()
