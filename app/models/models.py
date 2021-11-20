from typing import Optional
from pydantic import BaseModel
from beanie import Document


class Request(BaseModel):
    firstName: str
    lastName: str
    email: str
    phoneNumber: Optional[str]
    title: str                          
    description: Optional[str] = None   


class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    phoneNumber: Optional[str]


class Reservation(Document):                        
    description: Optional[str]
    user: User
    status: str
    checkInDate: str
    checkOutDate: str

    class Collection:
        name="reservations"



 

