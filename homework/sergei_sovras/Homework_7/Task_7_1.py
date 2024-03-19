quiz = 5
while True:
    answer = input('Enter the number or type end to leave: ')
    if answer == 'end':
        break
    elif quiz == int(answer):
        print('You are lucky!')
        break
    else:
        print('You are wrong( Try again')
