import csv, json

with open('playgrounds.csv', 'rt', encoding='utf-8') as file1, open('addresses.json', 'wt', encoding='utf-8') as file2:
    t = {}
    reader = csv.DictReader(file1, delimiter=';')
    for row in reader:
        area = row['AdmArea']
        district = row['District']
        address = row['Address']
        
        t.setdefault(area, {})
        t[area].setdefault(district, [])
        t[area][district].append(address)

    json.dump(t, file2, indent=3, ensure_ascii=False)