import yfinance as yf
import pandas as pd

def get_stocks_ma_comparison(stock_symbols):

    selected_stocks = []
    stock_with_averages = [ [0]*3 for i in range(3)]

    for symbol in stock_symbols:
        data = yf.download(symbol, period='30d', interval='1d')
        if data.empty or len(data) < 20:
            continue  # skip if not enough data

        data['MA5'] = data['Close'].rolling(window=5).mean()
        data['MA20'] = data['Close'].rolling(window=20).mean()

        latest_ma5 = data['MA5'].iloc[-1]
        latest_ma20 = data['MA20'].iloc[-1]

        if pd.notna(latest_ma5) and pd.notna(latest_ma20) and latest_ma5 > latest_ma20:
            ma_diff = latest_ma5 - latest_ma20
            ma_diff_pct = (ma_diff / latest_ma20) * 100
            selected_stocks.append({
                'Symbol': symbol,
                'MA5': round(latest_ma5, 2),
                'MA20': round(latest_ma20, 2),
                'MA_Diff': round(ma_diff, 2),
                'MA_Diff_Pct': round(ma_diff_pct, 2)
            })

    df = pd.DataFrame(selected_stocks)
    if not df.empty:
        df = df.sort_values(by='MA_Diff_Pct', ascending=False).reset_index(drop=True)
    return df

stock_symbols = [
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

stocks = get_stocks_ma_comparison(stock_symbols)
print("Selected Stocks with Moving Averages (5MA > 20MA):")
print(stocks)

'''
for symbol in stocks:
    data = yf.download(symbol, period='30d', interval='1d')
    print(data)
'''
