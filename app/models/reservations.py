from typing import Optional
from pydantic import BaseModel

class ReservationFormIn(BaseModel):
    first_name: str 
    last_name: str 
    email: str
    phone_number: Optional[str]
    title: str
    descritpion: Optional[str]