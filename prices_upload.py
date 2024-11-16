# Import packages
import requests
import tkinter as tk
from tkinter import messagebox

# Method to fetch crypto prices
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    # Fill parameters
    parameters = {
        'vs_currency': 'usd',  # Convert to USD
        'order': 'market_cap_desc',  # Order by market cap
        'per_page': 10,  # Top 10 cryptocurrencies
        'page': 1,
        'sparkline': 'false'
    }
    # Call request
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Raise error if the request fails
        data = response.json()
        
        # Display in a message box
        prices = "The top 10 Cryptocurrencies:\n"
        for coin in data:
            name = coin['name']
            symbol = coin['symbol'].upper()
            price = coin['current_price']
            prices += f"{name} ({symbol}): ${price}\n"
        
        messagebox.showinfo("Crypto Prices", prices)
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching cryptocurrency data: {e}")

# Create the GUI
root = tk.Tk()
root.title("Crypto Price Fetcher")

# Add a button
fetch_button = tk.Button(root, text="Fetch Crypto Prices", command=fetch_crypto_prices)
fetch_button.pack(pady=20)

# Run the GUI loop
root.mainloop()

