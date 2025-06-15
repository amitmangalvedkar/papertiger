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

def set_nifty50_symbols(file_location=".", file_name = "nifty_list.json"):
    try:
        # Save to disk
        with open(file_location +"/" + file_name, 'w') as f:
            json.dump(nifty_50_symbols, f)
    except:
        print("Unable to persist")
    

def get_nifty50_symbols(file_location=".", file_name = "nifty_list.json"):
    try:
        #This expects a file with the name nifty_stock_symbols having contents such as
        #["RELIANCE.NS", "TCS.NS", "INFY.NS"] to be present in the same folder
        # Load from disk
        with open(file_location +"/" + file_name, 'r') as f:
            nifty_stock_symbols = json.load(f)
    except:
        print("Exception thrown....")
        '''
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
        '''
        nifty_stock_symbols = nifty_50_symbols
    finally:
        return nifty_stock_symbols

set_nifty50_symbols()

print(get_nifty50_symbols())