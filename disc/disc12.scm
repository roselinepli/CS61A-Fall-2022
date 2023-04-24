; helper function
; returns the values of lst that are bigger than x
; e.g.,(larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
   (filter ((lambda (v)) (> v x)) lst))

(define (longest-increasing-subsequence lst)
   (if (null? lst) nil
       (begin
           (define first (car lst))
           (define rest (cdr lst))
           (define large-value-rest
               (larger-values first rest))
           (define with-first
               (cons
                   (car lst)
                   (longest-increasing-subsequence larger-values-rest)))
            (define without-first
                (longest-increasing-subsequence rest))
            (if (> (length with-first) (length without-first))
                 with-first
                 without-first))))
(expect (longest-increasing-subsequence '()) ())
(expect (longest-increasing-subsequence '(1)) (1))
(expect (longest-increasing-subsequence '(1 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 8 7 6 5 4 3 2 3)) (1 2 3))
(expect (longest-increasing-subsequence '(1 9 8 7 2 3 6 5 4 5)) (1 2 3 4 5))
(expect (longest-increasing-subsequence '(1 2 3 4 9 3 4 1 10 5)) (1 2 3 4 9 10))