import requests


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # will raise error for bad responses
        data = response.json()

        if data.get("success", True) and "result" in data:
            return data["result"]
        else:
            print("Error in response data.")
            return None

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None


# User Interface
print("Welcome to the Currency Converter 💱")
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency (e.g., USD): ").upper()
to_currency = input("Enter the target currency (e.g., EUR): ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("An error occurred during the conversion.")
