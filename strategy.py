import ta

def generate_signal(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    if df['rsi'].iloc[-1] < 30 and df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]:
        return 'buy'
    elif df['rsi'].iloc[-1] > 70 and df['macd'].iloc[-1] < df['macd_signal'].iloc[-1]:
        return 'sell'
    return 'hold'
