(define (square x) (* x x))

(define (vir-fib n)
  (cond ((<= n 1) n)
        ((= n 2) 1)
        (else (+ (vir-fib (- n 1))
                 (vir-fib (- n 2))))))


(define with-list (list(list 'a 'b) 'c 'd (list 'e)))

(define with-quote '((a b) c d (e)))

(define helpful-list
    (cons 'a (cons 'b nil)))

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))

(define with-cons
    (cons (helpful-list) (another-helpful-list)))

(define (list-concat a b)
    if (null? a) b (cons (car a) (list-concat (cdr a) b)))

(define (remove item lst)
    (cond ((null? lst) '())
    ((equal? item (car lst))(remove item (cdr lst)))
    (else (cons (car lst) (remove item (cdr lst))))))

(define (duplicate lst)
    (cond ((null? lst) '())
    (else (cons (car lst) (cons car lst) (duplicate (cdr lst))))))