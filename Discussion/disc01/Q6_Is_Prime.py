def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    prime = True
    if n == 1:
        prime = False
    else:
        i = 2
        while i <= n - 1:
            if n % i == 0:
                prime = False
            i = i + 1

    return prime