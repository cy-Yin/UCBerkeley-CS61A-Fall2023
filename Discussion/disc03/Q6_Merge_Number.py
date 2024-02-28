def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    
    
    > merge(841, 62)
    1 + 10 * merge(84, 62) -> merge(84, 62)1
    > merge(84, 62)
    merge(84, 6)2
    >   merge(841, 62)
    --> merge(84, 62)1
    --> merge(84, 6)21
    --> merge(8, 6)421
    --> merge(8, 0)6421
    --> 86421
    >>> merge(841, 62)
    86421
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    else:
        all_but_last_n1, last_n1 = n1 // 10, n1 % 10
        all_but_last_n2, last_n2 = n2 // 10, n2 % 10
        if last_n1 < last_n2:
            return last_n1 + 10 * merge(all_but_last_n1, n2)
        elif last_n1 >= last_n2:
            return last_n2 + 10 * merge(n1, all_but_last_n2)
            
