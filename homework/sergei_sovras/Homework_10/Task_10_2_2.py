def outher_decorator(count):
    def repeat_me(func):
        def wrapper(a):
            i = 0
            while i < count:
                func(a)
                i += 1
        return wrapper
    return repeat_me


@outher_decorator(count = 2)
def example(text):
    print(text)


example('print me')
