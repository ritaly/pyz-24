import requests
from flask import current_app



def convert_to_pln(price_usd):
    api_key = current_app.config['EX_RATE_API_KEY']
    base_url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/PLN'
    response = requests.get(base_url)
    if response.status_code == 200:
        exchange_data = response.json()
        rate_USD_PLN = exchange_data.get('conversion_rate')
        print(rate_USD_PLN)

        price_pln = float(price_usd) * rate_USD_PLN
    else:
        price_pln = 0
        print('Nieudało sie pobrać kursu wymiany walut')
    return price_pln
