import json

methods = []

with open('../4/_update_data.json', 'r') as file:
    arr = json.load(file)

for item in arr:
    methods.append(item['method'])

print(set(methods))
