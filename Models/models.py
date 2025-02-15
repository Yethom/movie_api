from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    release_date = Column(Date)
    overview = Column(String)
    ratings = Column(Float)

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    media_type = Column(String)
    gender = Column(Integer)
    popularity = Column(Float)


