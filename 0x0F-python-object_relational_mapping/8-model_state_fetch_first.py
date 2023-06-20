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
    first_state = session.query(State).first()
    print('{}: {}'.format(first_state.id, first_state.name))
