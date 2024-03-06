def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    # total = 0
    # for b in branches(t):
    #     total = total + sum_tree(b)
    # return label(t) + total
    return label(t) + sum([sum_tree(b) for b in branches(t)])