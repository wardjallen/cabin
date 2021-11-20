
import motor
from beanie import init_beanie
from pydantic import BaseSettings
from ..models.models import Reservation


class Settings(BaseSettings):
    mongo_host: str = "cluster0.yvh3i.mongodb.net"
    mongo_user: str = "dbuser"
    mongo_pass: str = "FeNzTThb6SWvhtuM"
    mongo_db: str = "cabin"
    
    @property
    def mongo_dsn(self):
       return f"mongodb+srv://{self.mongo_user}:{self.mongo_pass}@{self.mongo_host}/{self.mongo_db}?retryWrites=true&w=majority"

async def init():
    # Crete Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient(Settings().mongo_dsn)

    # Init beanie with the Product document class
    await init_beanie(database=client.cabin, document_models=[Reservation])

