import sqlite3

from solutions.songs import Songs
from solutions.task1_fill import parse_to_entries

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

with open('../3/_part_2.text', 'r', encoding='utf-8') as file:
    parsed_from_text = parse_to_entries(file.read())

print(len(parsed_from_text))
for p in parsed_from_text:
    songs.update((0 if p[-2] == False else 1, p[-1]), f"artist = '{p[0].replace('\'', '\'\'')}' AND song = '{p[1].replace('\'', '\'\'')}'")