#!/usr/bin/python3
# Comment
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).order_by(State.id)

    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
