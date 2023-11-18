#!/usr/bin/python3
""" create states table """

from sqlalchemy import INTEGER, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State definition """

    __tablename__ = "states"

    id = Column(INTEGER, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
