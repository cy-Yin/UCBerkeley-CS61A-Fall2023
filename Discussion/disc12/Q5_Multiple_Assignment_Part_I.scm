(define-macro (multi-assign sym1 sym2 expr1 expr2)
    `(begin (define ,sym1 ,expr1) (define ,sym2 ,expr2) undefined)
)

; Tests
(multi-assign x y 1 2)
(expect (= x 1) #t)
(expect (= y 2) #t)
