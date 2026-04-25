import requests

# Replace with your API key
API_KEY = "YOUR_API_KEY"

def convert_currency(from_currency, to_currency, amount):
    try:
        url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
        response = requests.get(url)
        data = response.json()

        rates = data['rates']

        if from_currency not in rates or to_currency not in rates:
            print("Invalid currency code!")
            return

        # Convert to USD first, then to target currency
        usd_amount = amount / rates[from_currency]
        converted_amount = usd_amount * rates[to_currency]

        print(f"{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")

    except Exception as e:
        print("Error occurred:", e)


# User Input
from_currency = input("Enter FROM currency (e.g. USD): ").upper()
to_currency = input("Enter TO currency (e.g. INR): ").upper()

try:
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be greater than 0")
    else:
        convert_currency(from_currency, to_currency, amount)
except:
    print("Invalid amount entered!")