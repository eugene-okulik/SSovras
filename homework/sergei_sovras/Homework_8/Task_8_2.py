def fibonachi_generator(limit=100000):
    a = 0
    b = 1
    lenth = 0
    while lenth < limit:
        yield a
        a, b = b, b + a
        lenth += 1


count = 1
for number in fibonachi_generator(100000):
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
    count += 1
