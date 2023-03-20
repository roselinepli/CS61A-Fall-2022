def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of n stairs,
    moving either 1 step or 2 steps at a time.

    >>> count_stair_ways(4)
    5
    """
    if n == 1 or n == 2:
        return n
    return count_stair_ways(n-1) + count_stair_ways(n-2)


def count_k(n, k):
    """Counts the number of paths up a flight of n stairs when taking up to
    and including k steps at a time.

    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_k(n-i, k)
            i += 1
    return total


def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(s) if i % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    return max(max_product(s[1:]), s[0] * max_product(s[2:]))

