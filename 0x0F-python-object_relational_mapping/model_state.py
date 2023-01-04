#!/usr/bin/python3
"""
This script includes a class that uses declarative base
object to map it's attributes against columns in a table in
a database
"""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """Class state that is mapped to the table 'states' in the
    database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa")
Base.metadata.create_all(engine)
