import sqlite3
import msgpack

from solutions.products import Products

with open ('../4/_product_data.msgpack', 'rb') as file:
    packed = msgpack.unpackb(file.read())

connection = sqlite3.connect('../outputs/lykov.db')
products = Products(connection)
products.create()

id = 1
for p in packed:
    products.insert((id, p['name'],
                     p['price'],
                     p['quantity'],
                     p['category'] if 'category' in p else None,
                     p['fromCity'],
                     0 if p['isAvailable']==False else 1,
                     p['views'],
                     0))
    id += 1
