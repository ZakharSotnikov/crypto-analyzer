from cripto_api import get_cripto
from stats import parse_cripto_data
from display import print_info


def main():
    cripto_lst = get_cripto(pages=1)
    data = parse_cripto_data(cripto_lst)
    print_info(data)


if __name__ == "__main__":
    main()
