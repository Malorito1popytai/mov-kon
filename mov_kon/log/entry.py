from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
from ..addtion.screen import clean_screen
from ..addtion.hello import hello_time
from datetime import datetime, time
import os
import getpass
import time

load_dotenv()
console = Console()

current_time = datetime.now()
hours = current_time.hour
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

#tqdm    
#Будьте терпимы к другим и строги к себе, осознавайте, что вы можете контролировать, а что нет, и игнорируйте людей, которые находятся во власти собственных негативных эмоций.
#Если вы хотите совершенствоваться, будьте довольны тем, что выглядите глупо или нелепо, у вас есть власть над своим разумом, а не над внешними событиями. Осознайте это, и вы обретете силы.
#Развивайте волю, чтобы сказать «нет» отвлекающим факторам. Иногда нам нужно исчезнуть на некоторое время, чтобы вернуться сильнее.