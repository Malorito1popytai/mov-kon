from datetime import datetime, time
from rich.markdown import Markdown
from rich.console import Console
from rich.box import ROUNDED
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
import random


console = Console()

word = ["good", "beautiful", "productive", "busy", "warm", "cheerful", "chill"]
current_time = datetime.now()
hours = current_time.hour
time_str = current_time.strftime("%I:%M %p")


def day_today():
    long = len(word)
    c = random.randint(0, long-1)
    wordrandfunch = word[c]
    return wordrandfunch

wordrand = day_today()

def hello_time(hours):
    if hours > 17:
        panel_content = Text()
        panel_content.append(f"Good Evening, ", style="bold white")
        panel_content.append(f"{user}", style="bold yellow")
        panel_content.append(f"\n    It's",style="bold white")
        panel_content.append(f" {time_str}", style="bold cyan")
        panel_content.append(f" on a ", style="bold white")
        panel_content.append(f"{wordrand}", style="bold magenta")
        panel_content.append(f" {datetime.now().strftime('%A')}!", style="bold blue")
    elif hours > 12:
        panel_content = Text()
        panel_content.append(f"Good Afternoon, ", style="bold white")
        panel_content.append(f"{user}", style="bold yellow")
        panel_content.append(f"\n    It's",style="bold white")
        panel_content.append(f" {time_str}", style="bold cyan")
        panel_content.append(f" on a ", style="bold white")
        panel_content.append(f"{wordrand}", style="bold magenta")
        panel_content.append(f" {datetime.now().strftime('%A')}!", style="bold blue")
    else:
        panel_content = Text()
        panel_content.append(f"Good Moring, ", style="bold white")
        panel_content.append(f"{user}", style="bold yellow")
        panel_content.append(f"\n    It's",style="bold white")
        panel_content.append(f" {time_str}", style="bold cyan")
        panel_content.append(f" on a ", style="bold white")
        panel_content.append(f"{wordrand}", style="bold magenta")
        panel_content.append(f" {datetime.now().strftime('%A')}!", style="bold blue")
    
    panel = Panel(
            panel_content,
            title="[bold]WELCOME TO SYSTEM, FAVOR![/bold]",
            border_style="green",
            title_align="center",
            box=ROUNDED,
            padding=(1, 2),
            expand=False
            )
    console.print(panel)