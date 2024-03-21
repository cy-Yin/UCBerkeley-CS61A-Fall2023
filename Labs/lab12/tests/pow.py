test = {
  'name': 'powers',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define expr (pow-expr 5 1))
          expr
          scm> (eval expr)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define expr2 (pow-expr 5 2))
          expr2
          scm> (eval expr2)
          25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (eval (pow-expr 3 4))
          81
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (eval (pow-expr 7 0))
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
