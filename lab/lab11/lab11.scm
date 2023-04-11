(define (over-or-under num1 num2) (cond ((< num1 num2) '-1)
((= num1 num2) '0) ((> num1 num2) '1)))

(define (over-or-under num1 num2) (if (< num1 num2) '-1 (if (= num1 num2) '0 '1)))

(define (make-adder num) (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n) (define (repeated-f x) (if (= n 0) x (repeated-f (f x)) (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 'YOUR-CODE-HERE)
