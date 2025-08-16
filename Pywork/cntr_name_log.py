import csv
from collections import Counter

with open ('cntr_name_log.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    cntr = Counter()
    for row in rows:
        cntr.update([row['email']])
    for key, value in sorted(cntr.items()):
        print(f'{key}: {value}')