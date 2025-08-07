import alpaca_trade_api as tradeapi
import pandas as pd
from config import API_KEY, SECRET_KEY, BASE_URL
from strategy import generate_signal
import datetime

def get_data(symbol, limit=100):
    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
    barset = api.get_bars(symbol, '1h', limit=limit).df
    return barset[barset['symbol'] == symbol]

def trade(symbol='AAPL'):
    df = get_data(symbol)
    signal = generate_signal(df)
    print(f"[{datetime.datetime.now()}] Signal for {symbol}: {signal}")

    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
    if signal == 'buy':
        api.submit_order(symbol=symbol, qty=1, side='buy', type='market', time_in_force='gtc')
    elif signal == 'sell':
        api.submit_order(symbol=symbol, qty=1, side='sell', type='market', time_in_force='gtc')
