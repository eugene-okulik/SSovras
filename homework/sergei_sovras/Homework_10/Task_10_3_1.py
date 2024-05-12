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
def calc(c, d, operation):
    if operation == '+':
        return c + d
    elif operation == '-':
        return c - d
    elif operation == '/':
        return c / d
    elif operation == '*':
        return c * d


a, b = int(input()), int(input())
print(calc(a, b))
