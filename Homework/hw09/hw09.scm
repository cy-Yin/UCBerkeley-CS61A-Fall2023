(define (curry-cook formals body)
  (if (null? formals)
    body
    `(lambda ,(cons (car formals) nil) ,(curry-cook (cdr formals) body))
  )
)

(define (curry-consume curry args)
  (if (null? args)
      curry
      (curry-consume (curry (car args)) (cdr args))
  )  
)

(define-macro (switch expr cases)
  (switch-to-cond (list 'switch expr cases)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map
         (lambda (case) (cons `(equal? ,(car (cdr switch-expr)) ,(car case)) (cdr case)))
         (car (cdr (cdr switch-expr))))))

(define (min x y)
  (if (< x y)
      x
      y))

(define (count f n i)
  (if (= i 0)
      0
      (+ (if (f n i)
             1
             0)
         (count f n (- i 1)))))

(define (is-factor dividend divisor)
  (if (equal? (modulo dividend divisor) 0)
      #t
      #f))

(define (switch-factors n)
  (switch (min 2 (count is-factor n (- n 1))) ((0 'one) (1 'prime) (2 'composite))))

; switch-factors func
; other than itself, we count the factor of n from 1 to n - 1
; if n = 1, "count" give 0
; if 1 is the only factor of n, then n is a prime number, "count" gives 1
; if 1 and k (ranging from 2 to n - 1) and more "k"s are the factors of n, then "count" gives the num >= 2
; Therefore, just compare the minimum of 2 and count result, min(2, count) = 2 if n is a composite ("count" >= 2).