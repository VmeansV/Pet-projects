from collections import Counter, defaultdict
import csv, json

total_vegetables = defaultdict(int)
with open('quarter1.csv', 'r', encoding='utf-8') as q1:
    columns = q1.readline()
    data = q1.read()
    for row in data.splitlines():
        row = row.split(',')
        for i in row:
            if i.isdigit():
                total_vegetables[row[0]] += int(i)

with open('quarter2.csv', 'r', encoding='utf-8') as q1:
    columns = q1.readline()
    data = q1.read()
    for row in data.splitlines():
        row = row.split(',')
        for i in row:
            if i.isdigit():
                total_vegetables[row[0]] += int(i)

with open('quarter3.csv', 'r', encoding='utf-8') as q1:
    columns = q1.readline()
    data = q1.read()
    for row in data.splitlines():
        row = row.split(',')
        for i in row:
            if i.isdigit():
                total_vegetables[row[0]] += int(i)

with open('quarter4.csv', 'r', encoding='utf-8') as q1:
    columns = q1.readline()
    data = q1.read()
    for row in data.splitlines():
        row = row.split(',')
        for i in row:
            if i.isdigit():
                total_vegetables[row[0]] += int(i)
total_num = 0
with open('prices.json', 'r', encoding='utf-8') as file:
    prices = json.load(file)
    for key, value in prices.items():
        total_num += (value * total_vegetables[key])

print(total_num)