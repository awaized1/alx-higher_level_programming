#!/usr/bin/python3
""" code prints first State object from db"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj_data = session.query(State).first()
    if obj_data is None:
        print("Nothing")
    else:
        print(obj_data.id, obj_data.name, sep=": ")
