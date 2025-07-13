from rich.console import Console
from rich.text import Text
import re
import json
import inquirer

title = input("Title: ")
status = ""
content = input("Content: ")

console = Console()
note = {status: content}
notes = {title: note}

to_json = {'notion': notes}

with open('data.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)

with open('data.json') as f:
    print(f.read())

print(notes)