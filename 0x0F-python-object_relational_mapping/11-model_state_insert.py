#!/usr/bin/python3
"""
return all state objects from database
parameters given to script: username, password, database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    name_db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, name_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    New = State(name="Louisiana")
    session.add(New)
    session.commit()

    print("{:d}".format(New.id))
    session.close()
