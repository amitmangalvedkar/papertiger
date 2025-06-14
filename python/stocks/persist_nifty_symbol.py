import json

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

# Save to disk
with open('nifty_list.json', 'w') as f:
    json.dump(nifty_50_symbols, f)

# Load from disk
with open('nifty_list.json', 'r') as f:
    loaded_list = json.load(f)

print(loaded_list)
