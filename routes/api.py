from fastapi import APIRouter
from database import get_last_candle


router = APIRouter(
    prefix="/api",
    tags=["Candlesticka"]
)

@router.get('/')
async def root():
    return {"message": "API SIGNAL!"}

@router.get('/signal')
async def get_signal(symbol:str,timeframe:str):
    candle = await get_last_candle(symbol,timeframe)
    
    if not candle:
        return {"error": "No Candle Found!"}
    candle["_id"] = str(candle["_id"])
    
    candle_trend = candle["trend"]
    candle_rsi = candle["indicators"]["rsi"]
    candle_distances = candle["distances"]
    candle_body = candle["candle"]["bodyPercent"]
    atr_percent = candle["indicators"]["atrPercent"]
    # STRENGTH
    strength = 0

    # EMA ABOVE
    if candle_trend["ema9Above20"]:
        strength += 20
    if candle_trend["ema20Above50"]:
        strength += 30
    if candle_trend["ema50Above200"]:
        strength += 50

    # RSI
    if candle_rsi < 20:
        strength += 25
    elif candle_rsi < 30:
        strength += 15
    elif candle_rsi < 40:
        strength += 5
    elif candle_rsi < 60:
        pass
    elif candle_rsi < 70:
        strength += 5
    elif candle_rsi < 80:
        strength += 10
    else:
        strength += 5

    # EMA DISTANCE
    if candle_distances["ema20Distance"] is not None: 
        if candle_distances["ema20Distance"] < -10:
            strength -= 25
        elif candle_distances["ema20Distance"] < -5:
            strength -= 15
        elif candle_distances["ema20Distance"] < 0:
            strength -= 5
        elif candle_distances["ema20Distance"] < 3:
            strength += 5
        elif candle_distances["ema20Distance"] < 7:
            strength += 10
        else:
            strength -= 5

    if candle_distances["ema50Distance"] is not None:
        if candle_distances["ema50Distance"] < 0:
            strength -= 15
        elif candle_distances["ema50Distance"] < 5:
            strength += 10
        elif candle_distances["ema50Distance"] < 15:
            strength += 20
        else:
            strength += 5
    
    if candle_distances["ema200Distance"] is not None:
        if candle_distances["ema200Distance"] < -10:
            strength -= 50
        elif candle_distances["ema200Distance"] < 0:
            strength -=20
        elif candle_distances["ema200Distance"] < 20:
            strength += 20
        else:
            strength += 40

    # EMA SPREAD
    if candle_trend["ema9_20Spread"] is not None:
        if candle_trend["ema9_20Spread"] < -2:
            strength -= 15
        elif candle_trend["ema9_20Spread"] < 0:
            strength -= 5
        elif candle_trend["ema9_20Spread"] < 2:
            strength += 5
        else:
            strength += 15

    if candle_trend["ema20_50Spread"] is not None:
        if candle_trend["ema20_50Spread"] < -2:
            strength -= 20
        elif candle_trend["ema20_50Spread"] < 0:
            strength -= 10
        elif candle_trend["ema20_50Spread"] < 2:
            strength += 10
        else:
            strength += 20

    if candle_trend["ema50_200Spread"] is not None:
        if candle_trend["ema50_200Spread"] < -5:
            strength -= 30
        elif candle_trend["ema50_200Spread"] < 0:
            strength -= 15
        elif candle_trend["ema50_200Spread"] < 5:
            strength += 15
        else:
            strength += 30

    # ATR
    if atr_percent is not None:
        if atr_percent < 0.3:
            strength -= 20
        elif atr_percent < 1:
            strength -= 5
        elif atr_percent < 5:
            strength += 10
        else:
            strength += 5


    # BODY PERCENT
    if candle_body > 3:
        strength += 10
    elif candle_body > 1:
        strength += 5

    # TREND , SIGNAL
    trend = ""
    signal = ""
    if strength < -80:
        trend = "VERY_STRONG_BEARISH"
        signal = "VERY_STRONG_SELL"
    elif strength < -40:
        trend = "STRONG_BEARISH"
        signal = "STRONG_SELL"
    elif strength < 0:
        trend = "BEARISH"
        signal = "SELL"
    elif strength < 40:
        trend = "NEUTRAL"
        signal = "HOLD"
    elif strength < 80:
        trend = "BULLISH"
        signal = "BUY"
    elif strength < 120:
        trend = "STRONG_BULLISH"
        signal = "STRONG_BUY"
    else:
        trend = "VERY_STRONG_BULLISH"
        signal = "VERY_STRONG_BUY"
    
 
    return {
        "STRENGTH": strength,
        "TREND": trend,
        "SIGNAL": signal,
    }