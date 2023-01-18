def ordered_digits(x):
    """Return True if the (base 10) digits of x > 0 are in
    non-decreasing order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375)
    >>> result
    False
    """
    last = x % 10
    x = x // 10
    while x > 0 and last >= x % 10:
        last = x % 10
        x = x // 10
    return x == 0

def get_k_run_starter(n,k):
    """Returns the 0th digit of the kth increasing run within n.

    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 0)
    3
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    while i <= k:
        while n > 10 and (n % 10 > (n //10) % 10):
            n //= 10
        final = n % 10
        i += 1
        n //= 10
    return final

from operator import add, mul
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1)
    243
    >>> make_repeater(square, 2)(5)
    625
    >>> make_repeater(square, 4)(5)
    152587890625
    >>> make_repeater(square, 0)(5)
    5
    """
    def inner_func(x):
        k = 0
        while k < n:
            x = func(x)
            k += 1
        return x
    return inner_func

# def make_repeater(func, n):
#     g = identity
#     while n > 0:
#         g = composer(func, g)
#         n -= 1
#     return g

# def composer(func1, func2):
#         """Return a function f, such that f(x) = func1(func2(x))."""
#         def f(x):
#             return func1(func2(x))
#         return f

def apply_twice(func):
    return make_repeater(func, 2)

def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i += 1
    return checker

def div_by_primes_under_no_lambda(n):
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f, i):
                def inner(x):
                    return x % i == 0 or f(x)
                return inner
            checker = outer(checker, i)
        i += 1
    return checker