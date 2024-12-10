import sqlite3
import json
from solutions.prizes import Prizes

connection = sqlite3.connect('../outputs/lykov.db')

prizes = Prizes(connection)

prizes.create()

with open('../1-2/subitem.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for entry in data:
        prizes.insert((entry['name'], entry['place'], entry['prise']))
