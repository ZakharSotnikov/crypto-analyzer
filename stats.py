import pandas as pd


def parse_cripto_data(cripto_lst):
    data = []
    total_cap = 0
    total_volume_max = 0
    for cripto in cripto_lst:
        name = cripto.get("name")
        cap = cripto.get("market_cap")
        total_cap += cap
        total_volume = cripto.get("total_volume")
        if total_volume > total_volume_max:
            total_volume_max = total_volume
            name_total = name
        price_change_percentage_24h = cripto.get("price_change_percentage_24h")
        data.append({
            "name": name,
            "price_change_percentage_24h": price_change_percentage_24h,
            "market_cap": cap,
            "total_volume_max": total_volume
        })
    data.append({
        "name": f"Суммарная капитализация = {total_cap}",
    })
    data.append({
        "name": f"Монета с максимальным объемом торгов - {name_total} = {total_volume_max}"
    })
    return pd.DataFrame(data)
    # Найти топ-3 лидера роста за 24 часа (по price_change_percentage_24h)

    # Найти топ-3 лидера падения за 24 часа

    # Найти монету с максимальным объёмом торгов (total_volume)
