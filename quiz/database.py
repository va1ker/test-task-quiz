from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from quiz import core

engine = create_engine(core.settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
