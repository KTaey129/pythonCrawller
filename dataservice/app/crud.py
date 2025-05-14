from sqlalchemy.orm import Session
from app import models, schemas

def create_flight(db: Session, fligth: schemas.FlightCreate):
    db_flight = models.Flight(**flight.dict)
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

def get_all_flights(db: Session):
    return db.query(models.Flight).all()