import config as cfg
from loader.data_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_conn():
    database_location = cfg.database_location
    print(f"Creating a connection to the database: {database_location}")
    engine = create_engine(database_location)
    Base.metadata.create_all(engine)
    return engine

def access_db(engine):
    # Access data via a session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session