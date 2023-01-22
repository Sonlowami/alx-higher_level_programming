#!/usr/bin/python3
"""
This script lists all records in a States table matching the search
term provided by the user"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Print all records in the state table whose name is like the
    user without risking injection attacks"""
    try:
        session = Session()
        res = session.query(State.id).filter(State.name == argv[4]).all()
        if res:
            for item in res:
                print(item[0])
        else:
            print("Not found")
    except IndexError:
        pass


if __name__=="__main__":
    main()
