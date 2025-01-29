from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User
from decouple import config

# Load the MongoDB URI from environment variables
MONGO_URI = config("MONGO_URI")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    database_name = MONGO_URI.split("/")[-1].split("?")[0]
    
    db = client[database_name]
    collection = db["users"]
    
    await init_beanie(database=db, document_models=[User])
