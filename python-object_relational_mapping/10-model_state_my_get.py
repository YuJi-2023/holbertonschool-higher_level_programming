#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
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
    s_state = session.query(State).filter(State.name == sys.argv[4]).first()

    # display states
    if s_state:
        print(s_state.id)
    else:
        print(f"Not found")

    # close the session
    session.close()
