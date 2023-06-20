#!/usr/bin/python3
'''
Prints City objects from the database
'''
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    db_url = 'mysql://{}:{}@localhost:3306/{}'.\
        format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
