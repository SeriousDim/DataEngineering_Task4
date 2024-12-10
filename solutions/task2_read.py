import sqlite3
from solutions.games import Games
from solutions.prizes import Prizes
import pandas as pd

connection = sqlite3.connect('../outputs/lykov.db')

games = Games(connection)
prizes = Prizes(connection)

cursor = connection.cursor()

# показать призы для каждой игры
cursor.execute("""
    SELECT g.id, g.name AS game_name, 
       p.place, p.prize
    FROM Games g
    LEFT JOIN Prizes p ON g.name = p.name;
""")
entries_1 = pd.DataFrame(cursor.fetchall(), columns=['id', 'name', 'place', 'prize'])
print(entries_1)

# показать сумму призовых по всем играм
cursor.execute("""
    SELECT g.name AS game_name, SUM(p.prize) AS prize_count
    FROM Games g
    JOIN Prizes p ON g.name = p.name
    GROUP BY g.name;
""")
entries_2 = pd.DataFrame(cursor.fetchall(), columns=['name', 'sum of prizes'])
print(entries_2)

# то же, но с сортировкой по сумме призовых
cursor.execute("""
    SELECT g.name AS game_name, SUM(p.prize) AS prize_count
    FROM Games g
    JOIN Prizes p ON g.name = p.name
    GROUP BY g.name
    ORDER BY prize_count DESC
""")
entries_3 = pd.DataFrame(cursor.fetchall(), columns=['name', 'sum of prizes'])
print(entries_3)
