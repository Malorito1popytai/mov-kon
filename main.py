from mov_kon import *
from datetime import datetime, time
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import time
import re
import inquirer
from rich.console import Console
from rich.text import Text

current_time = datetime.now()
hours = current_time.hour
console = Console()

questions = [
  inquirer.List('menu',
  message="What do you want to choose?",
  choices=['Weather now', 'Music', 'Exit'],
  ),
]

def main():
    while True:
        answers = inquirer.prompt(questions)
        if answers['menu'] == 'Weather now':
            clean_screen()
            time.sleep(0.5)
            main_weather()
            input("\nНажмите Enter для продолжения...")
            clean_screen()
            hello_time(hours)
        elif answers['menu'] == 'Music':
            print("asdasd")
            input()
        elif answers['menu'] == 'Exit':
            clean_screen()
            console.print("\n[bold white]Выход из программы....[/bold white]")
            time.sleep(0.5)
            break

if __name__ == '__main__':
    log_main()
    time.sleep(0.5)
    main()