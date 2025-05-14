import requests

initial_currency = input("Enter the initial currency (e.g., USD): ").upper()
target_currency = input("Enter the target currency (e.g., EUR): ").upper()

while True:
    try:
        amount = float(input("Enter the amount to convert : "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if amount == 0:
        print("Amount cannot be zero.")
        continue
    else:
        break

# ✅ Use f-string and correct the order of currencies
url = f"https://api.apilayer.com/fixer/convert?from={initial_currency}&to={target_currency}&amount={amount}"

headers = {"apikey": "k2LvOIQExhWoWWh10TAv8O4l59Eyxk2b"}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error: Unable to fetch data from the API.")
    quit()

data = response.json()

# ✅ Print the result in a formatted way
if data.get("success", False):
    result = data["result"]
    print(f"{amount} {initial_currency} = {result} {target_currency}")
else:
    print("Error:", data.get("error", {}).get("info", "Unknown error"))
