from collections import ChainMap        
from collections import Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

all_res = ChainMap(bread, meat, sauce, vegetables, toppings)
cntr = Counter()
total_price = 0
for i in input().split(','):
    cntr.update([i])
    total_price += all_res[i] 
mx_len = len(max(cntr, key=len))
second_len = 7 + len(str(total_price))
for key, value in sorted(cntr.items()):
    print(key.ljust(mx_len), end='')
    print(f' x {value}')
if mx_len > second_len:
    print('-' * (mx_len + len(str(max(cntr, key=lambda x: cntr[x])))))
    print(len(str(max(cntr, key=lambda x: cntr[x]))))
else:
    print('-' * (second_len))
print(f'ИТОГ: {total_price}р')