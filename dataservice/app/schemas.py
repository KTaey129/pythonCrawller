from pydantic import BaseModel

class FlightCreate(BaseModel):
    airline: str
    departure: str
    arrival: str
    departure_time: str
    price: str

class FlightOut(FlightCreate):
    id: int

    class Config:
        orm_mode = True