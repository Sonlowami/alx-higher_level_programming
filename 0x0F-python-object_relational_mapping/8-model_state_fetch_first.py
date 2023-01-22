#!/usr/bin/python3
"""
This script lists the first records in a States table"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Print the first record in the state table"""
    try:
        session = Session()
        res = session.query(State.id, State.name).order_by(State.id).first()
        if res:
            print("{}: {}".format(res.id, res.name))
        else:
            print("Nothing")
    except IndexError:
        pass


if __name__=="__main__":
    main()
