from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import reservations
from .models.models import User, Reservation
from .db.db import init



app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    reservations.router,
    prefix=("/api/v1")
    )


@app.on_event("startup")
async def app_init():
    await init()





