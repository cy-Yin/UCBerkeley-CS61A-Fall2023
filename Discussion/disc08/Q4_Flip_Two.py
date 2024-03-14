def flip_two(s):
    """
    Flips every pair of values in s.

    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    if s == Link.empty or s.rest == Link.empty:
        return
    else:
        first_elem = s.first
        second_elem = s.rest.first
        s.first = second_elem
        s.rest.first = first_elem
        return flip_two(s.rest.rest)

"*** YOUR CODE HERE ***"

