import sqlite3
import json
from pathlib import Path

from solutions.songs import Songs

connection = sqlite3.connect('../outputs/lykov.db')
songs = Songs(connection=connection, name='Songs',
              fields={
                  'artist': 'TEXT NOT NULL',
                  'song': 'TEXT NOT NULL',
                  'duration_ms': 'REAL',
                  'year': 'INTEGER',
                  'tempo': 'REAL',
                  'genre': 'TEXT',
                  'instrumentalness': 'REAL',
                  'explicit': 'INTEGER',
                  'loudness': 'REAL',
                  'mode': 'INTEGER',
                  'speechiness': 'REAL',
                  'acousticness': 'REAL'
              })

Path("../outputs/task3").mkdir(parents=True, exist_ok=True)

entries = songs.get_top_sorted('duration_ms', 10)
d = songs.entries_to_dict(entries)

with open('../outputs/task3/top_sorted.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)

entries = songs.count('MIN', 'year')
print(entries)

entries = songs.get_frequencies('artist')
print(entries)

entries = songs.get_by_condition('tempo', 'speechiness > 0.2', 15)
d = songs.entries_to_dict(entries)

with open('../outputs/task3/filtered.json', 'w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)
