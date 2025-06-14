'''
This returns display as shown below

          SYMBOL                           NAME OF COMPANY  SERIES  DATE OF LISTING   PAID UP VALUE   MARKET LOT   ISIN NUMBER   FACE VALUE
0      20MICRONS                        20 Microns Limited      EQ      06-OCT-2008               5            1  INE144J01027            5
1     21STCENMGM  21st Century Management Services Limited      EQ      03-MAY-1995              10            1  INE253B01015           10
2         360ONE                       360 ONE WAM LIMITED      EQ      19-SEP-2019               1            1  INE466L01038            1
3      3IINFOLTD                       3i Infotech Limited      EQ      22-OCT-2021              10            1  INE748C01038           10
4        3MINDIA                          3M India Limited      EQ      13-AUG-2004              10            1  INE470A01017           10
...          ...                                       ...     ...              ...             ...          ...           ...          ...
2093        ZOTA                  Zota Health Care LImited      EQ      19-AUG-2019              10            1  INE358U01012           10
2094       ZUARI              Zuari Agro Chemicals Limited      EQ      27-NOV-2012              10            1  INE840M01016           10
2095    ZUARIIND                  ZUARI INDUSTRIES LIMITED      EQ      12-APR-1995              10            1  INE217A01012           10
2096   ZYDUSLIFE                Zydus Lifesciences Limited      EQ      18-APR-2000               1            1  INE010B01027            1
2097   ZYDUSWELL                    Zydus Wellness Limited      EQ      13-NOV-2009              10            1  INE768C01010           10

'''

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
