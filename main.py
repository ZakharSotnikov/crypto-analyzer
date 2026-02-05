from cripto_api import get_cripto
from stats import parse_cripto_data
from display import table_rich


def main():
    cripto_lst = get_cripto(pages=1)
    data = parse_cripto_data(cripto_lst)
    table_rich(data)


if __name__ == "__main__":
    main()
