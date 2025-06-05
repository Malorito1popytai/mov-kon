from mov_kon import *
from datetime import datetime, time
import time


current_time = datetime.now()
hours = current_time.hour
options = ["Погода сегодня", "Музыка", "Выход"]

def main():
    while True:    
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input(f"Выберите действие (1-{len(options)}): ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            choice = int(choice)
            selected = options[choice - 1]
            
            if selected == "Погода сегодня":
                clean_screen()
                time.sleep(0.5)
                main_weather()
                input("\nНажмите Enter для продолжения...")
                clean_screen()
                hello_time(hours)
            elif selected == "Музыка":
                print("asdasd")
                input()
            elif selected == "Выход":
                print("Выход из программы")
                time.sleep(0.5)
                break
        else:
            clean_screen()
            print("Неверный выбор! Попробуйте снова.")
            input("\nНажмите Enter для продолжения...")

if __name__ == '__main__':
    log_main()
    time.sleep(0.5)
    main()