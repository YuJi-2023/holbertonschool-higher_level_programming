#!/usr/bin/python3
"""lists all cities objects of the database hbtn_0e_14_usa"""
import sys
from model_state import State
from model_city import City
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
    result = session.query(City).join(State.id)

    # display cites
    for city in result:
        print(f"{State.name}: ({city.id}) {city.name}")

    # close the session
    session.commit()
