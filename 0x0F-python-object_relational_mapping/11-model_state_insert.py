#!/usr/bin/python3
"""
This script adds an entry to the table states"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)

def main():
    """Adds Luisiana to the table 'states'"""
    new = State(name = "Luisiana")
    session = Session()
    session.add(new)
    session.commit()
    print(new.id)


if __name__=="__main__":
    main()
