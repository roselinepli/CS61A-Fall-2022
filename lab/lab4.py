def summation(n, term):
    """Return the sum of numbers 1 through n(including n) with
    term applied to each number.

    >>> summation(5, lambda x: x * x * x)
    225
    >>> summation(9, lambda x: x + 1)
    54
    >>> summation(5, lambda x: 2 ** x)
    62
    """
    assert n >= 1
    if n == 1:
        return term(1)
    return term(n) + summation(n-1, term)

def pascal(row, column):
    """Return the value of the item in Pascal's Triangle
    whose position is specified by row and column.

    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)
    0
    >>> pascal(3, 2)
    3
    >>> pascal(4, 2)
    6
    """
    if column > row:
        return 0
    elif row == 0 or column == 0 or row == column:
        return 1
    return pascal(row-1, column-1) + pascal(row-1, column)

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is[s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    return [[s[i], t[i]] for i in range(0, len(s))]

def double_eights(n):
    """Return whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(2834682)
    False
    >>> double_eights(78)
    False
    """
    last, second_last = n % 10, n//10 % 10
    if last == 8 and second_last == 8:
        return True
    elif n < 100:
        return False
    return double_eights(n // 10)

    # Alternate solution
    last, second_last = n % 10, n//10 % 10
    if n < 10:
        return False
    return (last == 8 and second_last == 8) or double_eights(n//10)


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x ** 2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[x, fn(x)] for x in seq if fn(x) in range(lower, upper+1)]

def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], .... where M is position of the
    second half of the deck. Assume that len(DECK) is even.

    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    return [deck[i // 2] if i % 2 == 0 else deck[len(deck) //2 + i//2] for i in range(len(deck))]