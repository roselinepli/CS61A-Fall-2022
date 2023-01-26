def merge(a, b):
    """
    >>> def sequence(start, step):
            while True:
                yield start
                start += step
    >>> a = sequence(2, 3)
    >>> b = sequence(3, 2)
    >>> result = merge(a, b)
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_num, b_num = next(a), next(b)
    while True:
        if a_num < b_num:
            yield a_num
            a_num = next(a)
        elif a_num == b_num:
            yield a_num
            a_num = next(a)
            b_num = next(b)
        elif a_num > b_num:
            yield b_num
            b_num = next(b)

def gen_perms(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = gen_perms([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
            next(perms)
        except StopIteration:
            print('No more permutations!")
    No more permutations!
    >>> sorted(gen_perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(gen_perms((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(gen_perms("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not seq:
        yield []
    else:
        for perm in gen_perms(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + [seq[0] + perm[i:]]

def yield_paths(t, value):
    """Yields all possible paths from the root of t to a node with the lable value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    """
    if label(t) == value:
        yield [label(t)]
    for branch in branches(t):
        for path in yield_paths(branch, value):
            yield [label(t)] + path

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Return True if the given tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

