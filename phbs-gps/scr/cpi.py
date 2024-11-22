import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime

def fetch_cpi_data(start_date, end_date):
    """
    Fetch US Consumer Price Index (CPI) data from FRED.
    """
    try:
        cpi_data = pdr.get_data_fred('CPIAUCSL', start_date, end_date)
        return cpi_data
    except Exception as e:
        print(f"Error fetching CPI data: {e}")
        return None

def calculate_last_4_quarters_inflation(cpi_data):
    """
    Calculate year-over-year inflation rates for the last 4 quarters.
    """
    cpi_data['Quarter'] = cpi_data.index.to_period('Q')
    quarterly_cpi = cpi_data.groupby('Quarter').mean()
    inflation_rates = quarterly_cpi.pct_change(periods=4) * 100
    return inflation_rates.tail(4)