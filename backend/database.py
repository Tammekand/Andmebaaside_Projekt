from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from data import DBhost, DBport, DBusername, DBpassword, DBdatabase

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{DBusername}:{DBpassword}@{DBhost}:{DBport}/{DBdatabase}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()