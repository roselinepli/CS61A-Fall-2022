def falling(n, k):
    """"Compute the falling factorial of n to depth k.
    >>> falling(6, 3) # 6 * 5 * 4
    120
    >>> falling(4, 3) # 4 * 3 * 2
    24
    >>> falling(4, 1) # 4
    4
    >>> falling(4, 0)
    1
    """
    # total = 1
    # if k == 0:
    #     return 1
    # while k > 0:
    #     total *= n
    #     n -= 1
    #     k -= 1
    # return total
    total, stop = 1, n-k
    while n > stop:
        total, n = total * n, n - 1
    return total

def sum_digits(y):
    """Sum all the digits of y.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    res = 0
    while y > 0:
        res += y % 10
        y = y // 10
    return res

def double_eights(n):
    """"Return true if n has two 8 in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(808080)
    False
    """
    prev_eight = False
    while n > 0:
        if n % 10 == 8 and prev_eight:
            return True
        elif n % 10 == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False