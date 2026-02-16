import requests
from utils import retry

URL = "https://api.coingecko.com/fffapi/v3/coins/markets"


@retry(max_attempts=3, delay=2)
def get_cripto(pages=1):
    for page in range(pages):
        params = {
            "page": page,
            "per_page": 50,
            "vs_currency": "usd",
            "order": "market_cap_desc"
        }
    responce = requests.get(URL, params=params)
    responce.raise_for_status()
    cripto_lst = responce.json()

    return cripto_lst
