from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
from funcs.config import get_database_connection_string


Base = declarative_base()

def setup_database_engine_into_session_generator(config: configparser.ConfigParser):
    engine = create_engine(
                get_database_connection_string(config),
                connect_args={"check_same_thread": False}
            )
    Base.metadata.create_all(bind=engine)
    Session_generator = sessionmaker()
    Session_generator.configure(bind=engine)

    return Session_generator