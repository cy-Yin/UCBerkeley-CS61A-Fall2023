def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # k = 2
    # while k < n:
    #     if n % k == 0:
    #         return False
    #     k = k + 1
    # return True
    def check(k):
        if k == n:
            return True
        elif n % k == 0:
            return False
        else:
            return check(k + 1)
    
    return check(2)