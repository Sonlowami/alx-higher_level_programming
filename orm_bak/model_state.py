#!/usr/bin/python3
"""
This module contain classes whose objects
are mapped to database tables by declarative_base
objects
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()


class States(Base):
    """Define objects of type states that
    are mapped toa table called states in the database
    """
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa")
Base.metadata.create_all(engine)
