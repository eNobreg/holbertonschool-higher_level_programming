#!/usr/bin/python3
# Comment
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import (create_engine)
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        if 'a' in state.name:
            print("%i: %s" % (state.id, state.name,))

    session.close()
