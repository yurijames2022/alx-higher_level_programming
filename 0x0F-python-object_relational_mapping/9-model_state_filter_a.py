#!/usr/bin/python3
'''
A script that prints the first state object
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    db_url = 'mysql://{}:{}@localhost:3306/{}'.\
        format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    astates = session.query(State).filter(State.name.like('%a%')).all()
    for astate in astates:
        print('{}: {}'.format(astate.id, astate.name))
