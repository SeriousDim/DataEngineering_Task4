import sqlite3
import json
from pathlib import Path

from solutions.games import Games


connection = sqlite3.connect('../outputs/lykov.db')

games = Games(connection)

Path("../outputs/task1").mkdir(parents=True, exist_ok=True)

entries = games.get_top_sorted('begin')
d = games.entries_to_dict(entries)

with open('../outputs/task1/top_sorted.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)

entries = games.count('MIN', 'min_rating')
print(entries)

entries = games.get_frequencies('system')
print(entries)

entries = games.get_by_condition('time_on_game', 'begin > 20')
d = games.entries_to_dict(entries)

with open('../outputs/task1/filtered.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)
