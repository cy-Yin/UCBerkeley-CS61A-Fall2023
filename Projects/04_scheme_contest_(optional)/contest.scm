;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: lambda
;;;
;;; counted 228 tokens
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (caar lst) (car (car lst)))
(define (cadr lst) (car (cdr (car lst))))

; Helper function: performs goto on a list
(define (list-goto lst)
  (if (not (null? lst))
    (begin
      (goto (caar lst) (cadr lst))
      (list-goto (cdr lst))
    )
  )
)

; Draw an line 
(define (line-poly poly)
  (penup)
  (goto (caar poly) (cadr poly))
  (pendown)
  (list-goto (cdr poly))
  (penup)
)

; Draw a filled polygon
(define (fill-poly poly)
  (penup)
  (goto (caar poly) (cadr poly))
  (begin_fill)
  (list-goto (cdr poly))
  (end_fill)
)

(define (draw)
  ; YOUR CODE HERE
  (speed 10)
  (color "black")

  (fill-poly 
    '(
      (-140 160)
      (-10 160)
      (110 -60)
      (140 -60)
      (160 -100)
      (80 -100)
      (-40 120)
      (-120 120)
      (-140 160)
    )
  )
  (fill-poly
    '(
      (-20 100)
      (20 71.43)
      (-100 -100)
      (-160 -100)
      (-20 100)
    )
  )

  (ht)
  (exitonclick))

; Please leave this last line alone. You may add additional procedures above
; this line.
(draw)