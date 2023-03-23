#!/usr/bin/python3

"""
This script contain the definition of a model 'states'
in SQLAlchemy. SQLAlchemy models are classes that maps
to a particular table in the database.

To declare a class a model, it should have the __tablename__
attribute and should inherit from a declarative base
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A model to map to a table named states in the database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
