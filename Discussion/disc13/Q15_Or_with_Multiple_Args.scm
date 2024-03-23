(define (make-long-or args)
    (if (null? args)
        #f
        `(let ((value ,(car args)))
            (if value
                value
                ,(make-long-or (cdr args))
            )
        )
    )
)


(expect (eval (make-long-or '((print 'hello) (/ 1 0) 3 #f)))
hello)
(expect (eval (make-long-or '((= 1 0) #f (+ 1 2) (print 'goodbye))))
3)
(expect (eval (make-long-or '((> 3 1))))
#t)
(expect (eval (make-long-or '()))
#f)


; Initially, the solution provided appears to correctly implement the make-long-or function
;
; (define (make-long-or args)
;     (if (null? args)
;         #f
;         `(if ,(car args)
;             ,(car args)
;             ,(make-long-or (cdr args))
;          )
;     )
; )
;
; However, it fails the first doctest
; (expect (eval (make-long-or '((print 'hello) (/ 1 0) 3 #f))) hello)
; 
; In this case, the failure stems from the fact that the code outputs two instances of "hello" due to the nature of its execution. 
; When the second "if" prediction is evaluated, it prints "hello" before evaluating the true condition, which also happens to be a "print" function.
; 
; To rectify this issue, a modification is introduced utilizing a let statement. 
; This modification involves assigning the result of "(print 'hello)" to a variable "value" within the "let", effectively resulting in None. 
; Consequently, in this updated version, the program prints "hello" only once within the scope of the let, resolving the duplication problem encountered in the initial implementation.