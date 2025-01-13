import tkinter as tk
import requests

# This script gets data from CoinDesk API
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_bitcoin_price(currency):
    """
    This function sends a GET request to CoinDesk API and returns Bitcoin's current price for the specified currency.
    """
    response = requests.get(url)  # sending request to URL
    jsonResponse = response.json()  # saving response as JSON
    price = jsonResponse["bpi"][currency]["rate"]  # getting price for the specified currency
    return price

def show_usd():
    """
    Displays the Bitcoin price in USD.
    """
    price = get_bitcoin_price("USD")
    result_label.config(text=f"Bitcoin Price in USD: {price}")

def show_gbp():
    """
    Displays the Bitcoin price in GBP.
    """
    price = get_bitcoin_price("GBP")
    result_label.config(text=f"Bitcoin Price in GBP: {price}")

def show_euro():
    """
    Displays the Bitcoin price in EUR.
    """
    price = get_bitcoin_price("EUR")
    result_label.config(text=f"Bitcoin Price in EUR: {price}")

# Create the main window
root = tk.Tk()
root.title("Bitcoin Price Checker")

# Create a label to display the results
result_label = tk.Label(root, text="Choose a currency to view Bitcoin price", font=("Helvetica", 14))
result_label.pack(pady=20)

# Create buttons for USD, GBP, and EUR
button_usd = tk.Button(root, text="Show Bitcoin Price in USD", command=show_usd, font=("Helvetica", 12))
button_usd.pack(pady=10)

button_gbp = tk.Button(root, text="Show Bitcoin Price in GBP", command=show_gbp, font=("Helvetica", 12))
button_gbp.pack(pady=10)

button_euro = tk.Button(root, text="Show Bitcoin Price in EUR", command=show_euro, font=("Helvetica", 12))
button_euro.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

# https://github.com/Yaqub133/Yaqubelmi-Bitcoin Price Checker