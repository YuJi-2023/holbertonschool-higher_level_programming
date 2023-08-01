#!/usr/bin/python3
"""adds the State object Louisiana to the database"""
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

    # perform add object
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # display states
    print(new_state.id)

    # close the session
    session.close()
