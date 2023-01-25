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
    for i in range(cnt):
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
    pass

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
        return helper(i+1)
    return helper(2)