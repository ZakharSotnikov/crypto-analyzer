import pandas as pd


def parse_cripto_data(cripto_lst):
    data = []

    for cripto in cripto_lst:

        data.append({
            "name": cripto["name"],
            "current_price": cripto["current_price"],
            "total_supply": cripto["total_supply"],
            "price_change_percentage_24h": cripto["price_change_percentage_24h"],
            "market_cap_rank": cripto["market_cap_rank"],
        })

    return pd.DataFrame(data)

    # Найти топ-3 лидера роста за 24 часа (по price_change_percentage_24h)

    # Найти топ-3 лидера падения за 24 часа

    # Найти монету с максимальным объёмом торгов (total_volume)

    # Посчитать суммарную капитализацию всех 50 монет
