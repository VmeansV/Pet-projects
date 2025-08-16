from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

res = OrderedDict()

for i in range(len(data)):
    if i % 2 != 0:
        name, grade = data.popitem(last=True)
        res[name] = grade
    else:
        name, grade = data.popitem(last=False)
        res[name] = grade

print(res)
for key, value in res.items():
    print(f'{key}: {value}')