(define (duplicate lst)
    (cond
        ((null? lst) lst)
        ((null? (cdr lst)) (cons (car lst) (cons (car lst) nil)))
        (else (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))
(expect (duplicate '(1 1)) (1 1 1 1))
