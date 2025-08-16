import csv

with open('name_log.csv', 'r', encoding='utf-8') as file:
    columns = file.readline().strip().split(',')
    file.seek(0)
    mydict = {}
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if row['email'] not in mydict:
            mydict[row['email']] = [row['username'], row['dtime']]
        else:
            if mydict[row['email']][1] < row['dtime']:
                mydict[row['email']] = [row['username'], row['dtime']]

    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(columns)
        t = []
        for key, value in sorted(mydict.items()):
            row = [value[0], key, value[1]]
            writer.writerow(row)
