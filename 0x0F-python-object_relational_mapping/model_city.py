#!/usr/bin/python3
# Everything
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = Column('id', Integer(), nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
