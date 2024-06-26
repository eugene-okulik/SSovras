def action_rule(func):
    def wrapper(x, y):
        if x == y:
            print(func(x, y, '+'))
        if x > y:
            print(func(x, y, '-'))
        if x < y:
            print(func(x, y, '/'))
        if x * y < 0:
            print(func(x, y, '*'))
    return wrapper


@action_rule
def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b


c, d = int(input()), int(input())
calc(c, d)
