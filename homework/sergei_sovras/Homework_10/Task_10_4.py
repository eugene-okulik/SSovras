PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')
item = []
cost = []
for i in range(len(new_list)):
    x, y = new_list[i].split(' ')
    item.append(x)
    cost.append(int(y[:-1]))
    i += 1
print(dict(zip(item, cost)))
