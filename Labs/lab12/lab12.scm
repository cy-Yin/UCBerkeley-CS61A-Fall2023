(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false)  
)

(define (pow-expr n p)
  (cond
      ((= p 0) 1)
      ((= p 1) `(* ,p ,n))
      (else `(* ,(pow-expr n (- p 1)) ,n))
  )
)

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr)
  (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
    (if (> (eval second) (eval first))
        (cons op (cons second (cons first rest)))
        expr
    )  
  ))

; Hint:
; for question 4 swap func,
; if I want to use quasiquote, I may give 
; `(,op ,second ,first ,rest)
; while each element of the scheme list has been unquoted in the list and quasiquoted before the whole list
; this quote/unquote does nothing in fact.
; However it is necessary to notice that ",rest" gives "()" (namely "nil") if there are just two operands in expr
; which we do not want to return explicitely in the final expression.
; So just the normal "cons" is fine to this question.