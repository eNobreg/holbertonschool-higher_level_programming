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

    states = session.query(State).order_by(State.id)\
                    .filter(State.name == sys.argv[4]).all()
    for state in states:
        print("%i" % (state.id,))

    session.close()
