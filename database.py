from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client[os.getenv("DATABASE_NAME")]

# DB FUNCTIONS
async def get_last_candle(symbol:str,timeframe:str):
    return await db.candlesticks.find_one({"symbol":symbol,"timeframe":timeframe},sort=[("createdAt",-1)])