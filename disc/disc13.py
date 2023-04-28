# def paths(x, y):
#     """Return a list of ways to reach y from x by repeated incrementing
#     or doubling.
#     >>> paths(3, 5)
#     [[3, 4, 5]]
#     >>> sorted(paths(3, 6))
#     [[3, 4, 5, 6], [3, 6]]
#     >>> paths(3, 3)
#     [[3]]
#     >>> paths(5, 3)
#     []
#     """
#     if x > y:
#         return []
#     elif x == y:
#         return [[x]]
#     else:
#         a = paths(x+1, y)
#         b = paths(x*2, y)
#         return [[x] + i for i in a] + [[x] + i for i in b]


# def reverse(lst):
#     """Reverse lst using mutation.

#     >>> original_list = [5, -1, 29, 0]
#     >>> reverse(original_list)
#     >>> original_list
#     [0, 29, -1, 5]
#     >>> odd_list = [42, 72, -8]
#     >>> reverse(odd_list)
#     >>> odd_list
#     [-8, 72, 42]
#     """
#     i, j = 0, len(lst)-1
#     while i < j:
#         lst[i], lst[j] = lst[j], lst[i]
#         i += 1
#         j -= 1


# def widest_level(t):
#     """
#     >>> sum([[1], [2]], [])
#     [1, 2]
#     >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]), Tree(4, [Tree(9, [Tree(2)])])])
#     >>> widest_level(t)
#     [1, 5, 9]
#     """
#     levels = []
#     x = [t]
#     while x:
#         levels.append([b.label for b in x])
#         x = sum([i.branches for i in x], [])
#     return max(levels, key=len)

# def in_order_traversal(t):
#     """
#     Generator function that generates an "in-order" traversal, in which we
#     yield the value of every node in order from left to right, assuming that
#     each node has either 0 or 2 branches.

#     >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
#     >>> list(in_order_traversal(t))
#     [4, 2, 6, 5, 7, 1, 3]
#     """
#     if t.is_leaf():
#         yield t.label
#     elif len(t.branches) == 2:
#         left, right = t.branches
#         yield from in_order_traversal(left)
#         yield t.label
#         yield from in_order_traversal(right)
#     else:
#         raise ValueError("Tree does not have 0 or 2 branches")


# def deep_map(f, link):
#     """Return a Link with the same structure as link but with fn mapped over
#     its elements. If an element is an instance of a linked list, recursively
#     apply f inside that linked list as well.

#     >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
#     >>> print(deep_map(lambda x: x * x, s))
#     <1 <4 9> 16>
#     >>> print(s) # unchanged
#     <1 <2 3> 4>
#     >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
#     <<2 <4 6> 8> <<10>>>
#     """
#     if link is Link.empty:
#         return link
#     elif isinstance(link.first, Link):
#         return Link(deep_map(f, link.first), deep_map(f, link.rest))
#     else:
#         return Link(f(link.first), deep_map(f, link.rest))


def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        g = lambda x: f(generated_func(x))
        generated_func = yield g


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'