import json

with open('pools.json', 'r', encoding='utf-8') as file:
    rows = json.load(file)
    t ={}
    for row in rows:
        time = row["WorkingHoursSummer"]['Понедельник'].split('-') 
        if '10:00' >= time[0] and time[1] >= '12:00':
            t[row['Address']] = [row["DimensionsSummer"]["Length"], row['DimensionsSummer']['Width']]
            res = max(t, key=t.get)
    print('x'.join(map(str, t[res])))
    print(res)