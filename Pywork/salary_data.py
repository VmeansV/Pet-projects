import csv

with open("salary_data.csv", "rt", encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter=';')
    mydict = {}
    for row in rows:
        mydict.setdefault(row['company_name'], []).append(int(row['salary']))
    for key, value in mydict.items():
        mydict[key] = int(sum(value) / len(value))
    res = sorted(mydict.items(), key=lambda x: x[1])
    for row in res:
        print(row[0])
