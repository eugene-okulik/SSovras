PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def creating_price(new_list):
    new_list = dict([x.split(' ') for x in new_list.split('\n')])
    new_list = {x: int(y[:-1]) for x, y in new_list.items()}
    return new_list


print(creating_price(PRICE_LIST))
