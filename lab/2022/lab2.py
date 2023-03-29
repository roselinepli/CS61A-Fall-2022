def lambda_curry2(func):
    """
    Return a Curried version of a two_argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> and_three = curried_add(3)
    >>> and_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda arg1: lambda arg2: func(arg1, arg2)

def count_factors(n):
    """
    Return the number of positive factors that n has.
    >>> count_factors(6)
    4
    >>> count_factors(4)
    3
    """
    count, i = 0, 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3
    >>> count_primes(13)
    6
    """
    count, i = 0, 1
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2

def count_cond(condition):
    """Return a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two_argument predicate function Condition, where the
    first argument for Condition is N and the second argument is the number from 1 to N.
    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)
    2
    >>> count_factors(12)
    6
    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(20)
    8
    """
    def counter(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return counter

def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3
    >>> a2 = composer(mul_three, a1)
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """Return a function with one parameter x that returns True if f(g(x)) is equal
    to g(f(x)). You can assume the result of g(x) is a valid input for f and vice versa.

    >>> add_one = lambda x: x + 1
    >>> square = lambda x: x** 2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)
    True
    >>> b1(4)
    False
    """
    # def identity(x):
    #     return composer(f, g)(x) == composer(g, f)(x)
    # return identity

    return lambda x: f(g(x)) == g(f(x))

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
            return x + 1
    >>> def times2(x):
            return x * 2
    >>> def add3(x):
            return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn