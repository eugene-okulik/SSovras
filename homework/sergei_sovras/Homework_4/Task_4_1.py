my_tuple = (1, 2, 'test_value', True, 124)
my_list = [23, 'test_item', False, 'test2', 0.99]
my_dic = {'first': 1, 'second': 'two', 'third': False, 'key_4': 'test_valued', 'key_5': 213123}
my_set = {1, 'trstasd', True, 2214, 'Null'}
my_dict_final = {'tuple': my_tuple, 'list': my_list, 'dict': my_dic, 'set': my_set}
print(my_dict_final.keys())
print(my_dict_final.values())

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict_final['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
my_dict_final['list'].append('New string element for the last place')
# удалите второй элемент списка
my_dict_final['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict_final['dict']["('i am a tuple',)"] = 'New element for the dict'
# удалите какой-нибудь элемент
my_dict_final['dict'].pop('third')

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
my_dict_final['set'].add('New string for the set')
# удалите элемент из множества
my_dict_final['set'].remove(2214)

# В конце выведите на экран весь словарь
print(my_dict_final)
