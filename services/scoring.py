# function for last candle
def score_ema_above(ema9Above20, ema20Above50, ema50Above200):
    score = 0
    if ema9Above20 is not None:
        if ema9Above20:
            strength += 20
        if ema20Above50:
            strength += 30
        if ema50Above200:
            strength += 50
    return score

def score_rsi_current(rsi_values):
    score = 0

    if rsi_values < 20:
        score += 25
    elif rsi_values < 30:
        score += 15
    elif rsi_values < 40:
        score += 5
    elif rsi_values < 60:
        pass
    elif rsi_values < 70:
        score += 5
    elif rsi_values < 80:
        score += 10
    else:
        score += 5

    return score


def score_distances_current(ema20_distances, ema50_distances, ema200_distances):
    score = 0
    if ema20_distances is not None: 
        if ema20_distances < -10:
            score -= 25
        elif ema20_distances < -5:
            score -= 15
        elif ema20_distances < 0:
            score -= 5
        elif ema20_distances < 3:
            score += 5
        elif ema20_distances < 7:
            score += 10
        else:
            score -= 5

    if ema50_distances is not None:
        if ema50_distances < 0:
            score -= 15
        elif ema50_distances < 5:
            score += 10
        elif ema50_distances < 15:
            score += 20
        else:
            score += 5
    
    if ema200_distances is not None:
        if ema200_distances < -10:
            score -= 50
        elif ema200_distances < 0:
            score -=20
        elif ema200_distances < 20:
            score += 20
        else:
            score += 40

    return score


def score_spreads_current(ema9_20spread, ema20_50spread, ema50_200spread):
    score = 0

    if ema9_20spread is not None:
        if ema9_20spread < -2:
            score -= 15
        elif ema9_20spread < 0:
            score -= 5
        elif ema9_20spread < 2:
            score += 5
        else:
            score += 15

    if ema20_50spread is not None:
        if ema20_50spread < -2:
            score -= 20
        elif ema20_50spread < 0:
            score -= 10
        elif ema20_50spread < 2:
            score += 10
        else:
            score += 20

    if ema50_200spread is not None:
        if ema50_200spread < -5:
            score -= 30
        elif ema50_200spread < 0:
            score -= 15
        elif ema50_200spread < 5:
            score += 15
        else:
            score += 30

    return score

def score_atr_current(atr_percent):
    score = 0

    if atr_percent is not None:
        if atr_percent < 0.3:
            score -= 20
        elif atr_percent < 1:
            score -= 5
        elif atr_percent < 5:
            score += 10
        else:
            score += 5
            
    return score

def score_candle_body(candle_body):
    score = 0
    if candle_body is not None:
        if candle_body > 3:
            score += 10
        elif candle_body > 1:
            score += 5
    return score

# functions for five candles
def score_rsi(rsi_values):
    score = 0

    rsi_change = rsi_values[-1] - rsi_values[0]

    if rsi_change > 20:
        score += 20
    elif rsi_change > 10:
        score += 10
    elif rsi_change > 5:
        score += 5
    elif rsi_change < -20:
        score -= 20
    elif rsi_change < -10:
        score -= 10
    elif rsi_change < -5:
        score -= 5

    return score

def score_distances(ema20_distances_values, ema50_distances_values, ema200_distances_values):
    score = 0
    ema20_distance_change = ema20_distances_values[-1] - ema20_distances_values[0]
    ema50_distance_change = ema50_distances_values[-1] - ema50_distances_values[0]
    ema200_distance_change = ema200_distances_values[-1] - ema200_distances_values[0]
    if ema20_distance_change < -10:
        score -= 25
    elif ema20_distance_change < -5:
        score -= 15
    elif ema20_distance_change < -0:
        score -= 5
    elif ema20_distance_change < 3:
        score += 5
    elif ema20_distance_change < 7:
        score += 15
    elif ema20_distance_change < 15:
        score += 20
    else:
        score += 5

    if ema50_distance_change < -15:
        score -= 35
    elif ema50_distance_change < -5:
        score -= 20
    elif ema50_distance_change < -0:
        score -= 10
    elif ema50_distance_change < 5:
        score += 10
    elif ema50_distance_change < 15:
        score += 20
    elif ema50_distance_change < 30:
        score += 30
    else:
        score += 10


    
    if ema200_distance_change < -20:
        score -= 60
    elif ema200_distance_change < -10:
        score -= 40
    elif ema200_distance_change < -0:
        score -= 20
    elif ema200_distance_change < 10:
        score += 15
    elif ema200_distance_change < 25:
        score += 30
    elif ema200_distance_change < 50:
        score += 45
    else:
        score += 20

    return score

def score_spreads(ema9_20spread_values, ema20_50spread_values, ema50_200spread_values):
    score = 0
    ema9_20spread_change = ema9_20spread_values[-1] - ema9_20spread_values[0]
    ema20_50spread_change = ema20_50spread_values[-1] - ema20_50spread_values[0]
    ema50_200spread_change = ema50_200spread_values[-1] - ema50_200spread_values[0]
    if ema9_20spread_change < -3:
        score -= 20
    elif ema9_20spread_change < -1:
        score -= 10
    elif ema9_20spread_change < 0:
        score -= 5
    elif ema9_20spread_change < 1:
        score += 5
    elif ema9_20spread_change < 3:
        score += 10
    else:
        score += 10

    if ema20_50spread_change < -5:
        score -= 25
    elif ema20_50spread_change < -2:
        score -= 15
    elif ema20_50spread_change < 0:
        score -= 5
    elif ema20_50spread_change < 2:
        score += 5
    elif ema20_50spread_change < 5:
        score += 15
    else:
        score += 25

    if ema50_200spread_change < -10:
        score -= 40
    elif ema50_200spread_change < -5:
        score -= 25
    elif ema50_200spread_change < 0:
        score -= 10
    elif ema50_200spread_change < 5:
        score += 10
    elif ema50_200spread_change < 15:
        score += 25
    elif ema50_200spread_change < 30:
        score += 40
    else:
        score += 20

    return score

def score_atr(atr_percent_values):
    score = 0
    atr_change = atr_percent_values[-1] - atr_percent_values[0]

    if atr_change > 1:
        score += 10
    elif atr_change < -1:
        score -= 10

    return score

def score_structure(bull_count, highs, lows, last_three_bull, last_three_bear):
    score = 0
    if bull_count == 5:
        score += 20
    elif bull_count == 4:
        score += 10
    elif bull_count == 1:
        score -= 10
    elif bull_count == 0:
        score -= 20

    if highs[4] > highs[3] > highs[2] > highs[1]:
        score += 15
    
    if lows[4] < lows[3] < lows[2] < lows[1]:
        score -= 15

    if last_three_bull:
        score += 15
    if last_three_bear:
        score -= 15

    return score



# Trend & Signal
def get_trend_and_signal(strength):

    if strength < -80:
        return "VERY_STRONG_BEARISH", "VERY_STRONG_SELL"

    elif strength < -40:
        return "STRONG_BEARISH", "STRONG_SELL"

    elif strength < 0:
        return "BEARISH", "SELL"

    elif strength < 40:
        return "NEUTRAL", "HOLD"

    elif strength < 80:
        return "BULLISH", "BUY"

    elif strength < 120:
        return "STRONG_BULLISH", "STRONG_BUY"

    return "VERY_STRONG_BULLISH", "VERY_STRONG_BUY"