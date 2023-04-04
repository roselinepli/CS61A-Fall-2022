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


def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    # if link is Link.empty:
    #     return []
    # return [link.first] + convert_link(link.rest)

    # res = []
    # while link is not Link.empty:
    #     res.append(link.first)
    #     link = link.rest
    # return res

    if link is Link.empty:
        return []
    if type(link.first) == Link:
        return [convert_link(link.first)] + convert_link(link.rest)
    return [link.first] + convert_link(link.rest)