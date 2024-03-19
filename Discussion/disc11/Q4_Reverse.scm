(define (reverse lst)
    (if (null? lst)
        nil
        (append 
            (reverse (cdr lst)) 
            (list (car lst))) ; the scheme "append" func needs to add a list rather than a number, unlike to python
    )
)
