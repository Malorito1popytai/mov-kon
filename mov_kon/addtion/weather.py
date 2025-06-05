from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text
import requests
import os

load_dotenv()
console = Console()

api_key = os.getenv('API_KEY')
url_weather = f'http://api.openweathermap.org/data/2.5/weather?lat=44.9572&lon=34.1108&appid={api_key}&units=metric'

def hello_weather():
    try:
        response = requests.get(url_weather)
        if response.status_code == 200:
            return response.json()
        else:
            console.print(f"[bold red]Ошибка API: {response.status_code}, {response.text}[/bold red]")
            return None
    except Exception as e:
        console.print(f"[bold]Ошибка: {e}[/blod]")
        return None


def humidity1():
    if data['main']['humidity'] > 70:
        console.print(f"[bold #0022ff]Влажность: {data['main']['humidity']}%[/]")
    elif data['main']['humidity'] < 45:
        console.print(f"[bold #0080ff]Влажность: {data['main']['humidity']}%[/]")
    else:
        console.print(f"[bold #005eff]Влажность: {data['main']['humidity']}%[/]")


def temperature():
    if data['main']['temp'] > 26:
        console.print(f"[bold #ff4d00]Температура (C): {data['main']['temp']}°C[/]")
    elif data['main']['temp'] < 13:
        console.print(f"[bold #00ff84]Температура (C): {data['main']['temp']}°C[/]")
    else:
        console.print(f"[bold #ffd500]Температура (C): {data['main']['temp']}°C[/]")
data = hello_weather()

def main_weather():
    with console.status("search..", spinner="dots"):
        time.sleep(1.5)
        hello_weather()
        console.print(f"\n[bold cyan]Детальный статус: [/bold cyan][bold magenta]{data['weather'][0]['description']}[/bold magenta]")
        humidity1()
        temperature()