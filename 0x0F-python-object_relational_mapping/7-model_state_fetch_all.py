#!/usr/bin/python3
"""
This script lists all records in a States table"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Print all records in te state table"""
    try:
        session = Session()
        res = session.query(State.id, State.name).order_by(State.id).all()
        for item in res:
            print("{}: {}".format(item.id, item.name))
    except IndexError:
        pass


if __name__=="__main__":
    main()
