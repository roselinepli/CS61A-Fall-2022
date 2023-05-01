(define (nondecreaselist s)
    (if (null? s) nil
        (let ((rest (nondecreaselist (cdr s))))
            (if (or (null? (cdr s)) (> (car s) (car (cdr s))))
                (cons (list (car s)) rest)
                (cons (cons (car s) (car rest)) (cdr rest))))))

SELECT m.day, m.time FROM records AS r, meetings as m WHERE r.division = m.division
AND r.supervisor = 'Oliver Warbucks';

SELECT e.name FROM records AS e, records AS s WHERE e.supervisor = s.name AND e.division != s.division;

SELECT m.day FROM records AS e, meetings AS m WHERE e.division = m.division GROUP BY m.day HAVING COUNT(*) < 5;
