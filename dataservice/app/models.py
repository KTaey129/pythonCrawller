from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String)
    departure = Column(String)
    arrival = Column(String)
    departure_time = Column(String)
    price = Column(String)