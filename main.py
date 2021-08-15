import requests
import json

response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin')
json_data = response.json()

print(json_data[0]['id'])
print(json_data[0]['symbol'])
print(json_data[0]['image'])
print(json_data[0]['current_price'])
print(json_data[0]['price_change_24h'])
print(json_data[0]['price_change_percentage_24h'])


