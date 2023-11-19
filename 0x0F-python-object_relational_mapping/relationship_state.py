#!/usr/bin/python3
""" create states table """

from sqlalchemy import INTEGER, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """ State definition """

    __tablename__ = "states"

    id = Column(INTEGER, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")
