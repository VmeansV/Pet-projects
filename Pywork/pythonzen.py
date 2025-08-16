from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    res = file.read()
cntr = Counter()
for s in res:
    if s.isalpha():
        cntr.update(s.lower())

for key, value in sorted(cntr.items()):
    print(f'{key}: {value}')