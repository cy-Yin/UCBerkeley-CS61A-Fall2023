def lgk_pow(n,k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        if k % 2 != 0:
            return n * lgk_pow(n * n, (k - 1) // 2)
        else:
            return lgk_pow(n * n, k // 2)
