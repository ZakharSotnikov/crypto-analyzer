from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.text import Text
from rich import box
from datetime import datetime
import time
import pandas as pd

console = Console()


def get_time():  # Получение сегодняшней даты
    date_now = datetime.now()
    formatted = date_now.strftime("%d.%m.%Y %H:%M")
    return formatted


# Создание нижнего "стола" для отображения информации по всем монетам
def table_all_wallet(data):
    table = Table(title=f"[bold green]Монеты", show_header=True,
                  header_style="bold magenta")

    table.add_column("ID[bold yellow]", style="dim", width=2)
    table.add_column("[bold yellow]Криптовалюта", min_width=20)
    table.add_column("[bold yellow]Изменение цены(%)",
                     justify="right", style="dim", min_width=20)
    table.add_column("[bold yellow]Капитализация(USD)",
                     justify="right", style="dim", min_width=20)
    table.add_column("[bold yellow]Объем торгов(USD)",
                     justify="right", style="dim", min_width=20)

    wallet = data.iloc[:50].copy()  # iloc функция для получения индекса строки

    for i, row in wallet.iterrows():  # функция iterrows() используется для построчного перебора DataFrame, возвращая пару «индекс — данные строки»
        change = row['price_change_percentage_24h']
        if pd.isna(change):  # Функция isna() ищет пустые значения и фильрует их, нужно для того, чтобы показать только монеты, без последних записей статистики
            change_text = Text("N/A")
        else:
            change_value = float(change)

            # Изменение цвета если значение больше или меньше нуля
            if change_value >= 0:
                style = Style(color="green", bold=True)
            else:
                style = Style(color="red", bold=True)

            # Корректировка значений для нормального вывода
            change_text = Text(f"{change_value:+.2f}%", style=style)

    # Добавляем строки поочередно
        table.add_row(
            str(i+1),
            str(row['name']),
            change_text,  # Вывод процентов в нормальном значении и после сортировки окрашены красным или зеленым в соответствии
            str(row["market_cap"]),
            str(row["total_volume_max"])
        )
    return console.print(table)


def table_analysis(data):  # Создание "стола" для вывода проанализированной информации
    analysis = data.iloc[50:].reset_index(drop=True)
    wallet = data.iloc[:50].copy()
    # reset_index с параметром drop=True полностью удаляет индекс и начинает с 0

    table_stats = Table(
        title=f"[bold green]Анализ рынка криптовалют на {get_time()}",
        show_header=False,  # Выключает отображения названия колонок
        box=box.SIMPLE,  # Добавляет рамку, но выключает отображение
        title_style="bold magenta",
        width=80
    )
    table_stats.add_column("1", style="bold", width=65)
    table_stats.add_column("2", style="cyan", width=40)

    table_stats.add_row("Всего монет:",
                        f"[bold]{len(wallet)}[/bold]")

    prev_category = ""
    for i, row in analysis.iterrows():
        name = str(row['name'])
        category = ""
        value_style = "bold yellow"

        if "=" in name:  # Т.к я в DataFrame написал статистику в одной колонке, понадобилось разделить по символу "="
            parts = name.split("=")
            if len(parts) == 2:  # Проверяем на сколько частей разделилось значение
                name_analisys = parts[0].strip()
                value_analisys = parts[1].strip()

                if "Топ 1 лидер роста" in name_analisys:
                    table_stats.add_row("", "")
                    value_style = "bold green"
                elif "лидер падения" in name_analisys:
                    category = '-'
                    value_style = "bold red"
                elif "лидер роста" in name_analisys:
                    category = '+'
                    value_style = "bold green"

                if category == '-' and prev_category == '+':
                    table_stats.add_row("", "")

                table_stats.add_row(
                    name_analisys, f"[{value_style}]{value_analisys}[/{value_style}]")

        prev_category = category  # Нужно для разделения пустой строкой лидеров роста и падения

    return console.print(table_stats)


def print_info(data):
    with console.status("[bold green]Загрузка...", spinner="dots") as status:
        time.sleep(2)
    console.print()
    table_analysis(data)
    table_all_wallet(data)
    console.print()
