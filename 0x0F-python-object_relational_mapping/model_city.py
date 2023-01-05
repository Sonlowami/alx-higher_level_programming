#!/usr/bin/python3
"""
This script creates a model class called City that
will map to the database table"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from model_state import State


Base = declarative_base()

def City(Base):
    """
    Create model class 'City' that maps to table 'cities'
    via the declarative base 'Base'"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
    state = relationship("State", backref="cities")


engine = create_engine("mysql+myslqdb://root:root@localhost:3306/{}".format(argv[4]))
Base.metadata.create_all(engine)
