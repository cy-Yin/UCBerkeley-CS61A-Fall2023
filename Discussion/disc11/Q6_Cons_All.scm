(define (cons-all first rests)
  (map (lambda (rest) (cons first rest)) rests)
)

(expect (cons-all 1 '((2 3) (2 4) (3 5))) ((1 2 3) (1 2 4) (1 3 5)))