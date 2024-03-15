(define (ascending? s) 
    (if (or (null? s) (null? (cdr s)))
        #t
        (and (<= (car s) (car (cdr s))) 
             (ascending? (cdr s))))
)

(define (my-filter pred s) 
    (cond 
        ((null? s) nil)
        ((eq? #t (pred (car s))) (cons (car s) (my-filter pred (cdr s))))
        ((eq? #f (pred (car s))) (my-filter pred (cdr s))))
)

(define (interleave lst1 lst2) 
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))))
)

(define (no-repeats s) 
    (cond
        ((null? s) nil)
        ((null? (cdr s)) s)
        (else (cons (car s) (no-repeats (filter (lambda (x) (not (= (car s) x)))(cdr s))))))    
)
