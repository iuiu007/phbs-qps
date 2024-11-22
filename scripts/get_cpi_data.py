from src.cpi import fetch_cpi_data, calculate_last_4_quarters_inflation
from datetime import datetime

# Define date range
start_date = '2018-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Fetch CPI data
print("Fetching US CPI data...")
cpi_data = fetch_cpi_data(start_date, end_date)

if cpi_data is not None:
    # Calculate inflation rates
    print("Calculating last 4 quarters' inflation rates...")
    inflation_rates = calculate_last_4_quarters_inflation(cpi_data)
    print("Last 4 quarters' inflation rates (year-over-year):")
    print(inflation_rates)
else:
    print("Failed to fetch CPI data.")