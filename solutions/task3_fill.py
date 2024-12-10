import sqlite3
import msgpack

from solutions.songs import Songs
from solutions.task1_fill import parse_to_entries

with open ('../3/_part_1.msgpack', 'rb') as file:
    packed = msgpack.unpackb(file.read())

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

songs.create()

print(len(packed))
for e in packed:
    songs.insert([e['artist'], e['song'], e['duration_ms'],
                             e['year'], e['tempo'], e['genre'],
                             e['instrumentalness'], 0, 0,
                             e['mode'], e['speechiness'], e['acousticness']])
