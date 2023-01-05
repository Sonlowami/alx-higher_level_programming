#!/usr/bin/python3
"""
This script lists all records in a States table matching the search
term provided by the user"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Print all records in the state table whose name is like the
    user without risking injection attacks"""
    session = Session()
    res = session.query(State.name, City.id, City.name).join(State).all()
    for item in res:
        print("{}: ({}) {}".format(item.name, item.id, item.name))

if __name__=="__main__":
    main()
