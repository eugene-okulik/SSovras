def action_rule(func):
    def wrapper(x, y):
        operator = ''
        if x == y:
            operator = '+'
        if x > y:
            operator = '-'
        if x < y:
            operator = '/'
        if x * y < 0:
            operator = '*'
        return func(x, y, operator)
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


a, b = int(input()), int(input())
print(calc(a, b))
