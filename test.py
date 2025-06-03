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
        print(f"Источник: {article['publisher']['title']}")
        print(f"Ссылка: {article['url']}")
        print("-" * 40)


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