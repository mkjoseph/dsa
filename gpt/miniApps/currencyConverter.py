import requests

# Replace 'YOUR_API_KEY' with your actual API key from exchangeratesapi.io
api_key = 'YOUR_API_KEY'
base_currency = 'USD'
target_currency = 'SEK'
url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base={base_currency}&symbols={target_currency}"


def convert_usd_to_sek(amount):
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    rate = data['rates'][target_currency]
    conversion_result = amount * rate
    return conversion_result
  else:
    print("Failed to fetch currency conversion rates")
    return None


# Example: Convert 100 USD to SEK
amount_usd = 100
converted_amount = convert_usd_to_sek(amount_usd)
if converted_amount is not None:
  print(f"{amount_usd} USD is equal to {converted_amount} SEK")
