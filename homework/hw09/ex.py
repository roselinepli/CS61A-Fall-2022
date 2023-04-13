from operator import add, mul, truediv

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    """Combine elements of s using f starting with initial."""
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    """Combine elements of s using f starting with initial."""
    if not s:
        return initial
    first, rest = s[0], s[1:]
    return reduce(f, rest, f(initial, first))

def add_all(n, ls):
    try:
        return reduce(add, ls, n)
    except TypeError:
        print('Please enter a number!')