def add_this_many(x, el, s):
    """Adds el to the end of s the number of times x occurs in s.

    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    cnt = 0
    for num in s:
        if num == x:
            cnt += 1
    for _ in range(cnt):
        s.append(el)


def countdown(n):
    print("Beginning countdowm!")
    while n >= 0:
        yield n
        n -= 1
    print("Blastoff!")


def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even))
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for elem in iterable:
        if f(elem):
            yield elem


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    # for elem in range(n, 1, -1):
    #     if is_prime(elem):
    #         yield elem

    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)


def preorder(t):
    """Return a list of the entries in this tree in the order that they would
    be visited by a preorder traversal (see problem description).
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    flattened_branches = []
    for child in branches(t):
        flattened_branches += preorder(child)
    return [label(t)] + flattened_branches

def preorder(t):
    yield label(t)
    for b in branches(t):
        yield from generate_preorder(b)