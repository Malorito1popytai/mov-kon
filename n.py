
import os
import time

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

options = ["Сканировать URL", "Проверка с использованием VirusTotal", "Выход"]

while True:
        clean_screen()    
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input(f"Выберите действие (1-{len(options)}): ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            choice = int(choice)
            selected = options[choice - 1]
            clean_screen()
            
            if selected == "Сканировать URL":
                print("asdasd")
            elif selected == "Проверка с использованием VirusTotal":
                print("asdasd")
            elif selected == "Выход":
                print("Выход из программы")
                time.sleep(0.5)
                break
        else:
            clean_screen()
            print("Неверный выбор! Попробуйте снова.")
            input("\nНажмите Enter для продолжения...")