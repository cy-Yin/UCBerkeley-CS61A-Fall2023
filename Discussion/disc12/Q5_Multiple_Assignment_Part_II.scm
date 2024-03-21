(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(begin (define ,sym2 (list ,expr1 ,expr2))
            (define ,sym1 (car ,sym2))
            (define ,sym2 (car (cdr ,sym2)))
            undefined)
)

; Tests
(multi-assign x y 1 2)
(expect (= x 1) #t)
(expect (= y 2) #t)
(multi-assign x y y x)
(expect (= x 2) #t)
(expect (= y 1) #t)
