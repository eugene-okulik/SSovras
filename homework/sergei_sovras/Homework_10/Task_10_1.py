def func_status(func):
    def wrapper(*any_value):
        result = func(*any_value)
        print('finished')
        return result
    return wrapper


@func_status
def example(text):
    print(text)


example('print me')
