from cripto_api import get_cripto
from stats import parse_cripto_data


def main():
    cripto_lst = get_cripto(pages=1)
    parse = parse_cripto_data(cripto_lst)
    parse.to_csv("cripto.csv", index=False)
    print(f"Сохранено {len(parse)} монет в cripto.csv")


if __name__ == "__main__":
    main()
