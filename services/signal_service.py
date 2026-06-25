from services.scoring import (score_rsi, score_rsi_current,
                              score_atr, score_atr_current,
                              score_distances, score_distances_current,
                              score_spreads, score_spreads_current,
                              score_structure, score_candle_body,
                              get_trend_and_signal, score_ema_above)
from database import (get_last_candle, get_last_five_candles)


async def analyze_by_last(symbol, timeframe):
    candle = await get_last_candle(symbol, timeframe)
    if not candle:
        return {"error": "No Candle Found!"}

    candle["_id"] = str(candle["_id"])
    
    strength = 0

    rsi_values = candle["indicators"]["rsi"]
    ema20_distances = candle["distances"]["ema20"]
    ema50_distances = candle["distances"]["ema50"]
    ema200_distances = candle["distances"]["ema200"]
    ema9Above20 = candle["trend"]["ema9Above20"]
    ema20Above50 = candle["trend"]["ema20Above50"]
    ema50Above200 = candle["trend"]["ema50Above200"]
    ema9_20spread = candle["trend"]["ema9_20spread"]
    ema20_50spread = candle["trend"]["ema20_50spread"]
    ema50_200spread = candle["trend"]["ema50_200spread"]
    candle_body = candle["candle"]["bodyPercent"]
    atr_percent = candle["indicators"]["atrPercent"]

    strength += score_ema_above(ema9Above20, ema20Above50, ema50Above200)
    strength += score_rsi_current(rsi_values)
    strength += score_atr_current(atr_percent)
    strength += score_distances_current(ema20_distances, ema50_distances, ema200_distances)
    strength += score_spreads_current(ema9_20spread, ema20_50spread, ema50_200spread)
    strength += score_candle_body(candle_body)

    trend, signal = get_trend_and_signal(strength)

    return {
        "SYMBOL": symbol,
        "STRENGTH": strength,
        "TREND": trend,
        "SIGNAL": signal
    }



async def analyze_by_last_five(symbol, timeframe):
    candles = await get_last_five_candles(symbol, timeframe)
    if len(candles) < 5:
        return 0
    
    strength = 0
    bull_count = 0

    rsi_values = [
        c["indicators"]["rsi"]
        for c in candles
    ]
    ema20_distances_values = [
        c["distances"]["ema20"]
        for c in candles
    ]
    ema50_distances_values = [
        c["distances"]["ema50"]
        for c in candles
    ]
    ema200_distances_values = [
        c["distances"]["ema200"]
        for c in candles
    ]
    ema9_20spread_values = [
        c["trend"]["ema9_20Spread"]
        for c in candles
    ]
    ema20_50spread_values = [
        c["trend"]["ema20_50Spread"]
        for c in candles
    ]
    ema50_200spread_values = [
        c["trend"]["ema50_200Spread"]
        for c in candles
    ]
    atr_percent_values = [
        c["indicators"]["atr14"] / c["prices"]["close"] * 100
        for c in candles
    ]
    bull_count = sum(
    1
    for c in candles
    if c["prices"]["close"] > c["prices"]["open"])
    highs = [
        c["prices"]["high"] for c in candles
    ]
    lows = [
        c["prices"]["low"] for c in candles
    ]
    last_three_bull = all(
        c["prices"]["close"] > c["prices"]["open"]
        for c in candles[-3:]
    )
    last_three_bear = all(
        c["prices"]["close"] < c["prices"]["open"]
        for c in candles[-3:]
    )

    required_lists = [
        rsi_values, ema20_distances_values, ema50_distances_values, ema200_distances_values, ema9_20spread_values, ema20_50spread_values, ema50_200spread_values
    ]
    for values in required_lists:
        if any(v is None for v in values):
            return 0
    

    strength += score_rsi(rsi_values)
    strength += score_distances(ema20_distances_values, ema50_distances_values, ema200_distances_values)
    strength += score_spreads(ema9_20spread_values, ema20_50spread_values, ema50_200spread_values)
    strength += score_atr(atr_percent_values)
    strength += score_structure(bull_count, highs, lows, last_three_bull, last_three_bear)

    trend, signal = get_trend_and_signal(strength)

    return {
        "SYMBOL": symbol,
        "STRENGTH": strength,
        "TREND": trend,
        "SIGNAL": signal
    }