import pandas as pd

# URL of the Wikipedia page containing the list
url = "https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_National_Stock_Exchange_of_India"

# Read all tables from the page
tables = pd.read_html(url)

# Initialize empty list for all symbols
nse_symbols = []

# Parse each table to extract symbols (assuming they are in the first or second column)
for table in tables:
    for col in table.columns:
        if "Symbol" in str(col) or "Ticker" in str(col) or "Code" in str(col):
            tickers = table[col].dropna().astype(str).tolist()
            nse_symbols.extend(tickers)
            break  # Take only the first relevant column

print(nse_symbols)

# Remove duplicates and format for Yahoo Finance
nse_symbols = sorted(set(nse_symbols))
yahoo_tickers = [symbol + ".NS" for symbol in nse_symbols if symbol.isalnum()]

# Save to CSV
df = pd.DataFrame(yahoo_tickers, columns=["Yahoo_Ticker"])
df.to_csv("nse_yahoo_symbols.csv", index=False)

print(f"Extracted {len(yahoo_tickers)} NSE stock tickers for Yahoo Finance.")