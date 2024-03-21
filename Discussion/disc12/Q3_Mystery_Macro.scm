(define-macro (mystery expr)
    `(let ((/ (lambda (a b) (if (= b 0) 1 (/ a b))))) ,expr))

(define (letter-grade earned possible)
    (mystery
        (cond
            ((>= (/ earned possible) 0.9) 'A)
            ((>= (/ earned possible) 0.8) 'B)
            ((>= (/ earned possible) 0.7) 'C)
            ((>= (/ earned possible) 0.6) 'D)
            (else 'F)
        )
    )
)

; Tests
(expect (letter-grade 100 0) A)
(expect (letter-grade 95 100) A)
(expect (letter-grade 85 100) B)
(expect (letter-grade 75 100) C)
(expect (letter-grade 65 100) D)
(expect (letter-grade 55 100) F)
