import re

import inquirer
questions = [
  inquirer.List('menu',
  message="What do you want to choose?",
  choices=['Weather now', 'Music', 'Exit'],
  ),
]
answers = inquirer.prompt(questions)
print(answers)
if answers['menu'] == 'Weather now':
    print('asd')