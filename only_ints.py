'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if all([isinstance(i, int) for i in args]):
            return fn(*args, **kwargs)
        return "Please only invoke with integers."
    return inner

@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
