import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm

import seaborn as sns
import matplotlib.pyplot as plt

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


symbols = nifty_50_symbols + ['^NSEI']  # Include NIFTY50 index

# ✅ Step 2: Download 1 year of adjusted close prices
price_data = yf.download(symbols, period='1y')['Close'].dropna()

# ✅ Step 2: Download 3 years of adjusted close prices
#price_data = yf.download(symbols, period='3y')['Close'].dropna()


# ✅ Step 3: Calculate daily returns
returns = price_data.pct_change().dropna()
market_returns = returns['^NSEI']
risk_free_rate = 0.07  # Annual risk-free rate (approx. Indian 10-yr govt bond yield)
daily_rfr = risk_free_rate / 252
market_annual_return = market_returns.mean() * 252


# ✅ Step 3: Initialize result container
results = []

# ✅ Step 4: Metrics for each stock
# ✅ Step 4: Metrics for each stock
for stock in nifty_50_symbols:
    daily_ret = returns[stock]
    annual_ret = daily_ret.mean() * 252
    annual_vol = daily_ret.std() * np.sqrt(252)

    # Excess returns
    excess_ret = daily_ret - daily_rfr
    sharpe = excess_ret.mean() / daily_ret.std() * np.sqrt(252)

    # Regression for Beta
    X = sm.add_constant(market_returns)
    model = sm.OLS(daily_ret, X).fit()
    beta = model.params[1]

    # Treynor Ratio
    treynor = (annual_ret - risk_free_rate) / beta if beta != 0 else np.nan

    # Jensen's Alpha
    expected_return_capm = risk_free_rate + beta * (market_annual_return - risk_free_rate)
    jensen_alpha = annual_ret - expected_return_capm

    try:
        pe_ratio = yf.Ticker(stock).info.get('trailingPE', np.nan)
        roe =  yf.Ticker(stock).info.get('returnOnEquity', np.nan)
        growth_rate = yf.Ticker(stock).info.get('earningsGrowth', np.nan) * 100
        peg_ratio = pe_ratio / growth_rate

    except:
        pe_ratio = peg_ratio = roe = np.nan

    results.append({
        'Stock': stock,
        'Sharpe Ratio': sharpe,
        'Beta': beta,
        'Treynor Ratio': treynor,
        'Jensen Alpha': jensen_alpha,
        'Return on Investment': roe,
        'P/E Ratio': pe_ratio,
        'Growth Rate %': growth_rate,
        'PEG Ratio': peg_ratio
    })

# ✅ Step 5: Display results
df = pd.DataFrame(results)
df.set_index('Stock', inplace=True)
df.sort_values(by='Sharpe Ratio', ascending=False, inplace=True)
print("\n🔝 Risk-adjusted Performance Metrics for NIFTY Stocks:")
print(df.round(3))


# ✅ Get Top 10 stocks by Sharpe Ratio
top10_df = df.head(10)[['Sharpe Ratio', 'Treynor Ratio', 'Jensen Alpha']]


# ✅ Normalize for better color contrast
normalized_top10 = (top10_df - top10_df.mean()) / top10_df.std()

# ✅ Plot Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(normalized_top10, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
plt.title("🔥 Top 10 NIFTY Stocks: Risk-Adjusted Metrics Heatmap")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()