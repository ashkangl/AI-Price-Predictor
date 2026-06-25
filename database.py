from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client[os.getenv("DATABASE_NAME")]

# DB FUNCTIONS
async def get_last_candle(symbol: str, timeframe: str):
    return await db.candlesticks.find_one({"symbol":symbol,"timeframe":timeframe},sort=[("createdAt",-1)])

async def get_last_five_candles(symbol: str, timeframe: str):
    candles = []
    async for candle in db.candlesticks.find({"symbol":symbol,"timeframe":timeframe},sort=[("createdAt",-1)]).limit(5):
        candle["_id"] = str(candle["_id"])
        candles.append(candle)
    candles.reverse()
    return candles