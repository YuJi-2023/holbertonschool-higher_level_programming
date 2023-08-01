#!/usr/bin/python3
"""lists all State objects contain the letter a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # connecting
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                                sys.argv[1],
                                                                sys.argv[2],
                                                                sys.argv[3]),
                           echo=False)
    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # perform query
    a_state = session.query(State).filter(State.name.like('%a%'))

    # display states
    for state in a_state:
        print(f"{state.id}: {state.name}")

    # close the session
    session.close()
