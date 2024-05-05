def repeat_me(func):
    def wrapper(a, count):
        i = 0
        while i < count:
            func(a)
            i += 1
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
