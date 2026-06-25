from fastapi import APIRouter
from services.signal_service import analyze_by_last_five, analyze_by_last

router = APIRouter(
    prefix="/api",
    tags=["Candlesticks"]
)

@router.get('/')
async def root():
    return {"message": "API SIGNAL!"}

@router.get('/signal/by/last')
async def get_signal(symbol:str,timeframe:str):
    result = await analyze_by_last(symbol, timeframe)
    return result


@router.get('/signal/by/lastfive')
async def get_signal_by_last_five(symbol: str, timeframe: str):
    result = await analyze_by_last_five(symbol, timeframe)
    return result