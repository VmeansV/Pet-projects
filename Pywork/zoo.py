import json

with open('zoo.json', 'r', encoding='utf-8') as file:
    rows = json.load(file)
    my_len = 0
    for row in rows:
        for value in row.values():
            my_len += value
    
    print(my_len)