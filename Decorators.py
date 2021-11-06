def decorate(func):
    def wrapper(*args, **kwargs):
        print('<<' * 25, 'J.A.R.V.I.S', '>>'*25)
        result = func(*args, **kwargs)
        return result

    return wrapper