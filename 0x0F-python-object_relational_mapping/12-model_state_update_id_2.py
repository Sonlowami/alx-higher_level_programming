#!/usr/bin/python3
"""
This script updates a table entry"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Updates a table entryi with primary_key of 2"""
    session = Session()
    new = session.query(State).get(2)
    new.name = "New Mexico"
    session.add(new)
    session.commit()

if __name__=="__main__":
    main()
