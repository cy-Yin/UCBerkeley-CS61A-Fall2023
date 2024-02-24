from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE=__file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    total = 1
    while n > 0:
        total = total * term(n)
        n = n - 1

    return total


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    i = 1
    total = start
    while i <= n:
        total = merger(total, term(i))
        i = i + 1
    return total


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def funception(func1, begin):
    """ Takes in a function (func1) and a begin value.
    Returns a function (func2) that will find the product of
    func1 applied to the range of numbers from
    begin (inclusive) to end (exclusive)

    >>> def increment(num):
    ...     return num + 1
    >>> def double(num):
    ...     return num * 2
    >>> g1 = funception(increment, 0)
    >>> g1(3)    # increment(0) * increment(1) * increment(2) = 1 * 2 * 3 = 6
    6
    >>> g1(0)    # Returns 1 because begin >= end
    1
    >>> g1(-1)   # Returns 1 because begin >= end
    1
    >>> g2 = funception(double, 1)
    >>> g2(3)    # double(1) * double(2) = 2 * 4 = 8
    8
    >>> g2(4)    # double(1) * double(2) * double(3) = 2 * 4 * 6 = 48
    48
    >>> g3 = funception(increment, -3)
    >>> g3(-1)   # increment(-3) * increment(-2) = -2 * -1 = 2
    2
    """
    "*** YOUR CODE HERE ***"
    def func2(end):
        if begin >= end:
            return 1
        else:
            product = 1
            i = begin
            while i < end:
                product = product * func1(i)
                i = i + 1
            return product

    return func2


def mul_by_num(num):
    """Returns a function that takes one argument and returns num
    times that argument.

    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    return lambda num1: num * num1


def add_results(f1, f2):
    """
    Return a function that takes in a single variable x, and returns
    f1(x) + f2(x). You can assume the result of f1(x) and f2(x) can be
    added together, and they both take in one argument.

    >>> identity = lambda x: x
    >>> square = lambda x: x**2
    >>> a1 = add_results(identity, square) # x + x^2
    >>> a1(4)
    20
    >>> a2 = add_results(a1, identity)     # (x + x^2) + x
    >>> a2(4)
    24
    >>> a2(5)
    35
    >>> a3 = add_results(a1, a2)           # (x + x^2) + (x + x^2 + x)
    >>> a3(4)
    44
    """
    return lambda x: f1(x) + f2(x)


def mod_maker():
    """Return a two-argument function that performs the modulo operation and
    returns True if the numbers are divisble, and the remainder otherwise.

    >>> mod = mod_maker()
    >>> mod(7, 2) # 7 % 2
    1
    >>> mod(4, 8) # 4 % 8
    4
    >>> mod(8,4) # 8 % 4
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'mod_maker', ['If', 'IfExp']) # no if / if-else statements
    True
    """
    return lambda x, y: x % y or True


def lambda_math_syntax_check():
    """Checks that definitions of summation_using_accumulate and
    produce_using_accumulate are each a single return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(mul_by_num)).body[0].body]
    ['Expr', 'Return']
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(add_results)).body[0].body]
    ['Expr', 'Return']
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(mod_maker)).body[0].body]
    ['Expr', 'Return']
    """

