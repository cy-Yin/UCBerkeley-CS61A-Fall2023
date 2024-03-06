def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    "*** YOUR CODE HERE ***"
    # (x1 / x2) / (y1 / y2) = (x1 * y2) / (x2 * y1)
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))

