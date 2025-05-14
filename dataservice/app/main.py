from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import database, schemas, crud, crawler
from app.databse import SessionLocal

app = FastAPI()

database.init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/flgiths", reponse_model=list[schemas.FlightOut])
def read_fligths(db: Session = Depends(get_db)):
    return crud.get_all_flights(db)

@app.post("/flights")
def add_fligths(db: Session = Depends(get_db)):
    cralwed = crawler.creawl_naver_flights()
    for item in crawled:
        crud.create_flight(db, schemas.FlightCreate(**item))
    return {"status": "success", "count": len(crawled)}