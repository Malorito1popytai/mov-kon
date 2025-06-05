'''
from gnews import GNews
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def gnew():
   google_news = GNews(language='us', country='US', max_results=10)
   news = google_news.get_news('zvo')
   for article in news:
        print(f"Заголовок: {article['title']}")
        #print(f"Источник: {article['publisher']['title']}")
        #print(f"Ссылка: {article['url']}")
        #print("-" * 40)

gnew()
'''
'''
import os
import time
from rich.markdown import Markdown
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

console = Console()
wordrand = "1111"
time_str = "22222"

console.print("Стандартный красный", style="red")
console.print("Ярко-зелёный", style="bright_green")
console.print("Жирный циановый на синем", style="bold cyan on blue")
console.print("Кастомный RGB", style="#ff4500 on #000080")
console.print("256-цвет", style="color(200) on color(50)")
console.print("Жирный и курсив", style="bold italic yellow")
console.print("[bold red]Ошибка![/bold red] [italic green]Успех![/italic green]")
console.print("Центрированный текст :rocket:", style="bold magenta", justify="center")
console.print("Длинный текст..." * 10, style="green", overflow="ellipsis")


console.print("Жирный красный на чёрном", style="bold red on black")
console.print("[underline cyan on blue]Подчёркнутый циановый на синем[/underline cyan on blue]")


table = Table(border_style="blue")
table.add_column("Заголовок", style="cyan")
table.add_row("Данные", style="yellow")
console.print(table)
'''

'''
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED

console = Console()
panel = Panel(
    "Сканировать URL\n[bold white]    It's [/bold white][bold cyan][/bold cyan][bold white] on a [/bold white][bold magenta][/bold magenta][bold blue]![/bold blue]\n,\nВыход",
    title="Меню",
    border_style="green",
    title_align="center",
    box=ROUNDED,
    padding=(1, 2),
    expand=False
)
console.print(panel)

'''

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import time
from gnews import GNews
import os

console = Console()


width_con_def = console.width
width_console = width_con_def // 2
width_news = width_console - 30

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



'''
   for article in news:
        print(f"Заголовок: {article['title']}")
        print(f"Источник: {article['publisher']['title']}")
        print(f"Ссылка: {article['url']}")
        print("-" * 40)
'''

def news_panel_search(querry):
    google_news = GNews(language='ru', country='US', max_results=10)
    news = google_news.get_news(querry)
    panel_news = Text()
    for article in news:
        title_news_str = f"{article['title']}"
        title_news_str = title_news_str[:width_news] + "..." if len(title_news_str) > width_news else title_news_str
        title = Text(title_news_str, style="bold cyan")

        panel_news.append(title)
        panel_news.append("\n")
        
    left_content = Panel(
    panel_news, 
    title=f"Новости: {querry}",
    expand=False,
    width=width_console,
    border_style="blue")

    right_text = Text(
        "Содержимое правой колонки\nLine A\nLine B", 
        style="white", 
        justify="center"  # Выравнивание по центру
    )

    right_content = Panel(
        right_text, 
        title="Правая колонка", 
        expand=False,
        width=width_console,
        border_style="red")

    columns = Columns([left_content, right_content], expand=False, equal=True)
    console.print(columns)


def main_news():
    clean_screen()
    while True:
        querry = Prompt.ask("Search")
        if querry.lower() == 'exit':
            break
        clean_screen()
        with console.status("Search", spinner="dots"):
            time.sleep(1)
            news_panel_search(querry)
            console.print("Готово!")

if __name__== "__main__":
    main_news()
