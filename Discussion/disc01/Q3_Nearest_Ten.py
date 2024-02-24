def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    remainder = n % 10
    if remainder >= 5:
        nearest = n + (10 - remainder)
    elif remainder < 5:
        nearest = n - remainder

    return nearest