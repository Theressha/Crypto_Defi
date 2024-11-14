#Import packages
import requests
#Method for fetch crypto
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parameters = {
        'vs_currency': 'usd',  # Convert to USD
        'order': 'market_cap_desc',  # Order by market cap
        'per_page': 10,  # Top 10 cryptocurrencies
        'page': 1,
        'sparkline': 'false'
    }
    #call request
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()  # Raise error if the request fails
        data = response.json()
        
        print("The top 10 Cryptocurrencies:")
        for coin in data:
            name = coin['name']
            symbol = coin['symbol'].upper()
            price = coin['current_price']
            print(f"{name} ({symbol}): ${price}")
    except requests.RequestException as e:
        print("Error fetching cryptocurrency data:", e)

#fech prices
fetch_crypto_prices()
