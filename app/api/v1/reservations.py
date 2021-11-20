from fastapi import APIRouter, Form, Depends, Request
from typing import Optional
from ...models.models import Reservation, User 
from ...models.reservations import ReservationFormIn

router = APIRouter()



@router.get("/reservations")
async def list_reservation():
    return await Reservation.find_all().to_list()

@router.get("/reservations/{reservation_id}")
async def find_reservation(reservation_id: str):
    return await Reservation.get(reservation_id)

@router.post("/reservations")
async def add_reservation(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    phone_number: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    checkindate: str = Form(...),
    checkoutdate: str = Form(...),
    ):
    print(first_name, last_name, email, phone_number, description, checkindate, checkoutdate)
    user = User(firstName=first_name, lastName=last_name, email=email, phoneNumber=phone_number)
    reserv = Reservation(description=description, checkInDate=checkindate, checkOutDate=checkoutdate, user=user, status="Pending")
    print(await reserv.insert())
    return {"status": "success"}

@router.put("/reservations/{reservation_id}")
async def update_reservation(reservation_id: str, status: str = Form(...)):
    reserv = await Reservation.get(reservation_id)
    reserv.status = status
    return await reserv.save()



