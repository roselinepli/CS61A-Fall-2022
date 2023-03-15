def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def is_prime(n):
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None # No return value
    True
    """
    i = 1
    while i <= n:
    # for n in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1
print(fizzbuzz(16))


def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309)  #All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(100000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    """
    num = 0
    while n > 0:
        last = n % 10
        n //= 10
        if not has_digit(n, last):
            num += 1
    return num

def has_digit(n, k):
    """Return whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    while n > 0:
        last = n % 10
        n //= 10
        if last == k:
            return True
    return False