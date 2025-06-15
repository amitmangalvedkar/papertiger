import yfinance as yf
import pandas as pd
import json

import nifty50 as nifty50

def get_moving_averages(stock_symbols, short_term_ma_period = 5, short_term_ma_term = 'MA5', 
                             long_term_ma_period = 20, long_term_ma_term = 'MA20'):

    selected_stocks = []
    stock_with_averages = [ [0]*3 for i in range(3)]

    for symbol in stock_symbols:

        #'auto_adjust = True' will suppress 'YF.download() has changed argument auto_adjust default to True'
        #'progress = False' will suppress '[*********************100%***********************]  1 of 1 completed'
        data = yf.download(symbol, auto_adjust = True, progress = False, period='30d', interval='1d')
        if data.empty or len(data) < 20:
            continue  # skip if not enough data

        data[short_term_ma_term] = data['Close'].rolling(window = short_term_ma_period).mean()
        data[long_term_ma_term] = data['Close'].rolling(window = long_term_ma_period).mean()

        latest_short_term = data[short_term_ma_term].iloc[-1]
        latest_long_term = data[long_term_ma_term].iloc[-1]

        if pd.notna(latest_short_term) and pd.notna(latest_long_term):
            ma_diff = latest_short_term - latest_long_term
            ma_diff_pct = (ma_diff / latest_long_term) * 100
            selected_stocks.append({
                'Symbol': symbol,
                short_term_ma_term: round(latest_short_term, 2),
                long_term_ma_term: round(latest_long_term, 2),
                'MA_Diff': round(ma_diff, 2),
                'MA_Diff_Pct': round(ma_diff_pct, 2)
            })

    df = pd.DataFrame(selected_stocks)
    if not df.empty:
        df = df.sort_values(by='MA_Diff_Pct', ascending=False).reset_index(drop=True)
    return df

nifty_stock_symbols = nifty50.get_nifty50_symbols()

stocks = get_moving_averages(nifty_stock_symbols, 5, 'MA5', 20, 'MA20')
print("\nSelected Stocks with Moving Averages:")
print("Bullish trend when MA5 > MA20")
print("Bearish trend when MA5 < MA20")
print(stocks)