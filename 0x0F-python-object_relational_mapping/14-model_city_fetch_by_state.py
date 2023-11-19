#!/usr/bin/python3
"""A python script  that prints all City objects from the
database hbtn_0e_14_usa:"""


if __name__ == '__main__':

    import sys
    from model_city import City
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, relationship

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id.asc()).all()
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
