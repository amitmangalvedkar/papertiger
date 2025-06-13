import yfinance as yf
import pandas as pd
import numpy as np

# ✅ Step 1: Nifty 50 stock symbols (Yahoo Finance format)
nifty_50_symbols = [
    'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
    'HINDUNILVR.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS', 'SBIN.NS',
    'AXISBANK.NS', 'HCLTECH.NS', 'BHARTIARTL.NS', 'BAJFINANCE.NS', 'ASIANPAINT.NS',
    'SUNPHARMA.NS', 'MARUTI.NS', 'TITAN.NS', 'NESTLEIND.NS', 'ULTRACEMCO.NS',
    'WIPRO.NS', 'POWERGRID.NS', 'TECHM.NS', 'NTPC.NS', 'TATAMOTORS.NS',
    'JSWSTEEL.NS', 'INDUSINDBK.NS', 'BAJAJFINSV.NS', 'ADANIENT.NS', 'ADANIPORTS.NS',
    'GRASIM.NS', 'CIPLA.NS', 'HINDALCO.NS', 'BPCL.NS', 'COALINDIA.NS',
    'EICHERMOT.NS', 'BRITANNIA.NS', 'ONGC.NS', 'DIVISLAB.NS', 'HEROMOTOCO.NS',
    'DRREDDY.NS', 'TATASTEEL.NS', 'M&M.NS', 'UPL.NS', 'SBILIFE.NS',
    'HDFCLIFE.NS', 'BAJAJ-AUTO.NS', 'APOLLOHOSP.NS', 'ICICIPRULI.NS', 'SHREECEM.NS'
]

# ✅ Step 2: Download 1 year of adjusted close prices
price_data = yf.download(nifty_50_symbols, period='1y')['Close']


price_data.dropna(axis=1, inplace=True)

# ✅ Step 3: Calculate daily returns
daily_returns = price_data.pct_change().dropna()

# ✅ Step 4: Compute Sharpe Ratio for each stock
risk_free_rate = 0.07  # 7% annual
daily_rfr = risk_free_rate / 252

sharpe_ratios = {}
for stock in daily_returns.columns:
    excess_daily_return = daily_returns[stock] - daily_rfr
    sharpe = np.mean(excess_daily_return) / np.std(daily_returns[stock]) * np.sqrt(252)
    sharpe_ratios[stock] = sharpe

# ✅ Step 5: Rank stocks by Sharpe ratio
sharpe_df = pd.DataFrame.from_dict(sharpe_ratios, orient='index', columns=['Sharpe Ratio'])
sharpe_df.sort_values(by='Sharpe Ratio', ascending=False, inplace=True)

# ✅ Display top N
print("🔝 Top NIFTY50 Stocks by Sharpe Ratio:\n")
print(sharpe_df.round(2))
