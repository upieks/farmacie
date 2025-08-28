# backend/models.py
import os
from sqlalchemy import create_engine, Column, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_recycle=3600)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class SES(Base):
__tablename__ = 'ses'
id = Column(Integer, primary_key=True)
postcode = Column(String(6), index=True)
year = Column(Integer, index=True)
data = Column(JSON)


class Healthcare(Base):
__tablename__ = 'healthcare'
id = Column(Integer, primary_key=True)
postcode = Column(String(6), index=True)
year = Column(Integer, index=True)
cost_estimate = Column(Float)
data = Column(JSON)


def init_db():
Base.metadata.create_all(engine)


def get_session():
return Session()