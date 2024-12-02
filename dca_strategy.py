#import packages for DCA strategy
import requests
#pandas package
import pandas as pd
#time package
import time

# Function to fetch Bitcoin prices from a public API. DCA strategy
def fetch_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))  # Price in USD
    except Exception as e:
        print("Error fetching Bitcoin price:", e)
        return None

# Function to fetch Bitcoin prices from a public API. DCA strategy
def fetch_bitcoin_price_new():
    try:
        response = requests.get("https://api.coindesk.com/v2/bpi/currentprice/BTC.json")
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))  # Price in USD
    except Exception as e:
        print("Error fetching Bitcoin price:", e)
        return None


# Simulate Dollar-Cost Averaging (DCA)
def simulate_dca(total_investment, interval_in_days, months):
    investment_per_interval = total_investment / (months * (30 // interval_in_days))
    investment_dates = pd.date_range(start=pd.Timestamp.now(), periods=(months * (30 // interval_in_days)), freq=f"{interval_in_days}D")
    
    bitcoin_owned = 0
    total_spent = 0
    
    print(f"Simulating DCA Strategy for {months} months, investing ${investment_per_interval:.2f} every {interval_in_days} days.")
    
    for date in investment_dates:
        price = fetch_bitcoin_price()
        if price:
            bitcoin_bought = investment_per_interval / price
            bitcoin_owned += bitcoin_bought
            total_spent += investment_per_interval
            print(f"[{date.date()}] Invested ${investment_per_interval:.2f} at ${price:.2f}/BTC. Total BTC owned: {bitcoin_owned:.6f}")
        else:
            print(f"[{date.date()}] Failed to fetch price. Skipping investment.")
        time.sleep(1)  # Wait to avoid hitting API limits (can be adjusted)

    print("\nSimulation complete")
    print(f"Total BTC owned: {bitcoin_owned:.6f}")
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Average cost per BTC: ${total_spent / bitcoin_owned:.2f if bitcoin_owned > 0 else 'N/A'}")

# Parameters for DCA strategy
total_investment = 1000  # Total USD to invest
interval_in_days = 7     # Invest every 7 days
months = 6               # Simulate for 6 months

simulate_dca(total_investment, interval_in_days, months)
