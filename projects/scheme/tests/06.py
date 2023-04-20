test = {
  'name': 'Problem 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          2
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          5
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = Pair(1, Pair(2, Pair(3, nil)))
          >>> eval_all(s, env)
          3
          >>> s     # The list should not be mutated!
          Pair(1, Pair(2, Pair(3, nil)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          11
          scm> (begin (define x 3) x)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          (+ 2 2)
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
          1a9a3321b8b99a0f9291d89be986e74c
          # locked
          scm> x
          eb892a26497f936d1f6cae54aacc5f51
          # locked
          scm> y
          2b7cdec3904f986982cbd24a0bc12887
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          scm> (begin (+ 1 2) nil)
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 0 1 2 0)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
