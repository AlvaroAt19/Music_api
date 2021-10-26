from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database


POSTGRES_URL = "postgresql://postgres:postgres@localhost:5432/Music" #postgresql://user:pass@localhost:port/database

if not database_exists(POSTGRES_URL): #create URL's database
        create_database(POSTGRES_URL)

engine = create_engine(POSTGRES_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()



