import json
import sqlite3

from solutions.products import Products

with open('../4/_update_data.json', 'r') as file:
    arr = json.load(file)

connection = sqlite3.connect('../outputs/lykov.db')
products = Products(connection)

for item in arr:
    name = item['name']
    splitted = item['method'].split('_')
    field = splitted[0]
    value = item['param']
    match field:
        case 'available':
            value = 0 if item['param'] == False else 1
            products.update(('isAvailable', value), f'name = "{name.replace('\'', '\'\'')}"')
        case 'price':
            if splitted[1] == 'abs':
                products.update(('price', f'ABS({value})'), f'name = "{name.replace('\'', '\'\'')}"')
            elif splitted[1] == 'percent':
                products.update(('price', f'MAX(price + (price * {value}), 0)'), f'name = "{name.replace('\'', '\'\'')}"')
        case 'quantity':
            products.update(('price', f'MAX(quantity + {value}, 0)'), f'name = "{name.replace('\'', '\'\'')}"')
        case 'remove':
            products.delete(f'name = "{name.replace('\'', '\'\'')}"')
