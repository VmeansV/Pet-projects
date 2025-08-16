import json, csv

with open('students.json', 'r', encoding='utf-8') as file1, open('data.csv', 'w', encoding='utf-8', newline='') as file2:
    reader = json.load(file1)
    t = []
    for row in reader:
        age = row['age']
        progress = row['progress']
        if age >= 18 and progress >= 75:
            t.append(row['name'] + ', ' + row['phone'])
    t = sorted(t)
    columns = ['name', 'phone']
    writer = csv.writer(file2)
    writer.writerow(columns)
    for row in t:
        writer.writerow(row.split(", "))