from colorama import init, Fore
from colorama import Back
from colorama import Style
from datetime import datetime, time
from dotenv import load_dotenv
import requests
import os
import random
import getpass
import time

load_dotenv()
init()

api_key = os.getenv('API_KEY')
url_weather = f'http://api.openweathermap.org/data/2.5/weather?lat=44.9572&lon=34.1108&appid={api_key}&units=metric'
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
        print(f"\n{Style.BRIGHT}{Fore.WHITE}Good Evening, {Fore.YELLOW}favor{Style.RESET_ALL}.")
    elif hours > 12:
        print(f"\n{Style.BRIGHT}{Fore.WHITE}Good Afternoon, {Fore.YELLOW}favor{Style.RESET_ALL}.")
    else:
        print(f"\n{Style.BRIGHT}{Fore.WHITE}Good Moring, {Fore.YELLOW}favor{Style.RESET_ALL}.")
    print(f"{Style.BRIGHT}{Fore.WHITE}    It's {Fore.CYAN}{time_str}{Fore.WHITE} on a {Fore.MAGENTA}{wordrand}{Fore.BLUE} {datetime.now().strftime("%A")}!{Style.RESET_ALL}\n")

def hello_weather():
    try:
        response = requests.get(url_weather)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"{Fore.RED}Ошибка API: {response.status_code}, {response.text}{Style.RESET_ALL}")
            return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def humidity1():
    if data['main']['humidity'] > 70:
        print(f"{Style.BRIGHT}{Fore.BLUE}Влажность: {data['main']['humidity']}%{Style.RESET_ALL}")
    elif data['main']['humidity'] < 45:
        print(f"{Style.DIM}{Fore.CYAN}Влажность: {data['main']['humidity']}%{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.CYAN}Влажность: {data['main']['humidity']}%{Style.RESET_ALL}")


def temperature():
    if data['main']['temp'] > 26:
        print(f"{Style.BRIGHT}{Fore.RED}Температура (C): {data['main']['temp']}°C{Style.RESET_ALL}")
    elif data['main']['temp'] < 13:
        print(f"{Style.BRIGHT}{Fore.CYAN}Температура (C): {data['main']['temp']}°C{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.YELLOW}Температура (C): {data['main']['temp']}°C{Style.RESET_ALL}")

data = hello_weather()

def main_weather():
    print(f"{Style.BRIGHT}{Fore.CYAN}Детальный статус: {Fore.MAGENTA}{data['weather'][0]['description']}{Style.RESET_ALL}")
    humidity1()
    temperature()

def log_main():
    clean_screen()
    log_user = getpass.getpass(prompt="\nUser: ")
    log_pas = getpass.getpass(prompt="Password: ")
    if log_user == user:
        if log_pas == pas:
            clean_screen()
            time.sleep(0.5)
            print(f"\n{Style.BRIGHT}{Fore.WHITE}WELCOME TO SYSTEM, FAVOR!{Style.RESET_ALL}")
            print("=========================")
            time.sleep(0.5)
            hello_time(hours)
        else:
            clean_screen()
            print(f"\n{Style.BRIGHT}{Fore.RED}НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ!{Style.RESET_ALL}")
            time.sleep(1)
            pass
    else:
        clean_screen()
        print(f"\n{Style.BRIGHT}{Fore.RED}НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ!{Style.RESET_ALL}")
        time.sleep(1)
        pass



if __name__ == '__main__':
    log_main()
    time.sleep(0.5)
    main_weather()
#Будьте терпимы к другим и строги к себе, осознавайте, что вы можете контролировать, а что нет, и игнорируйте людей, которые находятся во власти собственных негативных эмоций.
#Если вы хотите совершенствоваться, будьте довольны тем, что выглядите глупо или нелепо, у вас есть власть над своим разумом, а не над внешними событиями. Осознайте это, и вы обретете силы.
#Развивайте волю, чтобы сказать «нет» отвлекающим факторам. Иногда нам нужно исчезнуть на некоторое время, чтобы вернуться сильнее.