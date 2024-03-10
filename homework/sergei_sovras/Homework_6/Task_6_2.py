answ_word = ''
for i in range(101):
    if i % 3 == 0:
        answ_word += 'Fuzz'
    if i % 5 == 0:
        answ_word += 'Buzz'
    if answ_word != '':
        print(answ_word)
    else:
        print(i)
    answ_word = ''
