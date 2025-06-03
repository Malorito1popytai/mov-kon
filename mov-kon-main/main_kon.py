from datetime import datetime, time
from konsole import weather
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console
from rich.box import ROUNDED
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
import requests
import os
import random
import getpass
import time

load_dotenv()
console = Console()

pas = os.getenv('VAR1')
user = os.getenv('VAR2')

word = ["good", "beautiful", "productive", "busy", "warm", "cheerful", "chill"]
current_time = datetime.now()
hours = current_time.hour
time_str = current_time.strftime("%I:%M %p")

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
   
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

def log_main():
    clean_screen()
    log_user = getpass.getpass(prompt="\nUser: ")
    log_pas = getpass.getpass(prompt="Password: ")
    if log_user == user:
        if log_pas == pas:
            clean_screen()
            time.sleep(0.5)
            time.sleep(0.5)
            hello_time(hours)
        else:
            clean_screen()
            console.print(f"\n[bold red]НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ![/bold red]")
            time.sleep(1)
            console.print("\n[bold white]Нажмите Enter, чтобы закрыть программу...[/bold white]")
            input()
            exit()
            
    else:
        clean_screen()
        console.print(f"\n[bold red]НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ![/bold red]")
        time.sleep(1)
        console.print("\n[bold white]Нажмите Enter, чтобы закрыть программу...[/bold white]")
        input()
        exit()



if __name__ == '__main__':
    log_main()
    time.sleep(0.5)
    main_weather()

#tqdm    
#Будьте терпимы к другим и строги к себе, осознавайте, что вы можете контролировать, а что нет, и игнорируйте людей, которые находятся во власти собственных негативных эмоций.
#Если вы хотите совершенствоваться, будьте довольны тем, что выглядите глупо или нелепо, у вас есть власть над своим разумом, а не над внешними событиями. Осознайте это, и вы обретете силы.
#Развивайте волю, чтобы сказать «нет» отвлекающим факторам. Иногда нам нужно исчезнуть на некоторое время, чтобы вернуться сильнее.