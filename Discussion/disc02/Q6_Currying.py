def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    def first_num(x1):
        def second_num(x2):
            return func(x1, x2)
        return second_num
    return first_num
    
# Alternate
# def curry(func):
#     return lambda x1: lambda x2: func(x1, x2)
