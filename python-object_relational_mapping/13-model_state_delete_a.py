#!/usr/bin/python3
"""deletes the State object contains a"""
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

    # perform delete object
    result = session.query(State).filter(State.name.like('%a%'))
    for state in result:
        session.delete(state)

    session.commit()
    # close the session
    session.close()
