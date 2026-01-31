import requests

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1"


def get_cripto(pages=1):
    cripto_lst = []

    for page in range(pages):
        params = {
            "page": page,
            "per_page": 50,
        }
        responce = requests.get(URL, params=params)
        responce.raise_for_status()
        data = responce.json()

        cripto_lst.extend(data)

    return cripto_lst
