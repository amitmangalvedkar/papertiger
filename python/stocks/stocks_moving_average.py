import yfinance as yf
import pandas as pd

def get_stocks_ma_comparison(stock_symbols, short_term_ma_period = 5, short_term_ma_term = 'MA5', 
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

        if pd.notna(latest_short_term) and pd.notna(latest_long_term) and latest_short_term > latest_long_term:
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

nifty_stock_symbols = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'TCS.NS',
    'HINDUNILVR.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS', 'SBIN.NS',
    'BHARTIARTL.NS', 'ASIANPAINT.NS', 'HCLTECH.NS', 'BAJFINANCE.NS', 'MARUTI.NS',
    'AXISBANK.NS', 'SUNPHARMA.NS', 'ULTRACEMCO.NS', 'TITAN.NS', 'NESTLEIND.NS',
    'TATAMOTORS.NS', 'POWERGRID.NS', 'ONGC.NS', 'ADANIPORTS.NS', 'NTPC.NS',
    'JSWSTEEL.NS', 'GRASIM.NS', 'TATASTEEL.NS', 'BPCL.NS', 'COALINDIA.NS',
    'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'HEROMOTOCO.NS', 'HDFCLIFE.NS',
    'INDUSINDBK.NS', 'BAJAJFINSV.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'SHREECEM.NS',
    'ADANIENT.NS', 'APOLLOHOSP.NS', 'BAJAJ-AUTO.NS', 'SBILIFE.NS', 'TATACONSUM.NS',
    'TECHM.NS', 'UPL.NS', 'WIPRO.NS', 'HINDALCO.NS', 'ICICIPRULI.NS'
]

stocks = get_stocks_ma_comparison(nifty_stock_symbols, 5, 'MAS5', 20, 'MAS20')
print("Selected Stocks with Moving Averages (5MA > 20MA):")
print(stocks)


stocks = get_stocks_ma_comparison(nifty_stock_symbols, 50, 'MAS50', 200, 'MAS200')
print("Selected Stocks with Moving Averages (50MA > 200MA):")
print(stocks)
