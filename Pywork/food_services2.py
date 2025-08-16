import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    reader = json.load(file)
    mydict = {}
    for row in reader:
        if row['TypeObject'] not in mydict:
            mydict[row['TypeObject']] = [row['Name'], row['SeatsCount']]
        else:
            if mydict[row['TypeObject']][1] < row['SeatsCount']:
                mydict[row['TypeObject']] = [row['Name'], row['SeatsCount']]
    for key, value in sorted(mydict.items()):
        print(f'{key}: {value[0]}, {value[1]}')