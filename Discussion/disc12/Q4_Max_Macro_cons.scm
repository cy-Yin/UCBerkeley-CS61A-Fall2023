(define-macro (max expr1 expr2)
    (cons 'if (cons (cons '> (cons expr1 (cons expr2 nil))) (cons expr1 (cons expr2 nil))))
    )

; Test
(expect (max -3 (+ 1 2)) 3)
(expect (max 1 1) 1)
