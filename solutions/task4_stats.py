import sqlite3
import pandas as pd

connection = sqlite3.connect('../outputs/lykov.db')
cursor = connection.cursor()

cursor.execute("""
    SELECT name, changes FROM Products
    ORDER BY changes DESC
    LIMIT 10;
""")
df = pd.DataFrame(cursor.fetchall(), columns=['name','changes'])
print(df)

cursor.execute("""
    SELECT 
        category, 
        SUM(price) AS max_price, 
        MIN(price) AS min_price, 
        MAX(price) AS max_price, 
        AVG(price) AS avg_price,
        COUNT(*) AS product_count
    FROM 
        Products
    GROUP BY 
        category;
""")
df = pd.DataFrame(cursor.fetchall(), columns=['category','sum', 'min', 'max', 'avg', 'count'])
print(df)

cursor.execute("""
    SELECT 
        category, 
        SUM(quantity) AS max_price, 
        MIN(quantity) AS min_price, 
        MAX(quantity) AS max_price, 
        AVG(quantity) AS avg_price
    FROM 
        Products
    GROUP BY 
        category;
""")
df = pd.DataFrame(cursor.fetchall(), columns=['category','sum', 'min', 'max', 'avg'])
print(df)

cursor.execute("""
    SELECT 
        category, 
        SUM(quantity) AS q, 
        SUM(price) AS p,
        quantity * price AS total
    FROM 
        Products
    WHERE fromCity = 'Душанбе'
    GROUP BY 
        category;
""")
df = pd.DataFrame(cursor.fetchall(), columns=['category','quantity', 'price', 'total_price'])
print(df)

connection.close()
