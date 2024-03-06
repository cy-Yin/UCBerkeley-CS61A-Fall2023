def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
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
    "*** YOUR CODE HERE ***"
    # for branch in branches(t):
    #     if sum_tree(branches(t)[0]) != sum_b or not balanced(branch):
    #         return False
    # return True
    return (not False in [sum_tree(branches(t)[0]) == sum_tree(branch) for branch in branches(t)]) and \
             (not False in [balanced(branch) for branch in branches(t)])
    