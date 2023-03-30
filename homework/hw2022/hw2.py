from operator import add, mul
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.
    n: a positive integer
    term: a fuction that takes one argument to produce the term

    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square) # 1^2 * 2^2 * 3^2
    36
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple) # 1*3 * 2*3 * 3*3
    162
    """
    i = 1
    res = 1
    while i <= n:
        res *= term(i)
        i += 1
    return res


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative fuction.

    >>> accumulate(add, 0, 5, identity) # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 3, square) # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square) # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    res, i = start, 1
    while i <= n:
        res = merger(res, term(i))
        i += 1
    return res

# Alternative solution
def accumulate_reverse(merger, start, n, term):
    res, i = start, n
    while i >= 1:
        res = merger(res, term(i))
        i -= 1
    return res

def summmation_using_accumulate(n, term):
    """Return the sum: term(0) + ... + term(n), using accumulate

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """Return the product: term(1) * ... * term(n), using accumulate

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    return accumulate(mul, 1, n, term)