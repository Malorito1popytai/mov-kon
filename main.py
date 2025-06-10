from mov_kon import *
from datetime import datetime, time
from simple_term_menu import TerminalMenu
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import time


current_time = datetime.now()
hours = current_time.hour
options = ["Погода сегодня", "Музыка", "Выход"]

def main():
    while True:
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            clean_screen()
            time.sleep(0.5)
            main_weather()
            input("\nНажмите Enter для продолжения...")
            clean_screen()
            hello_time(hours)
        elif menu_entry_index == 1:
            print("asdasd")
            input()
        elif menu_entry_index == 2:
            print("\nВыход из программы")
            time.sleep(0.5)
            break

if __name__ == '__main__':
    log_main()
    time.sleep(0.5)
    main()