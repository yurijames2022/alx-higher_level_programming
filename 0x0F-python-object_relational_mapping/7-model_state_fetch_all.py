#!/usr/bin/python3
'''
A script that lists all State Objects from the db
'''
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
        format(username, password, db_name)

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
