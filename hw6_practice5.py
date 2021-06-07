import functools
import sys

class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:
            return 'Your Type Is No Valid'

def my_decorator(unit='int') :
    def checktype(some_func):
        @functools.wraps(some_func)
        def wrapper():
            the_type = type(some_func())
            if unit == the_type :
                some_func()
            else:
                raise MyCustomError
        return wrapper
    return checktype

@my_decorator('int')
def prt(x) :
    print(x)

prt(4)