;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((= total 0) (list nil))
    ((or (< total 0) (null? denoms)) nil)
    (else (append
            (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
            (list-change total (cdr denoms))
          )
    )
  )
)


(expect
    (list-change 10 '(25 10 5 1))
    ((10) (5 5) (5 1 1 1 1 1) (1 1 1 1 1 1 1 1 1 1))
)
(expect
    (list-change 5 '(4 3 2 1))
    ((4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1))
)