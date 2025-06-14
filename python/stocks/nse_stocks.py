import requests
import pandas as pd
from io import StringIO

def get_nse_in_dataframe(url = "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv", local_path=None, use_columns=None):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    }

    try:
        # Download CSV
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Optionally save to local file
        if local_path:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ File saved as: {local_path}")

        # Read CSV into pandas DataFrame
        content = response.content.decode('utf-8-sig')
        df = pd.read_csv(StringIO(content))

        # If specific columns requested, filter them
        if use_columns:
            df = df[use_columns]

        return df

    except Exception as e:
        print(f"❌ Error: {e}")
        return pd.DataFrame()

# 🔍 Example usage:
#url = "https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv"
#columns = ["SYMBOL", "NAME OF COMPANY"]
df = get_nse_in_dataframe(local_path = None, use_columns = None)

# Display top 5 rows
print(df)
