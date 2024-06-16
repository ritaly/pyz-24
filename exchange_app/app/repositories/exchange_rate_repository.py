import requests
from flask import current_app



def convert_to_pln(price_usd):
    api_key = current_app.config['EX_RATE_API_KEY']
    base_url = current_app.config['EX_RATE_BASE_URL']
    url = f'{base_url}/{api_key}/pair/USD/PLN'

    response = requests.get(url)
    if response.status_code == 200:
        exchange_data = response.json()
        rate_usd_pln = exchange_data.get('conversion_rate')
        price_pln = float(price_usd) * rate_usd_pln
    else:
        price_pln = 0
        print('Nieudało sie pobrać kursu wymiany walut')
    return price_pln
