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
from rich import box
from rich.prompt import Prompt
from rich.console import Group
import time
from gnews import GNews
import os
import keyboard

console = Console()


width_con_def = console.width
width_console = max(40, width_con_def // 2 - 2)
width_news = width_console - 10

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



'''
   for article in news:
        print(f"Заголовок: {article['title']}")
        print(f"Источник: {article['publisher']['title']}")
        print(f"Ссылка: {article['url']}")
        print("-" * 40)
'''

def news_panel_search(querry, selected_index=0):
    google_news = GNews(language='ru', country='US', max_results=10)
    news = google_news.get_news(querry)
    panel_news = Text()
    for idx, article in enumerate(news):
        title_news_str = f"{article['title']}"
        title_news_str = title_news_str[:width_news] + "..." if len(title_news_str) > width_news else title_news_str
        title = Text(title_news_str, style="bold cyan")
        style = "bold cyan on yellow" if idx == selected_index else "bold cyan"

        panel_news.append(title)
        panel_news.append("\n")
    selected_news = news[selected_index] if selected_index < len(news) else None

    left_content = Panel(
    panel_news, 
    title=f"Новости: {querry}",
    expand=False,
    width=width_console,
    padding=(1, 2),
    border_style="blue")

    if selected_news:
        right_text = Text()
        right_text.append(f"Заголовок: {selected_news['title']}\n", style="bold white")
        right_text.append(f"Источник: {selected_news['publisher']['title']}\n", style="italic cyan")
        right_text.append(f"Ссылка: {selected_news['url']}", style="link")

    right_content = Panel(
        right_text, 
        title="Детали новости",
        width=width_console,
        border_style="red",
        box=box.ROUNDED,
        padding=(1, 2)
    )

    right_content = Panel(
        right_text, 
        title="Правая колонка", 
        width=width_console,
        border_style="red")

    columns = Columns([left_content, right_content], expand=True, align="center")
    return Group(columns), news, selected_index


def main_news():
    clean_screen()
    querry = Prompt.ask("Search")
    if querry.lower() == 'exit':
        return
        
    clean_screen()
    with console.status("Search", spinner="dots"):
        time.sleep(1)
        result, news, selected_index = news_panel_search(querry)
        console.print(result)

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up' and selected_index > 0:
                selected_index -= 1
            elif event.name == 'down' and selected_index < len(news) - 1:
                selected_index += 1
            elif event.name in ('q', 'esc'):
                break

            clean_screen()
            result, _, selected_index = news_panel_search(querry, selected_index)
            console.print(result)
    clean_screen()
    console.print(Text("Done!"), style="bold green", justify="center")
if __name__== "__main__":
    main_news()