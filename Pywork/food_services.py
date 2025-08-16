import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    reader = json.load(file)
    areas_dict = {}
    net_dict = {}
    for row in reader:
        areas_dict[row['District']] = areas_dict.get(row['District'], 0) + 1
        if row['IsNetObject'] == 'да':
            net_dict[row['OperatingCompany']] = net_dict.get(row['OperatingCompany'], 0) + 1
    print(f'{max(areas_dict, key=areas_dict.get)}: {max(areas_dict.values())}')
    print(f'{max(net_dict, key=net_dict.get)}: {max(net_dict.values())}')