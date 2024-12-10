import sqlite3

from solutions.games import Games

connection = sqlite3.connect('../outputs/lykov.db')

games = Games(connection)

def parse_to_entries(text):
    result = []
    rows = text.split('=====')
    for row in rows:
        lines = row.split('\n')
        entry = []
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                k, v = line.split('::')
                entry.append(v)
        result.append(entry)
    return result[:-1]


if __name__ == '__main__':
    with open('../1-2/item.text', 'r', encoding='utf-8') as file:
        games.create()
        entries = parse_to_entries(file.read())
        for entry in entries:
            games.insert(entry)
