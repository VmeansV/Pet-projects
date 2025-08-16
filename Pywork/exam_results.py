import json, csv

with open('exam_results.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader.fieldnames[2] = 'best_score'
    reader = sorted(reader, key=lambda x: (x['best_score'], x['date_and_time']), reverse=True)
    mydict = {}
    for row in reader:
        if row['email'] not in mydict:
            mydict[row['email']] = row
            mydict[row['email']]
        else:
            if int(mydict[row['email']]['best_score']) < int(row['best_score']):
                mydict[row['email']] = row

    
    res = sorted(mydict.values(), key=lambda x: x['email'])
    for row in res:
        row['best_score'] = int(row['best_score'])
    with open('best_scores.json', 'w', encoding='utf-8') as file:
        json.dump(res, file, indent=2)