#!/usr/bin/python3
"""changes the name of a State object"""
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

    # perform update object
    session.query(State).\
        filter(State.id == 2).\
        update({State.name: 'New Mexico'})

    session.commit()
    # close session
    session.close()
