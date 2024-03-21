(define (replace-helper e o n)
  (if (pair? e)
      (cons (replace-helper (car e) o n) (replace-helper (cdr e) o n))
      (if (eq? e o) n e)))
(define-macro (replace expr old new)
    (replace-helper expr old new))

; Tests
(expect (replace (define x 2) x y) y)
(expect (= y 2) #t)
(expect (replace (+ 1 2 (or 2 3)) 2 0) 1)
