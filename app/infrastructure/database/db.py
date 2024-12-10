from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config


DATABASE_URL = config.DB_URL

read_engine = create_engine(DATABASE_URL, echo=True)
sessionLocal = sessionmaker(bind=read_engine, autoflush=False, autocomit=False)

Base = declarative_base()


def get_db() -> Generator:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()