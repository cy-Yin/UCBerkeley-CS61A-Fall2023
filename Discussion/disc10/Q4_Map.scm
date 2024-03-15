(define (map-fn fn lst)
    (if (null? lst)
        lst
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)
