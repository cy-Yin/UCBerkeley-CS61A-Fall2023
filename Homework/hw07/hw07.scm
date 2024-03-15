(define (square n) (* n n))

(define (pow base exp) 
  (cond 
    ((= exp 0) 1)
    ((even? exp) (square (pow base (/ exp 2))))
    ((odd? exp) (* base 
                  (square (pow base (/ (- exp 1) 2)))))
    ))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
