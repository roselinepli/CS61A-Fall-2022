def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.

    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    # return [fn(i) for i in seq]
    res = []
    for i in seq:
        res += fn(i)
    return res

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    # res = []
    # for elem in seq:
    #     if pred(elem):
    #         res.append(elem)
    # return res

    return [elem for elem in seq if pred(elem)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3])
    11
    """
    total = seq[0]
    for elem in seq[1:]:
        total = combiner(total, elem)
    return total

def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings L
    (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    # count = 0
    # for elem in L:
    #     if elem.lower() == elem.lower()[::-1]:
    #         count += 1
    # return count

    return len(my_filter(lambda s: s.lower() == s[::-1].lower(), L))

