test = {
  'name': 'swap',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (swap '(- 1 2))
          (- 2 1)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (swap '(list (- 10 5) (+ 1 4) 5 10))
          (list (- 10 5) (+ 1 4) 5 10)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (swap '(- 1 (+ 3 5) 7))
          (- (+ 3 5) 1 7)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (swap '(+ 3 5 (/ 1 0) 7))
          (+ 5 3 (/ 1 0) 7)
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
