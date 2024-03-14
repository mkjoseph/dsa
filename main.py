import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def calculate_average_annual_growth_rate(data):
    # Calculate the average annual growth rate for each ZIP code
    growth_rates = []
    for index, row in data.iterrows():
        # Example: Calculate growth rate based on the first and last available monthly data
        # This is a simplification; you might want to calculate monthly growth rates and average them
        start_price = row.dropna().iloc[-13]  # Assuming the last 12 months + 1 for the first non-NaN value. 
        end_price = row.dropna().iloc[-1]
        years = 1  # Simplification for example purposes; calculate based on actual dates for precision
        growth_rate = ((end_price / start_price) ** (1 / years)) - 1
        growth_rates.append((row['RegionName'], growth_rate))

    return pd.DataFrame(growth_rates, columns=['ZIP Code', 'Average Annual Growth Rate'])

def find_top_zip_codes_for_investment(data, top_n=10):
    # Sort the data by growth rate and select the top N ZIP codes
    top_zip_codes = data.sort_values(by='Average Annual Growth Rate', ascending=False).head(top_n)
    return top_zip_codes

# Load the data
file_path = Zip_zori_uc_sfrcondomfr_sm_month (1).csv  # Update this to your actual file path
data = load_csv(file_path)

# Calculate the average annual growth rates
growth_data = calculate_average_annual_growth_rate(data)

# Find the top ZIP codes for investment
top_zip_codes = find_top_zip_codes_for_investment(growth_data)

print(top_zip_codes)
