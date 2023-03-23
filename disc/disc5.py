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

def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    # if is_leaf(t):
    #     return 0
    # best_height = 0
    # for b in branches(t):
    #     best_height = max(height(b), best_height)
    # return best_height + 1

    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])

def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    # if is_leaf(t):
    #     return label(t)
    # max_sum = 0
    # for b in branches(t):
    #     max_sum = max(max_path_sum(b), max_sum)
    # return label(t) + max_sum

    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(b) for b in branches(t)])


def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = [find_path(b, x)]
        if path:
            return [label(t)] + path

def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    total = 0
    for b in branches(t):
        total += sum_tree(b)
    return label(t) + total


def balanced(t):
    """
    Checks if each branch has same sum of all elements and if
    each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b):
            return False
    return True


def sprout_leaves(t, leaves):
    """
    Sprout new leaves containing the data in leaves at each leaf in the original
    tree t and return the resulting tree.
    """
    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])


def hailstone_tree(n, h):
    """
    Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    """
    if h == 0:
        return label(n)
    branches = [hailstone_tree(n * 2, h-1)]
    if (n-1) % 3 == 0 and ((n-1) // 3) % 2 == 1 and (n - 1) // 3 > 1:
        branches += [hailstone_tree((n - 1) // 3, h-1)]
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i+1, b)
    helper(0, t)