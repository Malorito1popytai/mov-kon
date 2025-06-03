from mov_kon import hello_time
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
import os
import getpass
import time

load_dotenv()
console = Console()

pas = os.getenv('VAR1')
user = os.getenv('VAR2')

def log_main():
    clean_screen()
    log_user = getpass.getpass(prompt="\nUser: ")
    log_pas = getpass.getpass(prompt="Password: ")
    if log_user == user:
        if log_pas == pas:
            clean_screen()
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