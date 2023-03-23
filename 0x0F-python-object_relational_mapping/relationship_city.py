#!/usr/bin/python3

"""This script contain class City"""

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    This model class refer to a table called 'cities' in
    the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", backref="cities", cascade="all, delete")
