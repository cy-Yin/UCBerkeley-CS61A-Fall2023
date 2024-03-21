(define-macro (max expr1 expr2)
    (list 'if (list '> expr1 expr2) expr1 expr2)
    )

; Test
(expect (max -3 (+ 1 2)) 3)
(expect (max 1 1) 1)
