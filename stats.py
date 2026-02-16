import pandas as pd


def parse_cripto_data(cripto_lst):
    data = []
    price_change_lst = []
    total_cap = 0
    total_volume_max = 0

    for cripto in cripto_lst:
        name = cripto.get("name")
        cap = cripto.get("market_cap")
        price_change_percentage_24h = cripto.get("price_change_percentage_24h")
        total_cap += cap  # Суммирование капитализации
        total_volume = cripto.get("total_volume")
        if total_volume > total_volume_max:  # поиск монеты с наибольшим объемом торгов
            total_volume_max = total_volume
            name_total = name
        if price_change_percentage_24h == None:
            price_change_percentage_24h = 0
        price_change_lst.append(price_change_percentage_24h)
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
    sort_price_change_lst = sorted(price_change_lst)
    last_three_24h = sort_price_change_lst[:3]
    first_three_24h = sort_price_change_lst[-3:]
    item_count_last = 0
    item_count_first = 0
    for item in first_three_24h[::-1]:
        item_count_first += 1
        for item_change in data:
            name_monet = item_change["name"]
            for k, v in item_change.items():
                if item == v:
                    data.append({
                        "name": f"Топ {item_count_first} лидер роста - {name_monet} = {v}"
                    })
    for item in last_three_24h:
        item_count_last += 1
        for item_change in data:
            name_monet = item_change["name"]
            for k, v in item_change.items():
                if item == v:
                    data.append({
                        "name": f"Топ {item_count_last} лидер падения - {name_monet} = {v}"
                    })

    return pd.DataFrame(data)
